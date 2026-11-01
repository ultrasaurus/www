#!/usr/bin/env python3
"""Writes source/_redirects for Cloudflare Pages (step 9).

Old URLs -> where they live now, so links from other sites keep working:

* Movable Type posts, /sarahblog/archives/NNNNNN.html (movable-type.yaml,
  from map_movable_type.py --all)
* other old pages matched by hand (BY_HAND in fix_old_paths.py)
* WordPress posts whose slug changed (_wp_old_slug in the export)
* WordPress pages the new site doesn't have: month and year archives
  (and their extra pages, from www-archive) -> /archives/,
  /category/uncategorized/, /author/sarah/
* patterns: old uploads, /sarahblog/YYYY/MM/slug, anything else under
  /sarahblog/ or /code/, and /page/N/

Feeds and tag pages stay 404: the new site has neither (RSS is skipped
for now, see plan.md).

Cloudflare follows a redirect even when a file exists at that path, so a
pattern like /:year/:month/ would also catch /category/code/; month
archives are listed one by one instead. Checks that every target exists
in the source and that no old path is a page of the new site.

Usage: python3 make_redirects.py
"""
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from fix_old_paths import BY_HAND, MOVED, is_published

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
SOURCE = SITE / "source"
EXPORT = SITE / "export" / "all-theevolvingultrasaurus.WordPress.2021-04-13.xml"
ARCHIVE = SITE.parent / "www-archive"
OUT = SOURCE / "_redirects"
NS = {"wp": "http://wordpress.org/export/1.2/"}

# MT month pages go to /archives/ with the rest (BY_HAND sends this one to
# a post only for the link that called it "my second posting")
NOT_REDIRECTED = {"/sarahblog/archives/2003_03.html"}

PATTERNS = [
    ("/wp-content/uploads/*", "/uploads/:splat"),
    ("/sarahblog/:year/:month/:slug/", "/:year/:month/:slug/"),
    ("/sarahblog/:year/:month/:slug", "/:year/:month/:slug/"),
    ("/sarahblog/archives/*", "/archives/"),
    ("/sarahblog/*", "/"),
    ("/code/*", "/category/code/"),
    ("/page/*", "/"),
]


def posts_by_id():
    """WordPress post id -> published post path (YYYY/MM/slug)."""
    ids = {}
    for path in SOURCE.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        head = path.read_text().split("\n---", 1)[0]
        m = re.search(r"^id: (\d+)$", head, re.M)
        rel = path.relative_to(SOURCE).with_suffix("").as_posix()
        if m and is_published(rel):
            ids[m.group(1)] = rel
    return ids


def old_slugs():
    """/YYYY/MM/old-slug/ -> /YYYY/MM/slug/ for posts whose slug changed."""
    ids = posts_by_id()
    moved = {}
    for item in ET.parse(EXPORT).getroot().iter("item"):
        post = ids.get(item.findtext("wp:post_id", namespaces=NS))
        if not post:
            continue
        for meta in item.findall("wp:postmeta", NS):
            if meta.findtext("wp:meta_key", namespaces=NS) == "_wp_old_slug":
                old = f"/{post.rsplit('/', 1)[0]}/{meta.findtext('wp:meta_value', namespaces=NS)}/"
                if old != f"/{post}/":
                    moved[old] = f"/{post}/"
    return moved


def wordpress_archives():
    """Month and year archive pages of the live site -> /archives/."""
    pages = {}
    for index in ARCHIVE.glob("[0-9][0-9][0-9][0-9]/**/index.html"):
        parts = index.relative_to(ARCHIVE).parts[:-1]
        # YYYY, YYYY/MM, YYYY/page/N, YYYY/MM/page/N (not posts or feeds)
        if len(parts) == 1 or (len(parts) == 2 and parts[1].isdigit()) or "page" in parts:
            pages["/" + "/".join(parts) + "/"] = "/archives/"
    return pages


def exists(target):
    """Is target a page or file of the new site (or another site)?"""
    if target.startswith("http"):
        return True
    path = SOURCE / target.strip("/")
    if target.endswith("/"):
        return (path.with_suffix(".md").is_file() and is_published(target.strip("/"))) \
            or (path / "index.md").is_file()
    return path.is_file()


def main():
    static = {}
    static.update(MOVED)
    static.update({k: v for k, v in BY_HAND.items() if k not in NOT_REDIRECTED})
    static.update(old_slugs())
    static.update(wordpress_archives())
    static["/category/uncategorized/"] = "/category/general/"
    static["/author/sarah/"] = "/about/"
    # Cloudflare matches /old/ and /old separately; add the no-slash form
    # for pages (not the many month archives, rarely typed by hand)
    archives = wordpress_archives()
    static.update({old.rstrip("/"): new for old, new in list(static.items())
                   if old.endswith("/") and len(old) > 1 and old not in archives})

    bad = [f"{old} -> {new}" for old, new in static.items() if not exists(new)]
    shadow = [old for old in static if exists(old)]
    if bad or shadow:
        raise SystemExit("targets missing:\n  " + "\n  ".join(bad)
                         + "\nold paths that are pages now:\n  " + "\n  ".join(shadow))

    lines = ["# Old URLs -> new ones. Written by make_redirects.py; edit that, not this.",
             "# One-to-one first (Cloudflare uses the first rule that matches)."]
    lines += [f"{old} {new} 301" for old, new in sorted(static.items())]
    lines += ["", "# patterns"]
    lines += [f"{old} {new} 301" for old, new in PATTERNS]
    OUT.write_text("\n".join(lines) + "\n")
    print(f"{len(static)} redirects + {len(PATTERNS)} patterns written to {OUT}")


if __name__ == "__main__":
    main()
