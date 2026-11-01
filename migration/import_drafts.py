#!/usr/bin/env python3
"""One-time import of the WordPress drafts.

Reads www-ultrasaurus/zz_old/p<id>.md (the drafts as exported in 2021,
kept out of the Eleventy build) and writes each one to
www-ultrasaurus/source/YYYY/MM/<slug>.md with `status: draft`, so
altwebgen builds it only with `dev --drafts`.

* slug: the WordPress slug from the export if the draft has one,
  otherwise made from the title; `-<id>` is added if a post already has
  that name, and untitled drafts are `draft-<id>`
* frontmatter cleaned like import_frontmatter.py: one category (code or
  general; anything else stays Uncategorized, the default), WordPress-only
  keys dropped
* empty drafts (no text) are skipped, except the ones in KEEP_EMPTY
* zz_old/attachment_*.md are images, not posts: skipped

Safe to re-run while zz_old/ exists: a draft is rewritten in place, found
by its `id`. Run fix_wp_html.py and import_comments.py afterwards.
"""
import re
import sys
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

from import_frontmatter import category_of, split_blocks

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
SOURCE = SITE / "source"
DRAFTS = SITE / "zz_old"
EXPORT = SITE / "export" / "all-theevolvingultrasaurus.WordPress.2021-04-13.xml"

NS = {"wp": "http://wordpress.org/export/1.2/"}

# an empty draft kept for its title: "speak truth amidst fear and confusion"
KEEP_EMPTY = {"6695"}
CATEGORIES = {"code", "general"}
# kept when not empty, in this order
KEEP_KEYS = ["title", "date", "id", "excerpt", "tag"]
DROP_IF_EMPTY = {"tag": "[]", "excerpt": "''"}
# the Eleventy exporter wrapped some empty drafts in these
JUNK = re.compile(r'^(<!DOCTYPE html [^>]*>|<\?xml encoding="UTF-8">)\n', re.M)


def wordpress_slugs():
    """WordPress post id -> slug, for drafts that have one."""
    slugs = {}
    for item in ET.parse(EXPORT).getroot().iter("item"):
        name = item.findtext("wp:post_name", namespaces=NS)
        if name:
            slugs[item.findtext("wp:post_id", namespaces=NS)] = urllib.parse.unquote(name)
    return slugs


def slugify(title):
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"&[#\w]+;", " ", text)
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60].rstrip("-")


def existing_ids():
    """source path -> WordPress id, for every post already in source/."""
    ids = {}
    for path in SOURCE.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        m = re.search(r"^id: (\d+)$", path.read_text().split("\n---", 1)[0], re.M)
        ids[path] = m.group(1) if m else None
    return ids


def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def convert(path, slugs, ids, counts):
    text = path.read_text()
    m = re.match(r"^---\n(.*?\n)---\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    blocks = dict(split_blocks(m.group(1).splitlines(keepends=True)))
    post_id = unquote(blocks["id"][0].split(":", 1)[1])
    body = JUNK.sub("", text[m.end():])
    if not body.strip() and post_id not in KEEP_EMPTY:
        counts["empty (skipped)"] += 1
        return

    title = unquote(blocks["title"][0].split(":", 1)[1])
    date = unquote(blocks["date"][0].split(":", 1)[1])
    categories = [c for c in category_of_all(blocks["category"]) if c in CATEGORIES]
    category = categories[0] if len(categories) == 1 else "Uncategorized"

    folder = SOURCE / date[:4] / date[5:7]
    slug = slugs.get(post_id) or slugify(title) or f"draft-{post_id}"
    target = folder / f"{slug}.md"
    if target in ids and ids[target] != post_id:
        target = folder / f"{slug}-{post_id}.md"

    out = ["---\n"]
    for key in KEEP_KEYS:
        block = blocks.get(key)
        if not block:
            continue
        if key in DROP_IF_EMPTY and block[0].split(":", 1)[1].strip() == DROP_IF_EMPTY[key]:
            continue
        out.extend(block)
        if key == "date":
            out.append("status: draft\n")
    if category != "Uncategorized":
        out.append(f"category: {category}\n")
    out.append("---\n")
    out.append(body)

    folder.mkdir(parents=True, exist_ok=True)
    target.write_text("".join(out))
    ids[target] = post_id
    counts[category] += 1


def category_of_all(block):
    """Every category in a frontmatter block (a value or a list)."""
    try:
        return [category_of(block)]
    except ValueError:
        return [l.strip()[2:].strip() for l in block[1:] if l.strip().startswith("- ")]


def main():
    if not DRAFTS.exists():
        sys.exit(f"{DRAFTS} is gone: the drafts were already imported")
    slugs = wordpress_slugs()
    ids = existing_ids()
    counts = Counter()
    for path in sorted(DRAFTS.glob("p*.md")):
        try:
            convert(path, slugs, ids, counts)
        except (ValueError, KeyError) as e:
            sys.exit(f"{path}: {e}")
    print(f"{sum(n for k, n in counts.items() if 'skipped' not in k)} drafts imported")
    for key, n in counts.most_common():
        print(f"  {key}: {n}")


if __name__ == "__main__":
    main()
