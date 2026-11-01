# Plan: migrate ultrasaurus.com blog to altwebgen

Goal: all posts in markdown, built by altwebgen, with a working archive page
and working prev/next links. No more migrating every decade.

## Pick up here (as of 2026-10-31)

* **Next:** step 8
  * for step 8: 2 pingbacks point at the Movable Type URL
    `/sarahblog/archives/000548.html` (on `2008/12/getting-started-with-rails-2-day-1`
    and `2008/12/rails-2-day-3-behavior-driven-development`)
  * `import_comments.py` has `RENAMED` for posts renamed after a pingback
    went out (the Pirahã post: `what-can-we-learn-from-the-piraha-language`
    → `learning-from-the-piraha-language`)
* **State:**
  * altwebgen: `main`, ahead of `origin/main` (through `dev --drafts`
    and the sitemap), not pushed, not released
  * life-and-power: branch `alt-0.5`, committed, waiting on the release
  * www-ultrasaurus: branch `altwebgen`, steps 3–7 and the Pirahã
    pingback fix committed (no upstream branch; not pushed); "Speaking"
    removed from the top bar
    * pages outside the collection moved to folders so their URLs match
      the live site with no redirect: `about/`, `archives/`, `contact/`,
      `speaking/`, `ultrasaurus/` (each `index.md`; About's comments
      file moved with it); their old WordPress `date:` lines removed
      (also on `category/code/`), so they have no sitemap lastmod;
      internal links end in `/`
    * `job-opening-serverless-events-google` deleted (not on the live site)
* **Step 7 done:** `import_drafts.py` moved 274 drafts from
  `zz_old/` to `source/YYYY/MM/<slug>.md` with `status: draft`, then
  `zz_old/` was removed (`git rm`)
  * skipped the 5 empty drafts; kept "speak truth amidst fear and
    confusion" (empty, for its title); skipped 3 image attachments
  * slug from WordPress if it had one (28), else from the title;
    untitled drafts are `draft-<id>`
  * categories: 190 Uncategorized, 82 general, 2 code ("gogaruco" →
    Uncategorized)
  * `fix_wp_html.py` fixed 6 drafts; `import_comments.py` drops comment
    1224 and pingback 1195 (the empty "grim meathook" draft)
  * drafts were already public on GitHub (`zz_old/` on `main` since
    2021); the repo is public, so drafts are never private
  * review: `altwebgen dev --drafts` (or the `ultrasaurus-drafts` entry in
    altwebgen's `.claude/launch.json`); `/drafts/` lists only drafts;
    drafts show a "Draft" label and join category lists and prev/next
  * `build` never includes drafts or `/drafts/`
* **Step 6 done:** `import_comments.py`
  (re-runnable) wrote 299 `source/YYYY/MM/<slug>.responses.yaml` data
  files (template variable `responses`, keys `comments`, `linked_from`):
  745 comments, 5 tweets by others (your 50 dropped), 4 replies nested
  under their comment, 143 pingbacks as `linked_from` (32 from this blog
  point at the new post URL); one comment on a draft is left for step 7
  * emails: kept only in `export/comment-emails.yaml` (git-ignored), by
    comment `id`; IPs dropped; 2 emails typed into comment text are
    "[email removed]"; the script fails if any email or IP reaches source/
  * comment text: WordPress paragraphs → HTML, only safe tags kept, bare
    URLs linked, links `rel="nofollow ugc"`
  * templates: `_comments.hbs`/`_comment.hbs` after the post nav (post,
    vertical-banner and default layouts); `id="comment-123"` keeps old
    `#comment-123` links working
  * altwebgen: data files, `<slug>.<name>.yaml` next to a page becomes
    its variable `<name>` and isn't published (`doc/frontmatter.md`)
* **Archive links:** "All · Code · General" under the title of
  `/archives`, `/category/code/` and `/category/general/` (partial
  `_archive-nav.hbs`, page picks its link with `archive_nav:`);
  Uncategorized posts appear only under All
  * the Code page is at `/category/code/` again, like the old live site
  * top bar unchanged; adding Code there is undecided (no posts since 2020)
* **Step 5 done:** compared all 677 posts with the
  `www-archive` copy (script: `compare_posts.py` in the session
  scratchpad, not kept); `fix_wp_html.py` (re-runnable) fixed 53 posts:
  Markdown inside HTML blocks (figures, Skitch images, lists), old
  SlideShare Flash embeds → "Slides: [title](url)" links, `<br></br>`
  code → fenced code blocks, stray `<pre>` in code, bare YouTube URLs →
  iframes; one hand fix in `2008/12/getting-started-with-rails-2-day-1`
  * 2008 Rails tutorial days 2–4: filename labels and the flattened
    day 2 listings rebuilt by hand from the archived HTML (indentation and
    bold highlights kept, as `<pre><code>` blocks)
* **Home page:** graphic (Judah Nero) on the right; "Recent Posts"
  (5 general) and "Coding Notebook" (5 code) on the left, via named
  lists (`list:` sequence with `as:` and `limit:`, new in altwebgen)
  * an excerpt after each title: list items have `excerpt` (new in
    altwebgen): `excerpt` frontmatter, or the first sentence of the first
    real paragraph, up to 200 characters
* **Step 4 done:** `src/` → `source/`, `uploads/` → `source/uploads/`,
  Handlebars templates in `template/`, plain CSS in
  `template/css/styles.css` ("Garden" palette, teal links, centred 48rem
  column), Foundation CSS saved locally, Eleventy
  `_includes`/`src.json`/`scss` removed
  * build: `../../../target/release/altwebgen build` from
    `www-ultrasaurus/` (or the `ultrasaurus` entry in altwebgen's
    `.claude/launch.json` for dev mode on port 3456)
  * post nav reads "← Older: title" / "Newer: title →"
  * titles use `{{{ }}}` because WordPress titles contain entities
    like `&#8230;`
* **Step 3 done:** `import_frontmatter.py` (re-runnable) cleaned the
  frontmatter in place in `www-ultrasaurus/src/`
  * now: 104 code, 272 general, 301 Uncategorized (no `category:` key)
  * `category-review.md`: everything above the `## Unreviewed` heading
    is reviewed (checked = code, unchecked = general); the rest stay
    Uncategorized — move the heading down and re-run after reviewing more
* **Category review is optional, not a blocker** — publish without it
  * 55 posts reviewed so far (32 code); stop anytime
  * full review comes later, post by post, once posts have audio (TTS)
  * don't regenerate `category-review.md` (it would erase the checks)
* **Waiting on Sarah:** confirm how readers want to be credited, then
  release altwebgen v0.5

## Where things are today

* **Live site** `ultrasaurus.com` is served by `ultrasaurus/www-archive`
  (GitHub Pages, `main`), a frozen wget copy of the old WordPress site
  * prev/next work there; `/category/code/` 404s (works in the new
    site); comments hidden via CSS
* **Eleventy work-in-progress** `ultrasaurus/www` (local: `www-ultrasaurus/`)
  is published at `newblog.ultrasaurus.com` (GitHub Pages, `gh-pages`)
  * the local remote still uses the old name `www.ultrasaurus.com.git`
    (GitHub redirects to `ultrasaurus/www`)
* **WordPress export** (2021-04-13) is in `www-ultrasaurus/export/`
  * local only: `export/` is in `.gitignore`, so it is not on GitHub —
    back it up
  * contains commenter emails and IPs — never publish those
* Both local repos were in sync with GitHub as of 2026-10-29

## Constraint: never break the other altwebgen site

* `ext/life-and-power-discernment/website` must keep building and look the
  same after every altwebgen change (OK to change its site code, never OK
  to leave it broken)
* Features it relies on:
  * `series.yaml` prev/next/toc (`reference/1994-neym-booklet`)
  * refs (`{{> ref ...}}` partials from `ref/`, with frontmatter, `reader`)
  * `person`, `split` and `date_format` helpers
  * layouts chosen by `layout:` frontmatter; `.md.hbs` and `.html.hbs`
* Its CI pins altwebgen `VERSION=v0.4.4` (`.github/workflows`), so
  production only changes when that pin is bumped
  * branch `alt-0.5` has the site changes that need the next release
    (event date, `date_format`, reader styling)
* Check before each altwebgen commit:
  * build it with the previous altwebgen to a baseline folder
  * build it with the changed altwebgen, `diff -r` the two outputs
  * any difference must be intended (and fixed in the site if needed)
  * then `cargo test` and the `samples/` sites, as usual

## Decisions

* Categories: **code**, **general**, and **Uncategorized** (the default)
  * each post has exactly one category
  * the importer turns WordPress lists (`category: [general]`) into one
    value; the default comes from the collection's `defaults`
  * today: 355 Uncategorized, 250 general, 72 code
  * 338 of the Uncategorized posts are from before categories were used
    (2003-03 to 2008-12, the Movable Type era; first `general` post is
    2008-12-14); some of these are probably code posts
  * 17 later Uncategorized posts (2013–2020), probably just never tagged
* prev/next stays **within a post's category**, ordered by date
* Front page does not need a list of posts
* Archive: **one page**, with a heading for each month (e.g. "March 2003"),
  newest first
  * no per-month archive pages; old `/YYYY/MM/` URLs will 404
* Keep the old comments (approved ones only), rendered statically
* Bring the drafts over too (`status: draft`): kept in the repo, not built
* Skip RSS for now; add it back if someone asks
* Layout stays as is, but darken the blue for readability
  (check contrast against the background)
* Keep old post URLs working: posts are written to
  `/YYYY/MM/slug/index.html` (`pretty_urls`)
* Full rebuild every time; no incremental build needed (see Speed)

## Speed (measured 2026-10-29, 677 posts)

* Repeat build (output updated in place): about 0.15s; first build into an
  empty output folder: about 0.29s
* Dev mode: a saved edit is in the HTML after about 0.33s
* 4x the posts (2,708): about 0.56s repeat build
* Deploy speed depends on the host: pick one that only uploads changed
  files (e.g. Cloudflare), since GitHub Pages redeploys everything

## What to reuse from the Eleventy repo (`www-ultrasaurus/`)

* **As is**
  * `src/YYYY/MM/*.md` — 677 published posts with frontmatter (title,
    date, category, status, `exported_permalink`); dates already parse
  * `uploads/` — images, copied through
  * `src/about.md`, `contact.md`, `speaking.md`, `ultrasaurus.md`
  * `scss/styles.scss` — compile once to CSS (or keep a sass step)
  * `CNAME`
* **Port Liquid → Handlebars**
  * `_includes/layouts/base.liquid`, `layouts/post.liquid`
  * `_includes/layouts/vertical-banner.liquid` — a post layout with a
    banner image (`banner`, `banner-alt-text`), used by
    `2016/07/signals-of-happiness`; port it as `vertical-banner.hbs` and
    have the importer change `layout: layouts/vertical-banner` to
    `layout: vertical-banner`
  * `_includes/_post/header.liquid`, `date.liquid`, `nav.liquid`
  * `archives.md` and `category-code.md` become listing pages
    (`list: {collection: posts, order: newest}`, plus a `category` filter);
    `category-code.md` is now `category/code/index.md`
* **Leave behind**
  * `src/src.json` — replaced by the collection's `defaults`
  * `.eleventy.js`, `liquid.js`, `package.json`, `node_modules`
  * `_categories.liquid` (commented out), `_post_highlight.liquid` (front page)

## altwebgen features

Done (merged into `main`, not yet released; see `doc/frontmatter.md`, `doc/collections.md`):

* Typed frontmatter — any YAML value; page wins over `_site.yaml`
* Dates with precision, `date_format` helper; names (`Last, First`),
  `people` helper
* Collections (`collection.yaml`): members by glob, sorted by date,
  prev/next within a group (category), `defaults`, drafts not built,
  `pretty_urls`
* Listing pages (`list:`) with `filter` and `order`, plus `posts_by_month`
  * `list:` may be a sequence of named lists (`as:`, `limit:`)
  * list items have an `excerpt` (frontmatter, or the first sentence)
* Speed: posts read once, output updated in place (unchanged files not
  rewritten, stale files removed), 200ms dev-mode wait
* Dev mode no longer drops changes saved during a rebuild
* Config files (`collection.yaml`, `series.yaml`, `_site.yaml`) not
  published
* Data files: `<slug>.<name>.yaml` next to a page becomes its template
  variable `<name>`, not published
* `dev --drafts` (uncommitted): builds drafts with `draft: true`; any page
  with a `status` other than `publish` is a draft, collection member or not
* Sitemap (uncommitted): `sitemap.xml` when `_site.yaml` has `site_url`;
  `sitemap: false` and `updated` frontmatter (`doc/frontmatter.md`)

Still to do:

* **Release v0.5** — after reader names are confirmed; then bump
  life-and-power's CI pin and merge its `alt-0.5` branch

## Importer (one-time script, not in altwebgen)

* Frontmatter clean-up for the 677 posts:
  * `category` list → one value (and decide on general vs Uncategorized)
  * `layout: layouts/vertical-banner` → `vertical-banner`
  * drop Eleventy/WordPress-only keys if they get in the way
    (`tag`, `post_format`, `type`, `id`, `excerpt`) — or keep them, they're
    harmless
* Drafts: the ~278 drafts from the WordPress export, with `status: draft`
* Comments: approved only (944 of 16,838; the rest are unapproved spam)
  * includes pingbacks, trackbacks and Twitter mentions — decide whether
    to keep those or only real comments
  * 6 threaded replies (`comment_parent`)
  * writes `<slug>.responses.yaml` next to each post: author name, author
    URL, date, content, parent
  * strips emails and IPs; review the output before committing

## Steps

1. Done: Typed frontmatter + collection pass, tested against a small
   sample blog (`samples/blog`)
2. Done: Category prev/next, archive-by-month, category pages
3. Done: Importer: frontmatter clean-up (no comments yet)
4. Done: Port templates to Handlebars; darken the blue; compile the CSS
5. Done: Render 20–30 real posts from different years and compare with
   the live site — WordPress HTML in posts (captions, embeds, image
   classes) may render differently (all 677 compared)
6. Done: Comments: importer + altwebgen support + rendering
7. Done: Drafts import (review with `dev --drafts`, `/drafts/`)
8. Full build, link check
   * Done (uncommitted): Knol links in
     `2008/12/the-decline-of-women-in-cs-from-1940-1982` → Wayback, and
     its chart image fetched to `source/uploads/2008/12/`; RailsBridge
     link in `2009/05/fork-is-the-new-friend` → the bridgefoundry group;
     Grip video embedded again in `2007/09/analog-video-effects`; 12
     links missing `http://` fixed, the `…frameworks` typo, the stray
     `%22` on an upload, and 5 `/emailme.php` links → `/contact/`.
     Done (uncommitted): the last 10 missing old pages, from Wayback:
     Grace Hopper 2004 PDF → `source/speaking/`; Processing snapshots
     and `.pde` sources → `source/uploads/2003/10/` (applets can't run);
     Wayback links for indyjr map, findjerry.zip, gears demo,
     blogbox_history; guestmap → plain text + comment.
     `check_links.py` now finds 0 broken links to this site.
     Done (uncommitted): compared 196 Movable Type–era posts with the
     Wayback copies of the monthly archives (2003-03 to 2006-10); 9 posts
     had been cut off at a Windows-1252 apostrophe in the WordPress
     import. Restored the missing text in all 9 (incl.
     `2003/03/behavioral-demographics` with `msn_ducks.gif`) and
     `memex.jpg` in `2003/12/historical-perspective-on-links-and-trails`.
     Not compared: "Laszlo Mail" and "HyperScope release" (listed under
     another month), and posts from 2005-02 and 2006-08 (no capture).
     Done (uncommitted): fetched 25 old `/images/` files from Wayback
     into `source/uploads/YYYY/MM/` (the post's month) and put back 22
     images + 4 links in 18 posts; the Earthlink "screen shots" page
     (`uploads/2003/11/psp_images.html`) with its 5 screenshots; 4 extra
     Laszlo Mail screenshots saved in `uploads/2005/11/` (no post uses
     them yet). `2013-03-leapmotion-npr.png` has no good capture.
     50 lost notes left (no Wayback copy).
     Done (uncommitted): redirect list. `make_redirects.py` (re-runnable)
     writes `source/_redirects` (altwebgen copies it as-is): 647
     one-to-one (312 Movable Type posts, 27 old WordPress slugs — the 81
     `_wp_old_slug` entries have repeats — 296 month/year archive pages
     → `/archives/`, 10 `BY_HAND`, uncategorized, author) + 7 patterns
     (`/wp-content/uploads/*`, `/sarahblog/…`, `/code/*`, `/page/*`).
     Feeds and tag pages stay 404. Every target is checked to exist;
     every old upload is in `source/uploads/` (other than WordPress temp
     files). Checked on `www-ultrasaurus.pages.dev`: Cloudflare matches
     `/old` and `/old/` separately, so old pages (not month archives)
     also get a no-slash line (679 one-to-one in all). Posts keep the
     trailing slash; Cloudflare itself sends `/slug` → `/slug/` (308).
     `source/404.md` → `/404.html`: without it Cloudflare serves the
     home page for every unknown URL.
   * `check_links.py` (re-runnable, read-only) builds the site and writes
     `link-report.md`: every broken link to this site, by kind. First run
     (2026-10-31): 7,037 links checked; 81 old `/images/` files (not in
     `www-archive`), 48 `/sarahblog/YYYY/MM/slug` links to posts that
     exist, 39 Movable Type URLs, 34 `/wp-content/uploads/` links whose
     file is in `/uploads/`, 31 other missing pages (old `/code/2008/`
     notebook, `/sarahblog/notes/`, `/indyjr/`…), 12 links to other sites
     missing `http://`, 1 typo (`ruby-unit-test-framework` → `…frameworks`)
   * Done (uncommitted): `fix_old_paths.py` (re-runnable) rewrote 35
     `/wp-content/uploads/` links to `/uploads/` and 55 `/sarahblog/`
     links to the post's path, in 51 posts; `import_comments.py` uses it
     too (3 comment files changed); only when the target exists
   * Done (uncommitted): `fix_lost_images.py` replaced 66 lost `/images/`
     images in 39 posts with "(image lost — alt)" plus an HTML comment
     with the original URL (no copy in Wayback, backups or www-archive);
     10 text links to lost files keep their text with a "lost file"
     comment; hand fixes in `2008/02/edward-tufte-critiques-the-iphone`
     and `2006/07/the-coding-offsite` (an empty link)
   * Done: `source/writing/future-is-not-the-past/`, from the
     Wayback Machine: the paper (only 200 capture is June 2004; converted
     from Windows-1252 to UTF-8), the PDF and the 15 images it uses
   * `map_movable_type.py` (re-runnable, read-only; Wayback answers
     cached in `export/wayback-movable-type.json`) wrote
     `movable-type.yaml`: all 42 linked Movable Type URLs → posts (9 by
     WordPress's redirect, 32 by the old page's title with the same date,
     1 by hand: 000136 "I am ambitous" → `different-kinds-of-ambition`).
     Done (uncommitted): 18 links to other old pages rewritten by
     `BY_HAND` in `fix_old_paths.py` (Coding Notebook, old about pages,
     archive pages, backup → Wayback), 6 broken links fixed by hand
     (`cgi-bin/mt/www.…`, Twitter handles, information aesthetics, empty
     Laszlo Mail link). Left: 11 targets to try in Wayback, else plain
     text (Processing sketches, blogbox_history, indyjr, findjerry.zip,
     2004-grace-hopper-talk.pdf, emailme.php → /contact/?, gears/install)
     Decided for the 29 "missing page" links: `/sarahblog/archives/2003_03.html`
     → `/2003/03/are-blogs-the-vanity-press-of-the-internet/`;
     `/backup-2009-01-03/` ("old design" in
     `2009/01/renovations-may-take-a-while`) →
     `http://web.archive.org/web/20030425081135/http://www.ultrasaurus.com/sarahblog/`
     Done (uncommitted): `fix_old_paths.py` rewrote 59 Movable Type links
     in 38 posts, and `import_comments.py` 2 trackback URLs; the same
     list feeds the step 9 redirect list.
     `map_movable_type.py --all` also maps every Movable Type post URL
     the Wayback Machine saved: 312 of 318 → posts (29 by redirect, 279
     by title, 4 by hand); 6 have no capture (→ `/archives/` by pattern)
   * build a redirect list for step 9: `/sarahblog/...` paths, the 81
     `_wp_old_slug` renames in the WordPress export (could replace
     `RENAMED` in `import_comments.py`), and the Movable Type URLs
9. Host: Cloudflare Pages (uploads only changed files; real redirects)
   * redirects: a `_redirects` file in the output, from step 8's list
     (old URLs already 404 on the live site, so this wins back links)
   * Done: sitemap. altwebgen writes `sitemap.xml` because
     `source/_site.yaml` has `site_url: https://ultrasaurus.com` (685
     URLs, lastmod from `date` for posts, no drafts); every URL ends in
     `/`, as served, so none redirect; `source/robots.txt` has the
     absolute `Sitemap:` URL. The live site's `Sitemap: /wp-sitemap.xml`
     is relative and the file doesn't exist, so Search Console indexes
     nothing today
   * publish to `newblog.ultrasaurus.com`, review, then move the
     `ultrasaurus.com` domain from `www-archive` to the new site;
     keep `www-archive` as a fallback
   * then submit the sitemap in Search Console; its 404 report shows
     which old URLs people still request (more redirects to add)
10. Recover old content (after the deploy)
    1. Play the IndyJunior map in `2003/06/fun-with-maps` with Ruffle
       (Flash emulator, runs `.swf` in the browser)
       * Wayback has `/indyjr/map.swf` and the page, but not the
         `locations.xml` it loaded (`FlashVars`: `xml_file=locations.xml`)
       * recreate `locations.xml` from memory, in the format of
         `https://web.archive.org/web/20110903010655/http://www.bryanboyer.com/indyjunior/locations.xml`
       * host `map.swf` + `locations.xml` on the site, embed with Ruffle,
         and point "places I've lived" at it (until then the link goes to
         the Wayback copy, which shows an empty map)
       * then write a blog post about Ruffle
    2. Recover the "Twitter in the classroom" slides
       (`2009/06/twitter-in-the-classroom` ends with an empty link to
       `docs.google.com/Present?docid=dhn2vcv5_118cfb8msf8`)
       * two Wayback copies, each with broken images:
         2010, 30 slides:
         `https://web.archive.org/web/20101123061724/https://docs.google.com/present/view?id=dhn2vcv5_118cfb8msf8`;
         2013, 35 slides:
         `https://web.archive.org/web/20131119090934/https://docs.google.com/presentation/d/1Kv-Z9SXIDuw0mmpPhFOqmAtFEdKuwF5XxqGrjUfY5vA/present#slide=id.i0`
       * the 2009 post had 25 slides; the deck grew later
       * combine both copies (and any other captures of their images)
         into one complete local copy in `source/`, and link the post
         to it
    3. Show the 4 extra Laszlo Mail screenshots in a post
       (`source/uploads/2005/11/`: `filters.gif`, `blocked-images.gif`,
       `folder-summary-unread.gif`, `import-contacts.jpg`; saved from
       Wayback, no post uses them yet)
    4. Check links to other sites (no worse than the live site, so it
       can wait until after the deploy)
       * for each outside link that 404s, look for a Wayback Machine copy
         (`https://web.archive.org/web/<timestamp>/<url>`) and switch to it
         (done by hand so far: Theory Girl mp3 in
         `2009/08/hacker-love-songs`)
       * start with a read-only report, then fix in small batches
       * compare with the 2021 broken-link spreadsheet
11. Accessiblity
  * Audio for blog posts
  * Alt text for images
