#!/usr/bin/env python3
"""Replaces images that are lost for good with a short note (step 8).

The old /images/ folder (outside WordPress) isn't in the export, the
backups, www-archive or the Wayback Machine. Each Markdown image of a file
there becomes

    (image lost — alt text)<!-- lost image: original URL -->

or "(image lost)" when it had no alt text. A link around the image is
dropped too when it pointed at a lost file (usually the full-size image);
a link elsewhere is kept around the note. A text link to a lost file
keeps its text, without the link:

    screen shots<!-- lost file: original URL -->

Rewrites published posts in www-ultrasaurus/source/ in place (drafts are
left alone). Safe to re-run: notes don't match again.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "source"

OLD_IMAGE = r"(?:https?://(?:www\.)?ultrasaurus\.com)?/images/[^\s)\"'>]+"
IMAGE = rf"!\[([^\]]*)\]\(\s*({OLD_IMAGE})(?:\s+\"[^\"]*\")?\s*\)"
# [ ![alt](image) ](target), the image linked to something
LINKED = re.compile(rf"\[\s*{IMAGE}\s*\]\(\s*([^\s)]+)(?:\s+\"[^\"]*\")?\s*\)", re.I)
ALONE = re.compile(IMAGE, re.I)
TEXT_LINK = re.compile(rf"(?<!!)\[([^\]]+)\]\(\s*({OLD_IMAGE})(?:\s+\"[^\"]*\")?\s*\)", re.I)


def is_lost(url):
    path = re.sub(r"^https?://(?:www\.)?ultrasaurus\.com", "", url, flags=re.I)
    return not (SOURCE / path.lstrip("/")).is_file()


def note(alt, url):
    alt = alt.strip()
    text = f"(image lost — {alt})" if alt else "(image lost)"
    return f"{text}<!-- lost image: {url} -->"


def fix(text, counts):
    def linked(m):
        alt, image, target = m.groups()
        if not is_lost(image):
            return m.group(0)
        counts["images"] += 1
        if is_lost(target) if re.match(OLD_IMAGE, target, re.I) else False:
            return note(alt, image)
        return f"[{note(alt, image)}]({target})"

    def alone(m):
        alt, image = m.groups()
        if not is_lost(image):
            return m.group(0)
        counts["images"] += 1
        return note(alt, image)

    def text_link(m):
        words, url = m.groups()
        if not is_lost(url):
            return m.group(0)
        counts["text links"] += 1
        return f"{words.strip()}<!-- lost file: {url} -->"

    return TEXT_LINK.sub(text_link, ALONE.sub(alone, LINKED.sub(linked, text)))


def main():
    from collections import Counter

    counts = Counter()
    changed = 0
    for path in sorted(SOURCE.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md")):
        text = path.read_text()
        if re.search(r"^status: draft$", text.split("\n---", 1)[0], re.M):
            continue
        new = fix(text, counts)
        if new != text:
            path.write_text(new)
            changed += 1
    print(f"{counts['images']} lost images and {counts['text links']} text links "
          f"replaced in {changed} posts")


if __name__ == "__main__":
    main()
