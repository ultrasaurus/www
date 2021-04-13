---
title: 'js meetup, jon boutelle: Flash or Ajax?'
date: '2008-06-06T05:50:26-07:00'
status: publish
permalink: /2008/06/js-meetup-jon-boutelle-flash-or-ajax
author: sarah
excerpt: ''
type: post
id: 384
category:
    - Uncategorized
tag: []
post_format: []
---
[Jon Boutelle](http://www.jonathanboutelle.com/) of [slideshare.net](http://www.slideshare.net/) spoke at the [JS Meetup](http://javascript.meetup.com/4/calendar/7922755/?a=cr1p_grp) last night. He reported a refreshing perspective about the choice between Flash and Ajax on websites today: you quite possibly need both. He made the analogy to having a hammer and a saw — you need both to build a house. (By the way if you haven’t checked out slideshare is is way cool. See a collection of [Jon’s presentations](http://www.slideshare.net/jboutelle) or mine). Notes below:

**Keep Flash on a leash**, only use it for what its really good at

- you have to work extra to get SEO — slideshare puts the transcript of slides at the bottom of the page
- Jon finds that load time on average is worse in Flash (He note: Javascript can be fat too. I find it depends what you are doing — raw script execution and http requests are much slower than the browser, but you can bundle up a bunch of code &amp; graphics in a SWF and get better performance. Still I wouldn’t choose one or the other based on performance.)
- advocates Flash nuggets — I love this term!
- Full screen is nice — use it for good, not for evil
- invisible Flash — you might not even know you are using Flash. Used in some Javascript libs
- – graphics goodies: fonts, vectors, multimedia, recording audio/video, multimedia editing, widgets (don’t worry about layout, but SEO sucks)
- – upload progress bars
- – sockets! comet is cool, but server-side push — libraries w/ Ruby (443)
- – local dataObjects “super cookies” — you can ask the user to save 1GB
- – Flex: 125KB download for the framework

**Javascript cheap tricks** (not quite AJAX). Javascript 101 — you don’t even need to hit the server (although maybe you should if obscured stuff is seldom used)

- tabs (conserve real-estate)
- Accordians (aks Tab sliders) — like tabs only sideways
- Microlinks – expando-tabs
- One second mutation — animated transition: control the user’s attention, they see that the small thing becomes the big thing
- Popups — use with discretion, since you occlude part of the screen

**Javascript Cheap-ish Tricks**

- Malleable content (e.g. edit in place)
- progress indicators
- One second spotlight, famous yellow fade popularized from 37signals, tests well, makes people happy
- Temp message: show message, fade away: don’t leave a permanent mark on the page (sometime doesn’t test well since people miss it)
**Conclusion:**  
What the world needs is Ajax/Flash cross-over artists. Flash doesn’t kill people, people kill people. Can’t we all get along?

**Q&amp;A**  
Q: geni.com — could that be done in Javascript?  
Answer from the audience: zooming would be hard in javascirpt