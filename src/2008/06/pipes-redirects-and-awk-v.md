---
title: 'pipes, redirects and awk -v'
date: '2008-06-15T11:00:24-07:00'
status: publish
exported_permalink: /2008/06/pipes-redirects-and-awk-v
author: sarah
excerpt: ''
type: post
id: 391
category:
    - code
tag: []
post_format: []
---
I wanted to take the output of a command and put it in a temporary variable so I can append a string to it. (Trying to script perforce to append something to my client spec without interactive involvement.)

First attempt:  
$ p4 client -o &gt; $CLIENTSPEC  
c:cygwinbinbash: $CLIENTSPEC: ambiguous redirect  
I later learned that redirect is only for files.

Next attempt:  
$ TEST=`p4 client -o`  
$ echo $TEST  
//depot/apps/diamond-calendar-preview/… //sallen-LENOVO/svn/openlaszlo/branches/pagan-deities/diamond-calen //depot/apps/diamond-amaranth-ms2/… //sallen-LENOVO/svn/openlaszlo/branches/pagan-deities/diamond-amaranth- //depot/sandbox/my-webtops/… //sallen-LENOVO/svn/openlaszlo/branches/wafflecone/diamond/client/my-webtops/. ..  
which seems to have swallowed line endings and only provided the last few lines of output.

My colleagues at Laszlo, Trebor Fenstermaker and [Chris Pettitt](http://www.samsarin.com/blog/) and [ptw](http://pt.withy.org/), showed me the error of my ways and provided some good tips. Trebor noted that there is a length limit for shell variables and that line endings will get lost. Chris introduced a combination of pipe and awk -v which did the trick. At first I thought Tucker’s simple echo solution wasn’t working, but he pointed out that I just needed to properly parenthesize my commands.

**What worked:**  
p4 client -o | awk -v append=” //depot/apps/test/… //sallen-test/svn/openlaszlo/branches/pagan-deities/test/…” ‘{ print $0 } END { print append }’ | p4 client -i

**Even simpler:**  
(p4 client -o; echo ” //depot/apps/test/… //sallen-test/svn/openlaszlo/branches/pagan-deities/test/…” ) | p4 client -i

**Notes:**

- [Redirect](http://en.wikipedia.org/wiki/Redirection_%28Unix%29) only works for files, there are lots of different types of redirects (&gt; is a simple redirect of stdout to a file, &gt;&gt; will append to a file, 2&gt; will redirect stderr)
- awk -v will define a variable which can then be used in the awk script
- You need to properly parenthesize your commands: ( p4 client -o; echo “Thing to append” ) | p4 client -i
  
  The parens will execute the p4 and echo commands in a sub-shell so the output of both will be piped to the next. Without the parens you have said:
  
  p4 client -o; ( echo “Thing to append” | p4 client -i )
  
  I.e., run the client command, then run echo to a pipe.
- [Pipe](http://en.wikipedia.org/wiki/Pipe_%28Unix%29) will let you take the stdout of one command and send it to the stdin of another:  
  ![](http://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Pipeline.svg/280px-Pipeline.svg.png)