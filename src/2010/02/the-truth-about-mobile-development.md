---
title: 'the truth about mobile development'
date: '2010-02-21T08:56:26-08:00'
status: publish
permalink: /2010/02/the-truth-about-mobile-development
author: sarah
excerpt: ''
type: post
id: 2411
category:
    - general
tag: []
post_format: []
---
For my talk at [LA RubyConf](http://www.larubyconf.com/), I decided to share some truths about mobile development, in general, rather than focusing only on how it is different with Ruby using the [Rhomobile](http://rhomobile.com/) platform.

The truth is that mobile development sucks. With Ruby, sometimes it sucks less. The unavoidable problem is that at the end of the process you still need to get your app on the device using cruddy development tools reminiscent of the 1990s. I likened mobile developers to people who like to get tattooed. Perhaps some are thrilled by the painful process, but most endure it to achieve the end effect. Mobile applications are compelling, wonderful expressions of some practical problem solved that you can carry around in your pocket. Despite the often frustrating and stupid steps that I need to follow to get things done, I love what I can build as a mobile developer.

Rhomobile is steadily normalizing some of the process to smooth out the cross-platform differences using tools and techniques from Ruby, which I discussed at the end. My talk reviewed the development process backwards, starting with the user experience, reviewing what it takes to distribute the app and build it for distribution, then finally reviewing the code ([posted on github](http://github.com/blazingcloud/rhodes_rubyconf)). I posted links to the app for [iPhone and BlackBerry](http://blazingcloud.net/mobile/).

The key point on the user experience is that mobile apps should be different on each device, but those differences should be superficial. It is essential that your app use the common UI patterns that users of that device expect, but the core of your app has to do with the problem you are solving and that should be consistent across devices. For the RubyConf app, those device-specific differences were the navigation. On iPhone, there’s a tabbar across the bottom. On Android, there is also a tabbar that has a slightly different look and is positioned across the top. On BlackBerry, these navigation options appear in a menu. The user of each device would find the navigation expected, since it is consistent with how other apps look and feel on that device. Meanwhile, most of the screens are identical across the app. I didn’t discuss the map implementation which is almost the same across devices — of course, it always looks like a map with markers, but the markers have a different visual representation and the pan/zoom controls are different.

The other point about user experience, which is not expressed by the RubyConf app, since it is really a work-in-progress, is that your branding should be consistent across platforms. Mobile apps have more in common with web applications than they do with desktop applications. On the web, your brand is integrated into your application UI. I expect that to be the common pattern for mobile applications as well.

The process of building, signing and distributing the app is quite different cross-platform. It is really hard without actually doing it to get a feel for what it takes and how long it takes to do this on each platform. The documentation is scattered and hard to follow even for a single vendor. One of the goals of my [upcoming book](http://apress.com/book/view/9781430228684) is to pull together this information and help people understand what is common across platforms and what is consistent. In this talk, I gave a lightning-speed overview of the process on iPhone, BlackBerry and Android.

The slides for the talk don’t really stand alone, but I am posting them here for reference:

<div id="__ss_3235188" style="width:425px;text-align:left">[Mobile Ruby, LA RubyConf](http://www.slideshare.net/sarah.allen/mobile-ruby-la-rubyconf "Mobile Ruby, LA RubyConf")<div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">View more [presentations](http://www.slideshare.net/) from [Sarah Allen](http://www.slideshare.net/sarah.allen).</div></div>