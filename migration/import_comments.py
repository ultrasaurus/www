#!/usr/bin/env python3
"""One-time import of the approved WordPress comments.

For each post (or page) with approved comments, writes
www-ultrasaurus/source/YYYY/MM/<slug>.responses.yaml next to it, an
altwebgen data file: the page's template gets `responses`, with

  comments:     real comments and tweets, oldest first; a reply is listed
                under `replies` of the comment it answers
  linked_from:  pingbacks (another blog linked to the post)

Unapproved comments (spam) and the author's own tweets are dropped.

Privacy: commenter emails and IPs are never written to source/. The emails
go to export/comment-emails.yaml (git-ignored, like the rest of export/),
keyed by the comment `id` kept in the published file. After writing, every
.responses.yaml is checked for any commenter email or IP, or anything that
looks like one; the run fails if it finds one.

Safe to re-run: the .responses.yaml files are rewritten each time.
"""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

from fix_old_paths import fix_old_paths

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
SOURCE = SITE / "source"
EXPORT = SITE / "export" / "all-theevolvingultrasaurus.WordPress.2021-04-13.xml"
EMAILS = SITE / "export" / "comment-emails.yaml"

NS = {"wp": "http://wordpress.org/export/1.2/"}
OWN_TWITTER = "ultrasaurus"
# by comment id: the comment on, and pingback from, the empty draft "the
# grim meathook kind of future", which isn't imported
DROPPED = {"1224", "1195"}

# tags kept in comment text; any other tag is dropped, keeping its text
KEEP_TAGS = {"a", "p", "br", "code", "pre", "blockquote", "strong", "em", "i", "b"}
BLOCK_START = re.compile(r"^\s*<(p|blockquote|pre|ul|ol)\b", re.I)

EMAIL_LIKE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
IP_LIKE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
# look private but aren't: localhost in a curl command, an ssh key file
NOT_PRIVATE = {"127.0.0.1", "ubuntu@ec2.pem"}


def redact_emails(text):
    """An email address someone typed into their comment."""
    return EMAIL_LIKE.sub(
        lambda m: m.group(0) if m.group(0) in NOT_PRIVATE else "[email removed]", text
    )


BARE_URL = re.compile(r"https?://[^\s<>\"]+")
# a pingback from this blog: link to the post's new URL instead
OWN_POST = re.compile(r"^https?://(?:www\.)?ultrasaurus\.com(?:/sarahblog)?/(\d{4}/\d\d/[^/?#]+)/?$")
OWN_TITLE_SUFFIX = " | the evolving ultrasaurus"
# posts renamed after a pingback went out: old path -> current path
RENAMED = {
    "2009/03/what-can-we-learn-from-the-piraha-language": "2009/03/learning-from-the-piraha-language",
}


def link(url):
    return f'<a href="{html.escape(url)}" rel="nofollow ugc">{html.escape(url)}</a>'


def linkify(text):
    """WordPress showed bare URLs in comments as links."""
    out, last = [], 0
    for m in BARE_URL.finditer(text):
        url = m.group(0).rstrip(".,;:!?)'")
        out.append(html.escape(text[last : m.start()], quote=False))
        out.append(link(url))
        last = m.start() + len(url)
    out.append(html.escape(text[last:], quote=False))
    return "".join(out)


class Sanitizer(HTMLParser):
    """Rebuilds HTML with only KEEP_TAGS; links get rel="nofollow ugc"."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.in_link = 0

    def handle_starttag(self, tag, attrs):
        if tag not in KEEP_TAGS:
            return
        if tag == "a":
            self.in_link += 1
            href = dict(attrs).get("href") or ""
            if not href.startswith(("http://", "https://")):
                self.out.append("<a>")  # closed by handle_endtag
                return
            self.out.append(f'<a href="{html.escape(href)}" rel="nofollow ugc">')
        elif tag == "br":
            self.out.append("<br>")
        else:
            self.out.append(f"<{tag}>")

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.out.append("<br>")

    def handle_endtag(self, tag):
        if tag in KEEP_TAGS and tag != "br":
            self.out.append(f"</{tag}>")
        if tag == "a":
            self.in_link = max(0, self.in_link - 1)

    def handle_data(self, data):
        self.out.append(html.escape(data, quote=False) if self.in_link else linkify(data))


def sanitize(text):
    s = Sanitizer()
    s.feed(text)
    s.close()
    # a link without a usable href is just its text
    return re.sub(r"<a>(.*?)</a>", r"\1", "".join(s.out), flags=re.S)


def paragraphs(text):
    """WordPress stores comments as plain text: blank lines between
    paragraphs, single newlines as line breaks. Turn that into HTML."""
    text = text.replace("\r\n", "\n").strip()
    pres = []

    def keep_pre(m):
        pres.append(m.group(0))
        return f"\x00{len(pres) - 1}\x00"

    text = re.sub(r"<pre.*?</pre>", keep_pre, text, flags=re.S | re.I)
    blocks = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        if not BLOCK_START.match(block) and not block.startswith("\x00"):
            block = "<p>" + block.replace("\n", "<br>\n") + "</p>"
        blocks.append(block)
    text = "\n".join(blocks)
    return re.sub(r"\x00(\d+)\x00", lambda m: pres[int(m.group(1))], text)


def iso_date(local, gmt, fallback_offset):
    """'2009-08-17 10:00:00' -> '2009-08-17T10:00:00-07:00'."""
    when = datetime.strptime(local, "%Y-%m-%d %H:%M:%S")
    offset = fallback_offset
    if gmt and not gmt.startswith("0000"):
        minutes = round((when - datetime.strptime(gmt, "%Y-%m-%d %H:%M:%S")).total_seconds() / 60)
        sign = "-" if minutes < 0 else "+"
        offset = f"{sign}{abs(minutes) // 60:02d}:{abs(minutes) % 60:02d}"
    return when.strftime("%Y-%m-%dT%H:%M:%S") + offset


def post_paths():
    """WordPress post id -> (source path, the post date's UTC offset)."""
    paths = {}
    for path in SOURCE.rglob("*.md"):
        head = path.read_text().split("\n---", 1)[0]
        m = re.search(r"^id: (\d+)$", head, re.M)
        if not m:
            continue
        d = re.search(r"^date: '.*?([+-]\d\d:\d\d)'$", head, re.M)
        paths[m.group(1)] = (path, d.group(1) if d else "")
    return paths


def yaml_str(s):
    # JSON strings are valid YAML and need no further quoting rules
    return json.dumps(s, ensure_ascii=False)


def yaml_block(s, indent):
    """A literal block for multi-line HTML, so it reads naturally."""
    pad = " " * indent
    lines = [line.rstrip() for line in s.split("\n")]
    if lines[0].startswith(" "):
        return yaml_str(s)
    return "|-\n" + "\n".join(pad + line if line else "" for line in lines)


def write_comment(out, c, indent):
    pad = " " * indent
    out.append(f"{pad}- id: {c['id']}")
    out.append(f"{pad}  author: {yaml_str(c['author'])}")
    if c["url"]:
        out.append(f"{pad}  url: {yaml_str(c['url'])}")
    out.append(f"{pad}  date: '{c['date']}'")
    if c.get("via"):
        out.append(f"{pad}  via: {c['via']}")
    out.append(f"{pad}  content: {yaml_block(c['content'], indent + 4)}")
    if c["replies"]:
        out.append(f"{pad}  replies:")
        for r in c["replies"]:
            write_comment(out, r, indent + 2)


def main():
    paths = post_paths()
    counts = Counter()
    secrets = set()  # every commenter email and IP in the export
    emails = []
    written = []
    for item in ET.parse(EXPORT).getroot().iter("item"):
        found = []
        for c in item.findall("wp:comment", NS):
            for field in ("comment_author_email", "comment_author_IP"):
                value = (c.findtext(f"wp:{field}", namespaces=NS) or "").strip()
                if value:
                    secrets.add(value.lower())
            if c.findtext("wp:comment_approved", namespaces=NS) != "1":
                counts["unapproved"] += 1
                continue
            if c.findtext("wp:comment_id", namespaces=NS) in DROPPED:
                counts["dropped by hand"] += 1
                continue
            found.append(c)
        if not found:
            continue
        post_id = item.findtext("wp:post_id", namespaces=NS)
        if post_id not in paths:
            counts["not imported (no such post in source/)"] += len(found)
            print(f"skipped: {len(found)} on {item.findtext('wp:post_name', namespaces=NS)!r} "
                  f"({item.findtext('wp:status', namespaces=NS)}), not in source/")
            continue
        path, post_offset = paths[post_id]

        comments, linked_from, by_id = [], [], {}
        for c in found:
            get = lambda f: (c.findtext(f"wp:{f}", namespaces=NS) or "").strip()
            kind = get("comment_type") or "comment"
            author = html.unescape(get("comment_author"))
            if kind.startswith("social-twitter") and author == OWN_TWITTER:
                counts["own tweets (dropped)"] += 1
                continue
            entry = {
                "id": int(get("comment_id")),
                "author": author,
                "url": get("comment_author_url"),
                "date": iso_date(get("comment_date"), get("comment_date_gmt"), post_offset),
                "parent": int(get("comment_parent") or 0),
                "replies": [],
            }
            if get("comment_author_email"):
                emails.append((entry["id"], author, get("comment_author_email")))
            if kind in ("pingback", "trackback"):
                counts["pingbacks"] += 1
                own = OWN_POST.match(entry["url"])
                own_path = own and RENAMED.get(own.group(1), own.group(1))
                if own and (SOURCE / f"{own_path}.md").exists():
                    counts["pingbacks from this blog (new URL)"] += 1
                    entry["url"] = f"/{own_path}/"
                    entry["author"] = entry["author"].removesuffix(OWN_TITLE_SUFFIX)
                linked_from.append(entry)
                continue
            if kind.startswith("social-twitter"):
                entry["via"] = "twitter"
                counts["tweets"] += 1
            else:
                counts["comments"] += 1
            # a trackback from this blog, kept as a comment, may use an old URL
            entry["url"] = fix_old_paths(entry["url"])
            entry["content"] = fix_old_paths(
                redact_emails(sanitize(paragraphs(get("comment_content"))))
            )
            by_id[entry["id"]] = entry
            comments.append(entry)

        # replies go under the comment they answer (one level: a reply to a
        # reply goes under the top comment)
        top = []
        for c in sorted(comments, key=lambda c: c["date"]):
            parent = by_id.get(c["parent"])
            while parent and parent["parent"] in by_id:
                parent = by_id[parent["parent"]]
            if parent and parent is not c:
                parent["replies"].append(c)
                counts["replies"] += 1
            else:
                top.append(c)

        out = []
        if top:
            out.append("comments:")
            for c in top:
                write_comment(out, c, 0)
        if linked_from:
            out.append("linked_from:")
            for p in sorted(linked_from, key=lambda p: p["date"]):
                out.append(f"- id: {p['id']}")
                out.append(f"  title: {yaml_str(p['author'])}")
                out.append(f"  url: {yaml_str(p['url'])}")
                out.append(f"  date: '{p['date']}'")
        if not out:
            continue
        target = path.with_name(path.name[: -len(".md")] + ".responses.yaml")
        target.write_text("\n".join(out) + "\n")
        written.append(target)

    EMAILS.write_text(
        "# commenter emails, by comment id; private, never publish\n"
        + "".join(f"{i}:\n  author: {yaml_str(a)}\n  email: {yaml_str(e)}\n" for i, a, e in emails)
    )

    for k, v in sorted(counts.items()):
        print(f"{v:6} {k}")
    print(f"{len(written):6} .responses.yaml files written")
    print(f"emails kept privately in {EMAILS.relative_to(HERE)}")

    problems = []
    for path in SOURCE.rglob("*.responses.yaml"):
        text = path.read_text()
        lower = text.lower()
        for s in secrets - NOT_PRIVATE:
            if s in lower:
                problems.append(f"{path.relative_to(SOURCE)}: a commenter email or IP")
        for pattern in (EMAIL_LIKE, IP_LIKE):
            for m in pattern.finditer(text):
                if m.group(0) not in NOT_PRIVATE:
                    problems.append(f"{path.relative_to(SOURCE)}: looks private: {m.group(0)!r}")
    if problems:
        print("\nPRIVACY CHECK FAILED:")
        print("\n".join(sorted(set(problems))))
        sys.exit(1)
    print("privacy check passed: no emails or IPs in source/")


if __name__ == "__main__":
    main()
