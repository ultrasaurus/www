#!/usr/bin/env python3
"""Maps old Movable Type URLs to current posts, using the Wayback Machine
(step 8).

The blog's first URLs were /sarahblog/archives/NNNNNN.html (Movable Type,
2003-2008). For each one that posts or comments still link to (with
--all, also every one the Wayback Machine saved, for the step 9
redirects):

* a Wayback capture of a redirect (WordPress sent the old URL to the new
  post) gives the post's path directly
* otherwise a capture of the old page gives its title and date, matched
  against the published posts' titles (the date breaks ties)

Writes movable-type.yaml next to this script: old path -> new path, with
how each was found, and the ones not found. Changes nothing in source/.
Wayback answers are cached in www-ultrasaurus/export/ (git-ignored), so a
re-run only asks about new URLs.

Usage: python3 map_movable_type.py [--all]
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from import_comments import RENAMED

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
SOURCE = SITE / "source"
CACHE = SITE / "export" / "wayback-movable-type.json"
OUT = HERE / "movable-type.yaml"

MT_URL = re.compile(r"/sarahblog/archives/(\d{6})\.html")
NEW_PATH = re.compile(r"/(?:sarahblog/)?(\d{4}/\d\d/[^/?#]+)/?")
# matched by hand: Movable Type id -> post (YYYY/MM/slug), with why
BY_HAND = {
    "000136": ("2004/04/different-kinds-of-ambition",
               "old title 'I am ambitous', same date (April 30, 2004)"),
    "000155": ("2004/09/words-bullet-points-semantic-capitalism",
               "old title had the typo 'sematic', same date (September 2, 2004)"),
    "000316": ("2006/09/hyperscope-release",
               "old title 'HyperScope release party tonight', same date"),
    "000418": ("2008/01/comet-a-new-term-for-an-old-technique",
               "old title 'a new term for an old technique' (WordPress-era page)"),
}
CDX = "https://web.archive.org/cdx/search/cdx?url=ultrasaurus.com/sarahblog/archives/{}.html&fl=timestamp,statuscode&output=json"
CDX_ALL = "https://web.archive.org/cdx/search/cdx?url=ultrasaurus.com/sarahblog/archives/&matchType=prefix&fl=original&collapse=urlkey&output=json"
RAW = "https://web.archive.org/web/{}id_/http://www.ultrasaurus.com/sarahblog/archives/{}.html"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def fetch(url, timeout=60):
    """(status, location header, body) with a few retries."""
    for attempt in range(4):
        time.sleep(1 + attempt * 3)
        try:
            with OPENER.open(url, timeout=timeout) as r:
                return r.status, r.headers.get("location"), r.read()
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308, 404):
                return e.code, e.headers.get("location"), b""
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            pass
    raise RuntimeError(f"Wayback didn't answer: {url}")


def lookup(mt_id):
    """What the Wayback Machine knows about one old URL."""
    status, _, body = fetch(CDX.format(mt_id))
    rows = json.loads(body or b"[]")[1:] if status == 200 else []
    redirects = [ts for ts, code in rows if code in ("301", "302")]
    pages = [ts for ts, code in rows if code == "200"]
    # from 2015 the server sent old URLs to a broken address, so only a
    # redirect to a post counts; try a few, oldest first
    bad = None
    for ts in redirects[:4]:
        _, location, _ = fetch(RAW.format(ts, mt_id))
        target = re.sub(r"^https?://web\.archive\.org/web/\d+(?:id_)?/", "", location or "")
        if NEW_PATH.search(target):
            return {"redirect": target}
        bad = target
    if pages:
        _, _, body = fetch(RAW.format(pages[0], mt_id))
        page = body.decode("utf-8", errors="replace")
        if "�" in page:
            page = body.decode("windows-1252", errors="replace")
        title = re.search(r'<h3 class="title">(.*?)</h3>', page, re.S) or re.search(
            r"<title>[^:]*:\s*(.*?)</title>", page, re.S)
        date = re.search(r'<h2 class="date">(.*?)</h2>', page, re.S)
        return {"title": html.unescape(title.group(1)).strip() if title else None,
                "date": date.group(1).strip() if date else None}
    return {"bad_redirect": bad} if bad else {}


def normalize(title):
    title = html.unescape(title or "").lower()
    title = title.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9]+", " ", title).strip()


def published_posts():
    """path (YYYY/MM/slug) -> (normalized title, date YYYY-MM-DD)."""
    posts = {}
    for path in SOURCE.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md"):
        head = path.read_text().split("\n---", 1)[0]
        if re.search(r"^status: draft$", head, re.M):
            continue
        title = re.search(r"^title: (.*)$", head, re.M)
        title = title.group(1).strip() if title else ""
        if len(title) >= 2 and title[0] == title[-1] == "'":
            title = title[1:-1].replace("''", "'")
        date = re.search(r"^date: '?(\d{4}-\d\d-\d\d)", head, re.M)
        posts[path.relative_to(SOURCE).with_suffix("").as_posix()] = (
            normalize(title), date.group(1) if date else "")
    return posts


def linked_ids():
    """Movable Type ids that posts or comments link to."""
    ids = set()
    for path in list(SOURCE.rglob("*.md")) + list(SOURCE.rglob("*.responses.yaml")):
        ids.update(MT_URL.findall(path.read_text()))
    return sorted(ids)


def wayback_ids():
    """Movable Type ids the Wayback Machine has any capture of."""
    _, _, body = fetch(CDX_ALL, timeout=240)
    return sorted({m.group(1) for (url,) in json.loads(body)[1:]
                   if (m := MT_URL.search(url))})


def iso_date(text):
    """'September 02, 2003' -> '2003-09-02'."""
    try:
        return time.strftime("%Y-%m-%d", time.strptime(text, "%B %d, %Y"))
    except (TypeError, ValueError):
        return ""


def match(info, posts):
    """(new path or None, how, note)."""
    if "redirect" in info:
        m = NEW_PATH.search(info["redirect"])
        if m:
            path = RENAMED.get(m.group(1), m.group(1))
            if path in posts:
                return f"/{path}/", "redirect", ""
        return None, "redirect", f"redirect to {info['redirect']}, no such post"
    if info.get("title"):
        wanted = normalize(info["title"])
        found = [p for p, (t, _) in posts.items() if t == wanted]
        date = iso_date(info.get("date"))
        if len(found) > 1 and date:
            found = [p for p in found if posts[p][1] == date] or found
        if len(found) == 1:
            return f"/{found[0]}/", "title", info["title"]
        note = f"{len(found)} posts titled" if found else "no post titled"
        return None, "title", f"{note} {info['title']!r} ({info.get('date')})"
    if info.get("bad_redirect"):
        return None, "none", "only redirects to nowhere in the Wayback Machine"
    return None, "none", "not in the Wayback Machine"


def main():
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    # from a first version that kept the first redirect, wherever it went
    cache = {k: v for k, v in cache.items()
             if "redirect" not in v or NEW_PATH.search(v["redirect"])}
    ids = linked_ids()
    if "--all" in sys.argv[1:]:
        ids = sorted(set(ids) | set(wayback_ids()))
    for i, mt_id in enumerate(ids, 1):
        if mt_id not in cache:
            print(f"{i}/{len(ids)} {mt_id}", flush=True)
            cache[mt_id] = lookup(mt_id)
            CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True))

    posts = published_posts()
    found, missing = [], []
    for mt_id in ids:
        if mt_id in BY_HAND:
            path, note = BY_HAND[mt_id]
            path, how = (f"/{path}/", "by hand") if path in posts else (None, "by hand")
        else:
            path, how, note = match(cache[mt_id], posts)
        old = f"/sarahblog/archives/{mt_id}.html"
        if path:
            found.append(f"{old}: {path}  # {how}" + (f": {note}" if note else ""))
        else:
            missing.append(f"# {old}: {note}")
    OUT.write_text(
        "# Movable Type URL -> current post, from the Wayback Machine\n"
        "# (map_movable_type.py); `redirect` = WordPress's own redirect,\n"
        "# `title` = matched by the old page's title\n"
        + "\n".join(found) + "\n"
        + ("\n# not found:\n" + "\n".join(missing) + "\n" if missing else ""))
    print(f"{len(found)} of {len(ids)} mapped; written to {OUT}")


if __name__ == "__main__":
    main()
