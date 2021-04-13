---
title: 'sf rails meetup talks about performance'
date: '2011-07-02T11:15:02-07:00'
status: publish
permalink: /2011/07/sf-rails-meetup-talks-about-performance
author: sarah
excerpt: ''
type: post
id: 3214
category:
    - general
tag: []
post_format: []
---
I attended the [SF Ruby on Rails meetup](http://www.meetup.com/San-Francisco-Ruby-on-Rails-Group/events/22207811/) last week with two excellent talks on performance. The first talk, by Brian Doll ([@briandoll](https://twitter.com/#!/briandoll)) of [New Relic](http://newrelic.com/), provided an overview of how to think about performance. In the second talk, Guillaume Luccisano ([@luckwi](https://twitter.com/#!/luckwi)) of [justin.tv](http://www.justin.tv/) shared his experience of optimizing their Rails app.

Performance is a Feature
------------------------

Brian Doll points out that performance is not just about speed, it is about cost. The cloud allows us to add thousands of servers at the click of a button, but as a web app scales to dozens of virtual instances the infrastructure costs increase significantly. We also need to think about **operational efficiency**. Even if it significantly improves performance to create an alternate subsystem on a different server, that system will take effort to maintain and may scale differently from the rest of the system. A homogeneous architecture that is horizontally scalable allows us scale with little or no development costs. Being able to move quickly is the biggest factor in real life scalability.

Martin Fowler’s technical debt quadrant from [a 2009 article](http://martinfowler.com/bliki/TechnicalDebtQuadrant.html) illustrates a different aspect of cost. In thinking about performance, we often make debt tradeoffs. We need to think about the scalability of the system, not just the system in its current state.

[![](http://martinfowler.com/bliki/images/techDebtQuadrant.png)](http://martinfowler.com/bliki/TechnicalDebtQuadrant.html)

Planning for scale doesn’t imply that we should build a very scalable solution before we need it, but we also don’t want to just rewrite everything because it fell over last night.

Brian related thinking about performance to Kent Beck’s RailsConf talk about Agile, where he highlighted five attributes of agile development: Simplicity, Communication, Feedback, Respect and  
Courage. “We can be courageous because of the tools we have.”

Performance Optimization in Rails
---------------------------------

Guillaume Luccisano spent a couple of months optimizing justin.tv while also working on upgrading the site from Rails 2 to Rails 3. In case anyone wasn’t aware, Rails 3 is a little slower than Rails 2. Guillaume guesses about 20% slower.

Guillaume did an amazing job of collecting details about what made a difference in performance optimization. He has shared his slides which report his findings:

<div id="__ss_8476299" style="width:425px"> **[Rails performance at Justin.tv – Guillaume Luccisano](http://www.slideshare.net/kwi/rails-performance-at-justintv-guillaume-luccisano "Rails performance at Justin.tv - Guillaume Luccisano")**<div style="padding:5px 0 12px"> View more [presentations](http://www.slideshare.net/) from [kwi](http://www.slideshare.net/kwi) </div></div>