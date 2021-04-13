---
title: 'Laszlo OPML viewer'
date: '2003-09-09T01:04:26-07:00'
status: publish
permalink: /2003/09/laszlo-opml-viewer
author: sarah
excerpt: ''
type: post
id: 58
category:
    - Uncategorized
tag: []
post_format: []
---
Inspired by Mark Davis’ [Laszlo link viewer](http://drdreff.blogspot.com/2003_09_07_drdreff_archive.html#106305830618139273), I created a little [OPML file](http://host2.ultrasaurus.com:8080/lps/my-apps/opml/opml.xml) with some of my collected links and modified his LZX file to read the data from the there. \[Moved this version of the app into this blog entry, since I am going to update my gutter\]

The new app is only 60 lines of [code](http://host2.ultrasaurus.com:8080/lps/my-apps/opml/opmlviewer.lzx?lzt=source). LZX is fun!

  
It took me about two hours, from inspiration to deployment. Here’s what I did:

1. I read a bit about OPML. I ended up snagging the OPML file from [blogrolling.com](http://www.blogrolling.com/) and then hand-edited to create some categories. I wonder if I upgrade my account and have multiple blogrolls, does it generates a single hierarchical OPML? … that would be nice.
2. I borrowed the code and art assets — thanks Mark
3. I modified the LZX: 
  - added a dataset that references opml.xml
  - added datapaths to various views
  - changed color definitions to canvas attributes (although I probably should have left these as parameters)
  - added rollover feedback for links
4. created a 2 frame Flash movie for the link icon, drawing two icons by hand (a little rough, but I like to have some feedback that a new window will be opened)
5. uploaded the files to the [Laszlo Presentation Server](http://www.laszlosystems.com) that I recently set up at [mediatemple](http://www.mediatemple.net)
6. updated my MoveableType default template