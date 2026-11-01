#!/usr/bin/env python3
"""Internal link check for the built ultrasaurus.com site (step 8).

Builds www-ultrasaurus with altwebgen into a temporary folder, then checks
every link and image on every page that points at this site: relative
URLs, root-relative URLs (/about/), and absolute ones
(https://ultrasaurus.com/...). Links to other sites are not checked.

Read-only: changes nothing in source/. Writes link-report.md next to
this script, grouped by kind of problem, each with the pages that have it.

Usage: python3 check_links.py
"""
import re
import subprocess
import sys
import tempfile
import urllib.parse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
SOURCE = SITE / "source"
ALTWEBGEN = SITE.parents[2] / "target" / "release" / "altwebgen"
REPORT = HERE / "link-report.md"

OWN_HOST = re.compile(r"^https?://(?:www\.)?ultrasaurus\.com(?=/|$)", re.I)
MOVABLE_TYPE = re.compile(r"^/sarahblog/archives/\d+\.html$")
OLD_WORDPRESS = re.compile(r"^/sarahblog/(\d{4}/\d\d/[^/]+)/?$")
OLD_UPLOADS = re.compile(r"^/wp-content(/uploads/.*)$")
# a link to another site written without http://, e.g. [x](www.example.com)
NO_SCHEME = re.compile(r"^(?:www\.)?[\w-]+(?:\.[\w-]+)*\.(?:com|org|net|edu|gov|io|rs|co|us|uk)(?:/|$)", re.I)
# (tag, attribute) pairs that point at something
LINK_ATTRS = {("a", "href"), ("img", "src"), ("link", "href"), ("script", "src"),
              ("iframe", "src"), ("source", "src"), ("video", "src"),
              ("audio", "src"), ("embed", "src")}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []  # (tag, url)

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and (tag, name) in LINK_ATTRS:
                self.found.append((tag, value.strip()))
            if value and name == "srcset":
                for part in value.split(","):
                    if part.strip():
                        self.found.append((tag, part.split()[0]))


def page_url(out, path):
    """The URL a built file is served at: a/b/index.html -> /a/b/."""
    rel = "/" + path.relative_to(out).as_posix()
    return rel[: -len("index.html")] if rel.endswith("/index.html") else rel


def internal_path(url, base):
    """The site path a link points at, or None for another site.
    A link to another site written without http:// is returned as is,
    without a leading /, to be reported."""
    if NO_SCHEME.match(url):
        return url
    if OWN_HOST.match(url):
        url = OWN_HOST.sub("", url) or "/"
    elif re.match(r"^[a-z][a-z0-9+.-]*:|^//|^#", url, re.I):
        return None  # another site, mailto:, data:, javascript:, #anchor
    path = urllib.parse.urlsplit(urllib.parse.urljoin(base, url)).path
    return urllib.parse.unquote(path)


def draft_paths():
    """Site paths of drafts (/YYYY/MM/slug/), which `build` leaves out."""
    paths = set()
    for path in SOURCE.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        if re.search(r"^status: draft$", path.read_text().split("\n---", 1)[0], re.M):
            paths.add("/" + path.relative_to(SOURCE).with_suffix("").as_posix() + "/")
    return paths


def classify(out, path, drafts):
    """None if the link works, otherwise the kind of problem."""
    if not path.startswith("/"):
        return "link to another site without http://"
    target = out / path.lstrip("/")
    if path.endswith("/"):
        if (target / "index.html").is_file():
            return None
    elif target.is_file():
        return None
    elif (target / "index.html").is_file():
        return "works, but redirects: add a trailing /"
    if MOVABLE_TYPE.match(path):
        return "old Movable Type URL (/sarahblog/archives/NNNNNN.html)"
    m = OLD_WORDPRESS.match(path)
    if m:
        if (out / m.group(1) / "index.html").is_file():
            return "old /sarahblog/ URL, the post exists: drop /sarahblog"
        return "old /sarahblog/ URL, no post at that path"
    if path.rstrip("/") + "/" in drafts:
        return "links to a draft (not published)"
    m = OLD_UPLOADS.match(path)
    if m and (out / m.group(1).lstrip("/")).is_file():
        return "old /wp-content/uploads/ path, the file is in /uploads/"
    if m or path.startswith("/uploads/"):
        return "missing upload (image or file)"
    if path.startswith("/images/"):
        return "missing old image (/images/, not in www-archive)"
    return "missing page or file"


def main():
    if not ALTWEBGEN.is_file():
        sys.exit(f"build altwebgen first: {ALTWEBGEN} not found")
    drafts = draft_paths()
    problems = defaultdict(lambda: defaultdict(set))  # kind -> target -> pages
    checked = 0
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "site"
        subprocess.run([ALTWEBGEN, "-o", out, "build"], cwd=SITE, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for html in sorted(out.rglob("*.html")):
            base = page_url(out, html)
            parser = Links()
            parser.feed(html.read_text(errors="replace"))
            for _tag, url in parser.found:
                path = internal_path(url, base)
                if path is None:
                    continue
                checked += 1
                kind = classify(out, path, drafts)
                if kind:
                    problems[kind][url].add(base)

    lines = ["# Internal link check", "",
             f"Checked {checked} links to this site. Problems by kind:", ""]
    for kind, targets in sorted(problems.items(), key=lambda kv: -len(kv[1])):
        pages = set().union(*targets.values())
        lines.append(f"* {kind}: {len(targets)} targets on {len(pages)} pages")
    for kind, targets in sorted(problems.items(), key=lambda kv: -len(kv[1])):
        lines += ["", f"## {kind}", ""]
        for url, pages in sorted(targets.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            lines.append(f"* `{url}`")
            for page in sorted(pages):
                lines.append(f"  * {page}")
    REPORT.write_text("\n".join(lines) + "\n")
    print("\n".join(lines[: 4 + len(problems)]))
    print(f"\nfull list: {REPORT}")


if __name__ == "__main__":
    main()
