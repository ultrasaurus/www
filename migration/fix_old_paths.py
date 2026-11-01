#!/usr/bin/env python3
"""Rewrites old links to this site in posts to their new paths (step 8).

* /wp-content/uploads/... -> /uploads/... (when the file is there)
* /sarahblog/YYYY/MM/slug/ -> /YYYY/MM/slug/ (when that post is published)
* /sarahblog/archives/NNNNNN.html (Movable Type) -> the post that
  movable-type.yaml (from map_movable_type.py) maps it to
* other old pages in BY_HAND (Coding Notebook, old about pages, ...)

Only links to this site: https://www.ultrasaurus.com/..., //ultrasaurus.com/...
or root-relative /...; another site's /wp-content/ is left alone. Links
whose target doesn't exist are left for check_links.py to report.

Rewrites www-ultrasaurus/source/**/*.md in place; import_comments.py uses
fix_old_paths() on comment text. Safe to re-run.
"""
import re
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "source"

# this site with a scheme or protocol-relative, or a root-relative path
# right after ( " ' = or a space
OWN = r"(?:(?:https?:)?//(?:www\.)?ultrasaurus\.com|(?<=[(\"'=\s]))"
UPLOADS = re.compile(OWN + r"/wp-content(/uploads/[^\s)\"'<>?#]+)", re.I)
SARAHBLOG = re.compile(OWN + r"/sarahblog/(\d{4}/\d\d/[^\s/)\"'<>?#]+)/?", re.I)
MOVABLE_TYPE = re.compile(OWN + r"(/sarahblog/archives/\d{6}\.html)", re.I)


def movable_type_map():
    """Old Movable Type path -> new post path, from movable-type.yaml."""
    mapping = HERE / "movable-type.yaml"
    if not mapping.exists():
        return {}
    return dict(re.findall(r"^(/sarahblog/archives/\d{6}\.html): (\S+)", mapping.read_text(), re.M))


MOVED = movable_type_map()

# other old pages, matched by hand: old path -> new path or URL
BY_HAND = {
    # the 2008 Coding Notebook, a separate Movable Type blog
    "/code/": "/category/code/",
    "/sarahblog/code/": "/category/code/",
    "/code/2008/12/getting-started-with-rails.html": "/2008/12/getting-started-with-rails-2-day-1/",
    "/code/2008/12/rails-day2.html": "/2008/12/getting-started-with-rails-2-day-2/",
    "/code/2008/12/rails-2-day-3.html": "/2008/12/rails-2-day-3-behavior-driven-development/",
    "/code/2008/12/rails-2-day-4-rcov-and-bdd.html": "/2008/12/rails-2-day-4-rcov-and-more-behavior-driven-development/",
    "/code/2008/12/great-ruby-book.html": "/2008/12/great-ruby-book/",
    "/about/sarah.html": "/about/",
    "/about/ultrasaurus.html": "/ultrasaurus/",
    "/sarahblog/archives/2008/01/comet-a-new-term.html": "/2008/01/comet-a-new-term-for-an-old-technique/",
    # the March 2003 month page, linked as "my second posting"
    "/sarahblog/archives/2003_03.html": "/2003/03/are-blogs-the-vanity-press-of-the-internet/",
    # "old design": a copy of the site before the January 2009 rebuild,
    # never archived; the only Wayback capture of the old blog
    "/backup-2009-01-03/": "http://web.archive.org/web/20030425081135/http://www.ultrasaurus.com/sarahblog/",
}
OLD_PAGE = re.compile(
    OWN + "(" + "|".join(re.escape(p) for p in sorted(BY_HAND, key=len, reverse=True))
    + r")(?=[\s)\"'<>#?]|$)", re.I)


def is_published(path):
    post = SOURCE / f"{path}.md"
    if not post.is_file():
        return False
    head = post.read_text().split("\n---", 1)[0]
    return not re.search(r"^status: draft$", head, re.M)


def fix_old_paths(text, counts=None):
    def upload(m):
        if not (SOURCE / urllib.parse.unquote(m.group(1)).lstrip("/")).is_file():
            return m.group(0)
        if counts is not None:
            counts["uploads"] += 1
        return m.group(1)

    def post(m):
        if not is_published(m.group(1)):
            return m.group(0)
        if counts is not None:
            counts["sarahblog"] += 1
        return f"/{m.group(1)}/"

    def movable_type(m):
        new = MOVED.get(m.group(1))
        if not new or not is_published(new.strip("/")):
            return m.group(0)
        if counts is not None:
            counts["movable type"] += 1
        return new

    def old_page(m):
        if counts is not None:
            counts["by hand"] += 1
        return BY_HAND[m.group(1)]

    text = OLD_PAGE.sub(old_page, MOVABLE_TYPE.sub(movable_type, text))
    return SARAHBLOG.sub(post, UPLOADS.sub(upload, text))


def main():
    from collections import Counter

    counts = Counter()
    changed = 0
    for path in sorted(SOURCE.rglob("*.md")):
        text = path.read_text()
        new = fix_old_paths(text, counts)
        if new != text:
            path.write_text(new)
            changed += 1
    print(f"{changed} files changed: {counts['uploads']} /wp-content/uploads links, "
          f"{counts['sarahblog']} /sarahblog/ links, "
          f"{counts['movable type']} Movable Type links, "
          f"{counts['by hand']} other old pages")


if __name__ == "__main__":
    main()
