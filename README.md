# ultrasaurus.com

Sarah Allen's blog, "the evolving ultrasaurus", since 2003.

Now a static site
built with [altwebgen](https://github.com/ultrasaurus/altwebgen) and
hosted on Cloudflare Pages.

## Layout

* `source/` — posts in `YYYY/MM/slug.md`, with comments in
  `slug.responses.yaml`; pages like `about/` and `archives/`; images and
  files in `uploads/`
* `source/_site.yaml` — site settings (`site_url` turns on `sitemap.xml`)
* `source/_redirects` — old URLs → new ones for Cloudflare; written by
  `migration/make_redirects.py`, so edit that, not this
* `template/` — Handlebars layouts and CSS
* `migration/` — the 2026 migration: Python scripts (imports, link
  fixes, Wayback lookups, redirects), `movable-type.yaml`, and `plan.md`
  with the steps and decisions. The scripts read `export/` (the WordPress
  export, git-ignored) and `../www-archive` (the old site)

Drafts are posts with `status: draft`. They are left out of the build and
the sitemap, and listed at `/drafts/` when previewing with `--drafts`.

## Preview

From this folder, with altwebgen checked out three levels up:

```
cargo run dev
cargo run dev --drafts
```

## Deploy

Build into a fresh folder (not `.dist`, which the dev server may have
filled with drafts), then upload; only changed files are sent:

```
cargo run --release -- -o /tmp/ultrasaurus-deploy build
wrangler pages deploy /tmp/ultrasaurus-deploy --project-name www-ultrasaurus --branch main
```

`--branch main` makes it the production deploy.

## History

* 2003–2008: Movable Type, at `/sarahblog/archives/NNNNNN.html`
* 2008–2021: WordPress
* 2021: WordPress export saved as a static copy
  ([www-archive](https://github.com/ultrasaurus/www-archive), GitHub Pages);
  an Eleventy version was started here
* 2026: moved to altwebgen. Posts, comments and drafts imported from the
  WordPress export; old links fixed; text, images and pages lost along the
  way recovered from the Wayback Machine where it had them. The 2021
  broken-link check (60 links, via deadlinkchecker) is in a
  [spreadsheet](https://docs.google.com/spreadsheets/d/1sYxRjtbNwGNLc8RIhs-d9T5aVPmjjiniY5Qm1FtzI_g/edit#gid=0).

## TODO

* Google Analytics (or another analytics tool)
* check links to other sites, using Wayback copies for dead ones
