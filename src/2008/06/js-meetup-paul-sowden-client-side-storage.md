---
title: 'js meetup, paul sowden, client-side storage'
date: '2008-06-06T06:11:58-07:00'
status: publish
permalink: /2008/06/js-meetup-paul-sowden-client-side-storage
author: sarah
excerpt: ''
type: post
id: 385
category:
    - Uncategorized
tag: []
post_format: []
---
Paul Sowden of [meebo](http://www.meebo.com/) talked about client-side storage options at the [JS Meetup](http://javascript.meetup.com/4/calendar/7922755/t/cr1p_grp/?) last night.  
Great info! Here are my notes:

**Client-side storage… more options than cookies**  
3 examples:

- [halfnote](http://aaronboodman.com/halfnote/) \[Update: thanks Paul!\]
- gmail
- sticky notes

… not too exciting, but we could do more exciting stuff if we can tackle the x-browser issues. Technology is different per browser, standard has variants.

- Gears: sync’d db, SQL interface, search over the DB, unlimited storage (at least in the beta)
- WHATWG, fr HTML5: Safari 3.1+, WebKit, at least two MB, bit more code,
- FF2+ IE8, WHATWG Global Storage, when values change events are fired, in FF you get up to 5MB, in IE its XML, in FF its an SQLLite DB (allows potentially browser-desktop app) — pretty clean simple code
- userData HTML Behaviors in IE 5.5+, up to 1MB per domain — simplest code
- Flash Cookies, 100KB by default, but youcan ask the user for more (clunky little Flash interface), you’ll need to use SWF wrapper and Javascript bridge

On meebo, they checked out how many people had which available

- 87% Flash (they checked for v8, but this has been available since Flash Player 6, so ymmv)
- 74% have native storage
- gears in the single digits

Note: 97% have one of those, 96% had cookies enabled!

Libraries available

- Dojo.storage
- Persist.js – normalize API, just key-value gears

Note: global storage has widest adoption, but global storage actually has been taken out of the specification!  
\[Update: slides from this talk have been posted on [slideshare](http://www.slideshare.net/idontsmoke/client-side-storage/)\]

<div id="__ss_452242" style="width:425px;text-align:left"><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">[![SlideShare](http://static.slideshare.net/swf/logo_embd.png)](http://www.slideshare.net/?src=embed) | [View](http://www.slideshare.net/idontsmoke/client-side-storage?src=embed "View Client Side Storage on SlideShare") | [Upload your own](http://www.slideshare.net/upload?src=embed)</div></div>