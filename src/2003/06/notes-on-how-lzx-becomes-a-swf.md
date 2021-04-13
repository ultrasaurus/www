---
title: 'Notes on how LZX becomes a SWF'
date: '2003-06-18T06:19:38-07:00'
status: publish
permalink: /2003/06/notes-on-how-lzx-becomes-a-swf
author: sarah
excerpt: ''
type: post
id: 29
category:
    - Uncategorized
tag: []
post_format: []
---
Don Park recently spent some time with the [Laszlo Presentation Server](http://www.laszlosystems.com/) and drew a nice architecture diagram in his [blog](http://www.docuverse.com/blog/donpark/2003/06/16.html#a596). Generating an LZX from a JSP is one way to create applications in Laszlo. A more common development pattern is to simply write an LZX file that references an XML data source. I’ve drawn a diagram with a similar structure to Don’s that shows the HTTP requests from the browser, to illustrate how this works.

![](/images/blog/lzx.gif)  
1\. The user goes to the web page “http://mysite.com/hello.html”  
(a) the browser requests “hello.html” from mysite.com  
(b)The web server sends that document it to the browser.

2\. The browser notices that “hello.html” references “http://mysite.com/hello.lzx”  
(a) The browser requests “hello.lzx” from mysite.com  
(b) The Laszlo Presentation (LPS) finds “hello.lzx,” creates a SWF and sends it to the browser.

3\. Your app has referenced a data source (an XML file on the server’s local file system, on any other server, or dynamically created XML develivered over HTTP)  
(a) The LPS-generated SWF makes a native Flash call that causes the browser to send a request to LPS  
(b) LPS fetches the data (which is in standard XML). It transforms the data into native Flash goop and sends it back to the browser.  
(c) It appears in the SWF auto-magically datamapped to the appropriate view or whatever you asked it to do in your LZX file.

What Laszlo has done is to normalize the Flash runtime for the creation of applications. It all ends up running in the Flash player, but there is a bunch of Laszlo magic that lets you focus on application development and interface design. Laszlo provides a framework, which includes a view system, data mapping, layouts, constraints and all sorts of useful stuff.

One last technical note, LPS does a bunch of smart caching. If an LZX file or the data source hasn’t changed, LPS efficiently delivers the same bunch of bits it created for the previous request. Incremental compiles are achieved by breaking up your app into separate files, typically using the &lt;library&gt; tag. Then LPS only compiles the file that has changed.