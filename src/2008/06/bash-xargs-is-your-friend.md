---
title: 'bash: xargs is your friend'
date: '2008-06-14T12:17:18-07:00'
status: publish
permalink: /2008/06/bash-xargs-is-your-friend
author: sarah
excerpt: ''
type: post
id: 390
category:
    - code
tag: []
post_format: []
---
For some reason, since I set up my new machine, when I p4 sync I would get directories that aren’t writeable. This means that lzx files won’t compile since the swf needs to be written into the directory.

To work-around this, I tried to just set permissions on all the directories. My first attempt (below), didn’t work…. anyone know why? the second one is more verbose and did work.

$ find \* -type d | chmod a+w  
chmod: missing operand after `a+w’  
Try `chmod –help’ for more information.

Verbose work-around:  
$ for i in \* ; do if \[ -d $i \]; then chmod a+w $i ; fi ; done

**A better answer**: the chmod command does not accept arguments on stdin, so you can’t just pipe a file list to it:

$ find . -type d -print0 | xargs -0 chmod a+w

[xargs](http://en.wikipedia.org/wiki/Xargs) is your friend