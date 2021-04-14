---
title: 'exploring ghostscript API in C'
date: '2017-11-24T06:56:21-08:00'
status: publish
exported_permalink: /2017/11/getting-started-with-ghostscript-api-in-c
author: sarah
excerpt: ''
type: post
id: 6359
category:
    - code
tag: []
post_format: []
---
Ghostscript lets you do all sorts of PDF and PostScript transformations. It’s got a command-line tool which is great for page-level operations.

Installation on a mac is pretty easy with [homebrew](https://brew.sh/):

`brew install ghostscript`

The syntax for the commands not very memorable, but easy once you know it. To get a PNG from a PDF:

`gs -sDEVICE=pngalpha -o output.png input.pdf`

We can also use the API to call the engine from C code. Note: to use this from a program we need to publish our source code (or purchase a license from the nice folks who create and maintain Ghostscript), which seems fair to me. See [license details](https://www.ghostscript.com/download/gpdldnld.html).

To do the exact same thing as above, I created a small program based on the [example in the API doc](https://www.ghostscript.com/doc/current/API.htm#Example_usage), which I’ve posted on [github](https://github.com/ultrasaurus/ghostscript-c-app/tree/pdf2png).

What I really want to do is to replace text in a PDF (using one PDF as a template to create another). It seems like all the code I need is available in the Ghostscript library, but maybe not exposed in usable form:

- Projects Seeking Developers [Driver Architecture](https://www.biu.ac.il/os_site/documentation/gs/Projects.htm#Driver_architecture) was the only place in the docs that I learned that we can’t add a driver without modifying the source code: “Currently, drivers must be linked into the executable.” Might be nice for these to be filed as bugs so interested developers might discuss options here. Of course, not sure that making a driver is a good solution to my problem at all.
- There’s an option `-dFILTERTEXT` that removes all text from a PDF that I thought might provide a clue. I found the implementation in [gdevoflt.c](http://git.ghostscript.com/?p=ghostpdl.git;a=blob;f=base/gdevoflt.c;h=5e1b5cf60aa467dae4a913fa2975002c47f0b92e;hb=HEAD) with a comment that it was derived from [gdevflp.c](http://git.ghostscript.com/?p=ghostpdl.git;a=blob;f=base/gdevflp.c;h=2e4a07b1d96429a2771bd7b5ef9af62ce10dac50;hb=HEAD).
- `gdevflp`: This device is the first ‘subclassing’ device; the intention of subclassing is to allow us to develop a ‘chain’ or ‘pipeline’ of devices, each of which can process some aspect of the graphics methods before passing them on to the next device in the chain.

So, this appears to require diving into the inner-workings of Ghostscript, yet the code seems to be structured so that it is easily modifiable for exactly this kind of thing. It seems like it would be possible to add a filter that modifies text, rather than just deleting it, as long as the layout is unaffected. This implies setting up for building and debugging GhostScript from source and the potential investment of staying current with the codebase, which might not work for my very intermittent attention.