# www.ultrasaurus.com as static site

## Migration notes
* Migrated from WordPress (previously from MoveableType)
* pre-migration (4/13/2021) - 60 broken links detected via [deadlinkchecker](https://www.deadlinkchecker.com/) -- save in [spreadsheet](https://docs.google.com/spreadsheets/d/1sYxRjtbNwGNLc8RIhs-d9T5aVPmjjiniY5Qm1FtzI_g/edit#gid=0)
* using github actions to deploy to github pages ([tutorial](https://www.rockyourcode.com/how-to-deploy-eleventy-to-github-pages-with-github-actions/)
modified for yarn and using cname instead of subdirectory)

## to check DNS propagation
dig BLOG.ULTRASAURUS.COM +nostats +nocomments +nocmd

## TODO

1. don't forget to add back google analytics
1. check broken links -- did it get worse?

----
Could do these after switching DNS 
* Categories
* Comments?

## Notes on Eleventy

One maintainer, friendly yet possibly fragile.

Dependencies (that I depend on)
* [liquid](https://www.npmjs.com/package/liquid) - not wed to liquid, attempt to use non-liquid-specific syntax, mainly use it because there were many examples and seemed simpler than nunjucks (want as little content-embeded logic as possible), could be replaced by [liquidjs](https://github.com/harttle/liquidjs), not sure why both exist
* [markdown-it](https://github.com/markdown-it/markdown-it) JS markdown parser


