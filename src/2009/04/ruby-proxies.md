---
title: 'ruby proxies'
date: '2009-04-17T14:11:00-07:00'
status: publish
exported_permalink: /2009/04/ruby-proxies
author: sarah
excerpt: ''
type: post
id: 1051
category:
    - general
tag:
    - gogarugo
    - Ruby
post_format: []
---
[Ilya Grigorik](http://www.igvita.com/), gave a very informative talk “Ruby Proxies for Scale, Performance, and Monitoring”

Ilya describes a proxy server as his new favorite hammer. I can think of lots of cases where having an easy way to write a proxy server would come in handy. Mostly what we think of when we think of proxy servers is a “transparent, cut-through proxy,” but proxies can be useful for other purposes.

The problem that led Ilya to write a proxy server was benchmarking and performance testing. He started with HTTPPerf is good tool for simulating load, but it is only good for a single run. [autoperf](http://github.com/igrigorik/autoperf/) will make multiple runs and simulate more users.

[em-proxy](http://github.com/igrigorik/em-proxy/) Very simple syntax to send traffic to both the production server and benchmark server (and only the response is returned from production). Real-time benchmarking against production traffic and user sees no performance hit. Only about 300 lines of code, shows the pattern for how to build a proxy server.

Ilya walked us through using [EventMachine](http://rubyeventmachine.com/) which has very concise, easy-to-read syntax for implementing proxy servers. This does not need to be restricted to http, but can work with any protocol.

Ilya described an interesting use case in detail. They created a proxy server which works with Beanstalkd, a distributed in-member work queue, where jobs are stored in MySql when they don’t need to be in memory.

Slides from the talk:

<div id="__ss_1307248" style="width:425px;text-align:left">[Ruby Proxies for Scale, Performance, and Monitoring – GoGaRuCo – igvita.com](http://www.slideshare.net/igrigorik/ruby-proxies-for-scale-performance-and-monitoring-gogaruco-igvitacom?type=presentation "Ruby Proxies for Scale, Performance, and Monitoring - GoGaRuCo - igvita.com")<div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">View more [presentations](http://www.slideshare.net/) from [Ilya Grigorik](http://www.slideshare.net/igrigorik).</div></div>