#!/usr/bin/env python3
"""One-time frontmatter clean-up for the ultrasaurus.com posts.

Rewrites www-ultrasaurus/src/YYYY/MM/*.md in place (on the `altwebgen`
branch) and writes src/collection.yaml. Post bodies are not touched.

Categories: each WordPress list becomes one value. For Uncategorized
posts, category-review.md decides: reviewed posts (everything up to the
last checked line) become `code` if checked, `general` if not; the rest
stay Uncategorized, which is the collection default, so the key is left
out.

Safe to re-run on its own output.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "source"
REVIEW = HERE / "category-review.md"

# Same for every post, or only meaningful to WordPress/Eleventy.
# (enclosure: podcast mp3 for RSS; the link is also in the post text.)
DROP_KEYS = {"type", "status", "author", "post_format", "enclosure"}
# Dropped only when empty.
DROP_IF_EMPTY = {"tag": "[]", "excerpt": "''"}

COLLECTION_YAML = """\
name: posts
include: "[0-9][0-9][0-9][0-9]/**/*.md"
sort: date
group: category
defaults:
  layout: post
  category: Uncategorized
pretty_urls: true
"""

ITEM = re.compile(r"^- \[([ xX])\] .*?\n  `([^`]+)`", re.M)


def read_review():
    """Map post path (YYYY/MM/slug) -> category, for reviewed posts only."""
    reviewed = REVIEW.read_text().split("\n## Unreviewed", 1)[0]
    return {path: ("general" if mark == " " else "code")
            for mark, path in ITEM.findall(reviewed)}


def split_blocks(lines):
    """Group frontmatter lines into (key, [lines]) top-level blocks."""
    blocks = []
    for line in lines:
        m = re.match(r"^([A-Za-z_-]+):", line)
        if m:
            blocks.append((m.group(1), [line]))
        else:
            blocks[-1][1].append(line)
    return blocks


def category_of(block):
    first = block[0].split(":", 1)[1].strip()
    if first:
        return first
    items = [l.strip()[2:].strip() for l in block[1:] if l.strip().startswith("- ")]
    if len(items) != 1:
        raise ValueError(f"expected one category, got {items}")
    return items[0]


def clean(path, review):
    text = path.read_text()
    m = re.match(r"^---\n(.*?\n)---\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    lines = m.group(1).splitlines(keepends=True)
    rel = str(path.relative_to(SRC).with_suffix(""))

    out = []
    category = "Uncategorized"
    for key, block in split_blocks(lines):
        if key in DROP_KEYS:
            continue
        if key in DROP_IF_EMPTY and block[0].split(":", 1)[1].strip() == DROP_IF_EMPTY[key]:
            continue
        if key == "category":
            category = category_of(block)
            continue
        if key == "layout":
            block = [block[0].replace("layouts/vertical-banner", "vertical-banner")]
        if key == "banner":
            block = [re.sub(r"(\.\./)+uploads/", "/uploads/", block[0])]
        out.extend(block)

    # Every reviewed post was Uncategorized in WordPress, so the review
    # wins, also on a re-run after the review changed.
    category = review.get(rel, category)
    if category != "Uncategorized":
        out.append(f"category: {category}\n")

    new ="---\n" + "".join(out) + "---\n" + text[m.end():]
    if new != text:
        path.write_text(new)
    return category


def main():
    review = read_review()
    counts = Counter()
    for path in sorted(SRC.glob("[0-9][0-9][0-9][0-9]/*/*.md")):
        try:
            counts[clean(path, review)] += 1
        except ValueError as e:
            sys.exit(f"{path}: {e}")
    (SRC / "collection.yaml").write_text(COLLECTION_YAML)
    print(f"{sum(counts.values())} posts, {len(review)} reviewed")
    for cat, n in counts.most_common():
        print(f"  {cat}: {n}")


if __name__ == "__main__":
    main()
