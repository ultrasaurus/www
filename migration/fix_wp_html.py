"""Fix WordPress HTML that the Eleventy importer left half-converted.

Rewrites post bodies in www-ultrasaurus/source/YYYY/MM/*.md in place;
safe to re-run (a second run changes nothing).

1. Markdown inside an HTML block (e.g. `<figure>[![alt](img)](link)...`)
   isn't processed, so readers see the raw Markdown. Put the element's
   tags on their own lines with blank lines around the content, so the
   Markdown inside renders. Post text that follows the element on the
   same line becomes its own paragraph. Old SlideShare Flash embeds
   (`<div id="__ss_...">`) become a plain "Slides: [title](url)" link.
2. Multi-line code squashed into one inline code span with `<br></br>`
   between lines becomes a fenced code block; `<br></br>` inside a fenced
   code block becomes a line break.
3. A stray `<pre ...>` / `</pre>` inside a fenced code block is removed.
4. A YouTube URL alone on a line (WordPress embedded these) becomes an
   embedded player, like the other posts' YouTube iframes.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent / "source"

FENCE = re.compile(r"^\s*(?:>\s?)*(```|~~~)")
# tags that start a CommonMark "type 6" HTML block, so Markdown inside
# them isn't processed
BLOCK_TAGS = "div|figure|figcaption|p|table|ul|ol|blockquote|section|center"
HTML_BLOCK_START = re.compile(rf"^ {{0,3}}</?({BLOCK_TAGS})\b", re.I)
ELEMENT_START = re.compile(rf"<({BLOCK_TAGS})\b", re.I)
TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>")
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "embed", "wbr"}
HAS_MARKDOWN = re.compile(r"\]\(|\*\*|^- ", re.M)
TRACKING_PIXEL = re.compile(r"!\[\]\(http://counters\.gigya\.com/[^)]*\)")
YOUTUBE_LINE = re.compile(
    r"^https?://(?:www\.)?(?:youtu\.be/|youtube\.com/watch\?v=)([\w-]+)\s*$"
)
YOUTUBE_IFRAME = (
    '<iframe loading="lazy" width="770" height="433" '
    'src="https://www.youtube.com/embed/{}?feature=oembed" '
    'frameborder="0" allowfullscreen></iframe>'
)


unclosed_embeds = 0  # SlideShare divs whose closing </div> is still to come


def element_end(text, start):
    """(index just past the tag that closes the element opening at `start`,
    True), or (len(text), False) if it isn't closed in `text`."""
    depth = 0
    for m in TAG.finditer(text, start):
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if name in VOID or selfclose:
            continue
        depth += -1 if closing else 1
        if depth == 0:
            return m.end(), True
    return len(text), False


def slideshare_link(element):
    """'Slides: [title](url)' for an old SlideShare embed, or None."""
    links = re.findall(r'\[([^\[\]]*)\]\((\S+?)(?:\s+"([^"]*)")?\)', element)
    for text, url, title in links:
        if not re.search(r"slideshare\.net/[^/?\s]+/[^/?\s]+", url):
            continue
        if text in ("", "View", "presentation", "presentations"):
            m = re.match(r"View '(.+)' on SlideShare$", title)
            text = m.group(1) if m else title
        return f"Slides: [{text}]({url.split('?')[0]})"
    return None


def fix_element(element, closed):
    """(new text, changed) for one HTML block element; an element that
    isn't `closed` continues past this run of lines."""
    if re.match(r'<div[^>]*id="__ss_', element):
        link = slideshare_link(element)
        if link:
            if closed:
                return link, True
            # the embed's own div closes later, and the post text in between
            # (after the boilerplate's last </div>) must be kept; the later
            # lone </div> goes too, or it would close the page's content div
            global unclosed_embeds
            unclosed_embeds += 1
            tail = element[element.rfind("</div>") + len("</div>") :].strip()
            return f"{link}\n\n{tail}" if tail else link, True
    open_tag = TAG.match(element)
    if not open_tag:
        return element, False
    close = re.search(r"</[a-zA-Z0-9]+>\s*$", element) if closed else None
    inner = element[open_tag.end() : close.start() if close else len(element)]
    if not HAS_MARKDOWN.search(inner):
        return element, False
    inner = inner.strip()
    inner = re.sub(r"\s*(<figcaption\b)", r"\n\n\1", inner)
    # "Awesome volunteers: - [Brian..." starts a list
    inner = re.sub(r":\s+- \[", ":\n\n- [", inner)
    text = f"{element[:open_tag.end()]}\n\n{inner}"
    if close:
        text += f"\n\n{close.group(0).strip()}"
    return text, True


def fix_html_block(text):
    """Fix the elements in an HTML block (a run of non-blank lines)."""
    pieces, pos, changed = [], 0, False
    after_element = False
    while pos < len(text):
        m = ELEMENT_START.search(text, pos)
        if m and not text[pos : m.start()].strip():
            end, closed = element_end(text, m.start())
            new, did = fix_element(text[m.start() : end], closed)
            changed |= did
            if pieces and not did and not after_element:
                pieces[-1] += text[pos:end]
            else:
                pieces.append(new)
            pos, after_element = end, True
            continue
        end = m.start() if m else len(text)
        run = text[pos:end]
        # text right after an element, on the same line, becomes its own
        # paragraph; closing tags and whitespace stay where they are
        if after_element and run.strip() and not run.lstrip().startswith("<"):
            pieces.append(run.strip())
            changed = True
        elif pieces:
            pieces[-1] += run
        else:
            pieces.append(run)
        pos, after_element = end, False
    return "\n\n".join(pieces) if changed else text


def fix_code_span(line):
    """Lines for a `<br></br>`-joined inline code span as a fenced block,
    or None."""
    m = re.match(
        r"^(?P<lead>\s*(?:>\s?)*)(?P<before>[^`]*?)(?P<ticks>`+)"
        r"(?P<code>.*<br></br>.*?)`*(?P=ticks)(?P<after>[^`]*)$",
        line,
    )
    if not m:
        return None
    lead, before, after = m["lead"], m["before"], m["after"]
    code = re.sub(r"</?(strong|b)>", "", m["code"])
    rows = [r.rstrip() for r in code.split("<br></br>")]
    while rows and not rows[0].strip():
        rows.pop(0)
    while rows and not rows[-1].strip():
        rows.pop()
    indent = lead
    marker = re.match(r"(\d+\.|[-*+])\s+", before)
    if marker:
        indent = lead + " " * len(marker.group(0))
    out = []
    if before.strip():
        out.append(lead + before.rstrip())
    out.append(indent + "```")
    out += [(indent + r) if r.strip() else indent.rstrip() for r in rows]
    out.append(indent + "```")
    if after.strip():
        out.append(lead + after.strip())
    return out


def split_code_line(line):
    """A code block line with WordPress `<br></br>`s, as separate lines.
    The line already ends in a newline, so one trailing `<br></br>` is
    dropped; bold tags and non-breaking spaces were WordPress formatting."""
    lead = re.match(r"^\s*(?:>\s?)*", line).group(0) if line.lstrip().startswith(">") else ""
    line = re.sub(r"</?(strong|b)>", "", line).replace("\xa0", " ")
    line = re.sub(r"<br></br>\s*$", "", line)
    first, *rest = line.split("<br></br>")
    return [first.rstrip()] + [(lead + r).rstrip() for r in rest]


def fix_body(body):
    lines = body.split("\n")
    out, group, in_fence, fence_start = [], [], False, False

    def flush():
        if not group:
            return
        start = next(
            (i for i, l in enumerate(group) if HTML_BLOCK_START.match(l)), None
        )
        if start is None:
            out.extend(group)
        else:
            out.extend(group[:start])
            out.extend(fix_html_block("\n".join(group[start:])).split("\n"))
        group.clear()

    for line in lines:
        if FENCE.match(line):
            flush()
            in_fence = not in_fence
            fence_start = in_fence
            out.append(line)
            continue
        if in_fence:
            if fence_start:
                fence_start = False
                pre = re.match(r"^(\s*)<pre\b[^>]*>", line)
                if pre:
                    line = pre.group(1) + line[pre.end() :]
                    if not line.strip():
                        continue
            line = re.sub(r"</pre>\s*$", "", line)
            if "<br></br>" in line:
                out.extend(split_code_line(line))
            else:
                out.append(line)
            continue
        global unclosed_embeds
        if unclosed_embeds and line.strip() == "</div>" and not group:
            unclosed_embeds -= 1
            continue
        line = TRACKING_PIXEL.sub("", line)
        if "<br></br>" in line and "`" in line:
            fenced = fix_code_span(line)
            if fenced:
                flush()
                out.extend(fenced)
                continue
        video = YOUTUBE_LINE.match(line)
        if video:
            line = YOUTUBE_IFRAME.format(video.group(1))
        if line.strip():
            group.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def main():
    changed = 0
    for path in sorted(SRC.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md")):
        text = path.read_text()
        m = re.match(r"---\n.*?\n---\n", text, re.S)
        head, body = (m.group(0), text[m.end() :]) if m else ("", text)
        new = head + fix_body(body)
        if new != text:
            path.write_text(new)
            changed += 1
            print(path.relative_to(SRC))
    print(f"{changed} posts changed")


if __name__ == "__main__":
    main()
