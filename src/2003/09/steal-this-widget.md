---
title: 'steal this widget'
date: '2003-09-18T17:32:59-07:00'
status: publish
permalink: /2003/09/steal-this-widget
author: sarah
excerpt: ''
type: post
id: 61
category:
    - Uncategorized
tag: []
post_format: []
---
With a little help from Peter Andrea for the art, additional borrowed code and inspired naming from [Mark Davis](http://drdreff.blogspot.com) and a few extra lines of my own…. you can now check out the code for the link browser by simply clicking on “view source” in the top-right.

The widget uses Laszlo’s “[Tab Slider](http://www.laszlosystems.com/developers/documentation/lzxref/tabslider.php)” component, a UI element that pre-dates Macromedia’s Accordian Pane which offers that same functionality. The URL for the XML data file (in OPML format) is passed as a parameter to the application. One of the features of the Laszlo Presentation Server is that it auto-magically fetches the file from a remote site. You don’t have to worry about cross-domain scenarios because the SWF and its data end up being served by the same server (LPS). This should clarify some questions from [JD’s post](http://www.markme.com/jd/archives/003298.cfm).

Now its easy to steal the code for the widget if you happen to already by running LPS like Mark or me. For those who aren’t yet, I would like to make it so its easy to steal the widget as an HTML snippet like [Marc](http://blogs.it/0100198/) did. For now its not for the timid, but feel free to view source in your web browser menu and grab the embed/object tag and add your own colors and opml file for your page.