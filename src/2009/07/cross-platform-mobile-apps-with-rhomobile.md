---
title: 'cross-platform mobile apps with rhomobile'
date: '2009-07-10T07:00:18-07:00'
status: publish
exported_permalink: /2009/07/cross-platform-mobile-apps-with-rhomobile
author: sarah
excerpt: ''
type: post
id: 1747
category:
    - general
tag: []
post_format: []
---
[Rhomobile](http://www.rhomobile.com/) offers an open-source, ruby application framework. On the client-side, Rhodes allows you to build mobile applications on iPhone, BlackBerry, Windows Mobile, Symbian and Android. The client app could be stand-alone or connected. On the server-side, enabling connected applications, RhoSync dramatically simplifies client-server data transfer.

I spent some time experimenting with it last week. The docs were pretty raw, but these folks are moving fast and the doc issues that I ran into have been fixed already. They also have a responsive [google group](http://groups.google.com/group/rhomobile). I built an iPhone app with a [Heroku](http://www.heroku.com/)-hosted Rails back-end in about a day. Now with [Rhohub](http://www.rhohub.com/), [it appears](http://www.youtube.com/rhomobile#play/all/uploads-all/0/yTmdV4eC_7o) that I could have built that same app in about a minute. I’ve just been approved for the beta, and am looking forward to checking it out myself.

A number of folks have asked me about my experience with Rhodes and are interested in learning about it, so I drew the diagram below in [gliffy](http://www.gliffy.com/) this morning to outline how it works ([click](http://www.gliffy.com/pubdoc/1759859/L.jpg) it for a larger image).

[![rhomobile architecture](http://www.gliffy.com/pubdoc/1759859/M.jpg)](http://www.gliffy.com/pubdoc/1759859/L.jpg)

The green in the diagram represents Rhomobile framework code and the blue represents your code (where the blue cloud could be your web service or anything else you decide to connect to). You write your code in Ruby along with handy Rails-like generators. The UI is HTML and CSS, but it hooks into native controls. Very cool. I am intrigued to see just how the nuances of UI translate across all of the different client platforms using the framework. However, I don’t really need to worry about how much control I will have: the platform is open source, and if need be, I can always fall back to extending the platform with my own native code.