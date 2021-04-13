---
title: 'building unix package with autotools'
date: '2013-07-14T12:41:52-07:00'
status: publish
permalink: /2013/07/building-unix-package-with-autotools
author: sarah
excerpt: ''
type: post
id: 4070
category:
    - code
tag: []
post_format: []
---
ever wonder what all those random files are at the root of some package source that you are playing with? and how exactly does the mystical `configure` command actually do?

Alexandre Duret-Lutz has created a fabulous [Autotools Overview &amp; Tutorial](http://www.lrde.epita.fr/~adl/dl/autotools.pdf) — well worth flipping through the first 19 slides (38 pages of the PDF since each there are “builds” of individual slides exported as multiple pages).

Later, at page 97, he starts a tutorial section, which I replicated in this [git repo](https://github.com/ultrasaurus/hello-autotools) — the README has a little cheat sheet of step to set up and build the package.