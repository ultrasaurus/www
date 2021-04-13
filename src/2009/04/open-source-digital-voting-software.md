---
title: 'open source digital voting software'
date: '2009-04-19T06:40:09-07:00'
status: publish
permalink: /2009/04/open-source-digital-voting-software
author: sarah
excerpt: ''
type: post
id: 1119
category:
    - general
tag:
    - 'Add new tag'
    - gogaruco
    - Ruby
post_format: []
---
Josh Susser, organizer of the [Golden Gate Ruby Conference](http://gogaruco.com), introduced this talk by saying that he wanted to have talks that weren’t only about *how* we do what we do, but also about *why* we do what we do. Gregory Miller’s talk “Trust the Vote: An Open Source Digital Public Works Project” addressed a significant issue for the United States and for democracy in general, and spoke to why the open source process that is so alive in the Ruby community is critical to solving many of the problems of our day.

Here in the U.S., we have some serious problems with our voting system:

- No Federal Guidelines about how votes are counted
- No assurance in California that absentee votes are counted
- Problems with the voting machines and the companies who make them 
  - Most voting machines are written on Windows95
  - 4 vendors creating voting systems in the US, may be 2 by the end of the year.
  - Very high barrier to entry: certification costs millions $, this is actually a dis-inventive to innovate
  - Natural conflict of interest: shareholder interest collides with public interest. The companies have feduciary responsibility so the shareholder interst always trumps public interest.

The [Open Source Digital Voting Foundation](http://www.osdv.org/) is seeking to fix this “critical democracy infrastructure.” We should consider it a “digital public works project” since it is so imperative, creating transparency by using an open source approach. They are creating an endowment to support a public technology repository.

> “Sunlight is the best disinfectant”

Overview:

- Dev process: core team essential for continuity
- RFC Services: similar to IETF process
- Design Congress: state elections directors arround the country in a virtual community to drive the business requirements
- Federal Certification undertaken by the non-profit

All the software will be dual license; Public Development License &amp; Commercial Deployment License, so that it can be easily adopted by corporations. The goal is to create transparency by using an open source aproach, and actually build things that we can see, touch, and try.

Major work areas (\*=Ruby on Rails projects):

- Digital voter registration system\*
- Ballot design\*
- Ballot casting and counting
- Election management\* – back office web app for supporting the admin tasks of an election, including district data
- Operating system platform: they are building on “commodity” hardware and components, but for some customer who are seeking additional security features they are collaborating on open source hardware with Intel and AMD

A good portion of the work is Rails-based, with Pivotal Labs as a development partner. He also noted that they are in the process of putting together a “core team,” recently joined by Alec Totec, one of the original Netscape engineers (a very smart, practical guy who I had the opportunity to work with in ’95 tracking down bugs in the Netscape Plugin API when I worked on Shockwave).

After the talk, I got the chance to speak to John Sebes, OSDV CTO. He noted which projects are being implemented with RoR (see \* items above). Some of the web apps they are buiding will solve fairly simple technical problems, but they answer a huge need. The folks who run the elections generally work with very poor quality software with awkward UI that can lead to errors. For example, one might think that putting together a ballot would be straight-forward, but there are countless examples of very basic design flaws, which could be remedied by some relatively simple, effective software. He told a story of the election of Rush Holt, who was fortunately uncontested, yet the ballot made it very hard to tell the intent of the voter:

![](http://feministphilosophers.files.wordpress.com/2008/05/ballot-detail.jpg)

I can imagine all sorts of ways that ballot design in general could be improved for usability in addition to fixing outrageous bugs in the system like the one illustrated above. As a voter and open source developer, I am very excited about this project.

There are [lots of ways to get involved](http://www.osdv.org/get). Join their [new facebook group](http://www.facebook.com/group.php?gid=2434315512) to stay in touch.