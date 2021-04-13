---
title: 'rhomobile reflections'
date: '2009-08-15T09:31:12-07:00'
status: publish
permalink: /2009/08/rhomobile-reflections
author: sarah
excerpt: ''
type: post
id: 1935
category:
    - general
tag: []
post_format: []
---
I’ve been actively developing mobile applications using the new SmartPhone application framework from [Rhomobile](http://rhomobile.com/). I wrote an [overview of the technology](https://www.ultrasaurus.com/sarahblog/2009/07/cross-platform-mobile-apps-with-rhomobile/), but folks have asked for some more details. Below are some reflections from my development experience so far:

Rhodes
======

Rhodes is the client-side framework that Rhomobile offers. This is the key technology that abstracts the device-specific functions and makes Rhodes (mostly) platform independent. The Rhodes architecture is compelling, simple applications are dead simple, but any real application is going to take thoughtful design and implementation work. This is really what you want of any technology. A key strength of Rhodes is that it is open source and you can dive into device-specific code if you have a need — I haven’t done this yet, but just knowing it is there makes me confident that I won’t run into a wall as one always fears when adopting a new framework. I have found that Rhodes significantly accelerates development (once you know its ins and outs).

The major drawback to Rhodes is that it is pretty rough around the edges right now. The docs give you almost all of the information you need and the rest you can pretty much guess. The hard part is that there are few examples of the design patterns that that you commonly use in any application that goes beyond a toy; however, the Rhomobile team is incredibly responsive on the google group and very welcoming of contributions to the docs on the wiki and the core code, so it is only a matter of time before this is fixed. I have run into a few bugs, but again, open source helps here.

On the awesome side of Rhodes: you are writing Ruby, CSS and HTML and once you know a design pattern, replicating it for another app (or another part of the same app) is trivial, which is typically not the case with languages like C or Java. It follows a pattern which a lot of mobile developers are using in their native apps of defining UI in embedded HTML controls that call out to native functions. Rhodes wires in Ruby, so you can easily embed code in HTML (with erb syntax and some useful helper methods borrowed from Rails). It seems a natural crystallization of the methodologies that manyfolk are building by hand, which is what you want and expect from any good framework.

RhoSync
=======

RhoSync offers some serious magic. You can write a one page of code on the server side that translates your web service or whatever into a generic result set and then automatically syncs it to the client. I’ve written sync code before: even a basic implementation can stretch your brain and take some work to get right. By using RhoSync you can easily get the data from the server onto your client and vice-versa. Then, when you are out of cell-phone range or on a flaky network, your data is still available on the device, without additional development work. This is well-worth the license fee, and it is free for open source apps.

Final Notes
===========

Rhodes 1.2 is a huge step forward. It is great to see this company quickly addressing known issues and adding features. RhoHub is a very cool idea. It is still in private beta (and deservedly so), but it is evolving quickly and I look forward to its public unveiling.

In summary, if you want to get into mobile app development, you know Ruby and you are comfortable on the cutting edge, Rhodes is a great option right now. If you need to develop a mobile app and you plan to spend some serious time on it, it’s worth starting now, even wih the rough spots, since after you climb the learning curve Rhodes and RhoSync will be a huge time saver.