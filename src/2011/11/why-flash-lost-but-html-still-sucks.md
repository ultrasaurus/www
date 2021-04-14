---
title: 'Why Flash Lost but HTML Still Sucks'
date: '2011-11-09T16:42:51-08:00'
status: publish
exported_permalink: /2011/11/why-flash-lost-but-html-still-sucks
author: sarah
excerpt: ''
type: post
id: 3443
category:
    - general
tag: []
post_format: []
---
I’ve been creating and using cross-platform tools for application development since the late 80s, from VideoWorks, HyperCard, and Authorware to Director, SuperCard, ScriptX and mTropolis to Shockwave, Flash, and HTML/Javascript. We’ve moved past the experimental days when it was called multimedia and techniques for interactivity, graphics, animation and information design are routinely applied for mainstream consumer and business applications. The dominant paradigm is now HTML.

When people say HTML, they really mean HTML, CSS, Javascript and a collection of proprietary browser APIs which are similar enough across desktop and mobile browsers that we can build applications that look and feel the same even if the code under-the-hood needs to be a little different.

Flash successfully enabled one set of code for one application, independent of browser and OS. Macormedia documented the file format back in the 90s. The Flash Player itself remained proprietary, but the open file format enabled competitive authoring tools like OpenLaszlo in addition to the original Flash authoring tool and later Flex. Of course, OpenLaszlo moved to support HTML many years ago, as browsers grew faster and more capable making HTML a practical choice for apps with desktop-like interactivity.

It’s Not Just About Technical Merits
------------------------------------

I believe that the technical reason that Flash lost was that Flash never completely made the leap to app development from its origins in games and entertainment (some of the following may be out of date, since I stopped using Flash for anything but video 2 years ago). However, the big reason that Flash lost was an emotional one that Steve Jobs did a good job of propagating. Macromedia and Adobe never successfully embraced and fostered an open source approach to the platform, and sadly I think the marketing of this is more important today than the reality. The reality is that any effective, so-called HTML5 implementation that rivals Flash uses proprietary browser APIs that differ across browsers. Today a lot of that is hidden by popular frameworks, but any Javascript developer that has produced something meaningful that is widely used knows what I’m talking about.

The HTML, CSS, and JavaScript you need to write for the iOS implementation of the webkit browser has a lot in common with what you would need to write for the Windows Phone 7 Internet Explorer which both share a lot with the documented standards and their desktop counterparts, but share a lot less with BlackBerry 4 browsers or IE6, let alone earlier browser versions. Standards are only as good as their widespread and shared implementations. In the real-world, we do what works, which means we write to proprietary APIs.

For a while it looked like Flash might just offer a proprietary API that worked effectively across desktop, web and mobile, but they didn’t effectively make the leap to mobile, nor did they keep up with some of the capabilities of the desktop browsers; however, neither have web browsers yet to fully catch up to Flash. The standards committee approach doesn’t seem to be effectively driving new capabilities and the platforms are splintering even more than they were in the late 90s.

So why did Flash lose (technically)?
------------------------------------

- Text was never a first class citizen (undo, spellcheck, etc.) — the truth is that text is hard and really important. HTML forced web browsers to do this very well. With the addition of JavaScript, with its dynamic manipulation of the DOM, web applications started to be able to have the kinds of interactions people were familiar with from the desktop, but Flash never matched with regard to text.
- Settings… (This should have been called Flash Player Settings: with the addition of context menu items, the “Settings…” menu may appear to control application setting; however, if someone picks that menu item when an iframe is partially obscuring the app, it will not appear to the end-user and the app will seem to hang. I have to admit personally responsibility for screwing this up circa 2000 when I was at Macromedia leading the Flash video team. In my own defense, it is very hard to balance usability and security. I wish we had done more of a trusted app model with authorization of features (like Android and iOS do fairly well for mobile apps) and used OS dialogs to prevent spoofing.
- Drag &amp; drop not integrated with the desktop (Browsers are doing better on this, but there is still a ways to go)
- Cut/Copy/Paste really needs to work well for text and all media types, which is still not fully there on browsers.
- http auth: seriously silly that this was not easily supported
- Sometime network operations fail — real apps need reliability

Why HTML still sucks, just like Flash
-------------------------------------

1. “This script has caused the Flash Player to run slowly” — web browsers haven’t figured this out either, I like how Apple handles this with desktop apps better
2. From a performance perspective, HTML/Javascript has the same challenges as Flash — has anyone else noticed the return of “skip intro” and progress bar loading screens, but they are so-called HTML5 sites instead of Flash?

How HTML sucks more than Flash
------------------------------

Desktop HTML video suffers from same of the same issues as mobile web video:

1. The only use case that is well-vetted and works effectively cross-platform is playing a movie with VCR controls. There are a lot of other video interaction use cases that Flash did a very good job of supporting and HTML isn’t there yet on even modern browsers, let alone on the range of browsers and platforms supported by Flash.
2. There is no accepted standard here — we’re back to the codec/format wars of the late ’90s with Apple sticking to QuickTime and Google arguing that zero cost = open. This is a hard problem, and pretending it is solved isn’t helping anyone.

and of course, same goes for audio.