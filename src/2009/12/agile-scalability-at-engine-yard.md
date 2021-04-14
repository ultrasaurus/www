---
title: 'agile scalability at engine yard'
date: '2009-12-13T11:46:41-08:00'
status: publish
exported_permalink: /2009/12/agile-scalability-at-engine-yard
author: sarah
excerpt: ''
type: post
id: 2213
category:
    - general
tag: []
post_format: []
---
I attended the [EngineYard Road Show](http://www.railsroadshow.com/) a couple of weeks ago. I had low expectations for a mid-week corporate-sponsored event, but I found it to be unexpectedly good. I took a few notes on some of the presentations, which I’ve collected below:

Why Performance Matters
=======================

Tom Mornini of EngineYard told us about a [Google search latency experiment](http://code.google.com/speed/files/delayexp.pdf) which measured drop-off rates when response time was slow. It is awesome that Google also measured that the effects persisted even when the previous fast response time was restored. As humans, our behavior often reflects our expectations, rather than our immediate experience.  
[![](http://img.skitch.com/20091213-xakamqiqfqhnd43dw8pmksj6w4.jpg "Google Search Latency Experiment")](http://www.slideshare.net/engineyard/rail-performance-in-the-cloud-opening)  
I also enjoyed the four stages of performance which he defined as Delight, Satisfaction, Frustration and Abandonment. It is really easy to get bogged down in the wrong places and optimize things that don’t matter when working on performance. It was nice to see a clear presentation on how to prioritize (and why to prioritize) work on performance and scalability. ([Slides](http://www.slideshare.net/engineyard/rail-performance-in-the-cloud-opening))

Agile Deployment
================

Bill Lapcevic [(@blap](http://twitter.com/blap)) from [New Relic](http://www.newrelic.com/) challenged the audience to do “agile deployment.” [AboutUs](http://www.aboutus.org/) often releases several times per day — averaging 10 per week. “Smaller deployments more often allow you to back out small pieces of code” says Ward Cunnigham of AboutUs. Instead of stress and load testing before you deploy, make it part of the culture of your development team to watch the performance effects of the live site right after deployment and make it easy to roll back and roll forward.

Engine Yard Cloud
=================

Abheek Anand @abheek [presented](http://www.slideshare.net/engineyard/scaling-your-applications-with-engine-yard-cloud) Engine Yard’s new Cloud product, which has a complete web UI for set up. There’s no command-line interface to it, which is weird, since it offers a deeply geeky array of options for you to tweak exactly how your stack is configured. This is the other end of the spectrum from Heroku. You even get ssh access!

Abheek notes that Engine Yard sets everything up to be performant by default — 20% perf improvement out of the box, e.g. gzip’d content, correct load balance settings. He also adds this generally useful tip: measure everything, identify top ten, pick #1 and optimize.

More about Agile
================

Ian McFarland ([@imf](http://twitter.com/imf)) talked about agile, rails and the cloud:

- specialization breeds efficiency: cloud allows you to focus on your key business value (not ops)
- increase your bus number: the number of people who would need to get hit by a bus before it would jeopardize your project
- shift from a technical decision about whether we can release to a business decision of whether you want to
- <span><span>business driven is sadly, kind of a novelty in software</span></span>

<span><span>Also there was an interesting talk on cloud testing by [soasta.com](http://soasta.com/) — wish I had that the last time I had to build a load test lab! </span></span>