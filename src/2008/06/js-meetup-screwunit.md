---
title: 'js meetup: ScrewUnit'
date: '2008-06-06T06:27:22-07:00'
status: publish
exported_permalink: /2008/06/js-meetup-screwunit
author: sarah
excerpt: ''
type: post
id: 387
category:
    - Uncategorized
tag: []
post_format: []
---
Nick demonstrated ScrewUnit at the [JSMeetup](http://javascript.meetup.com/4/calendar/7922755/?a=cr1p_grp) last night. My notes:

- behavior-driven development, particularly popular in the Ruby world with the RSPEC framework
- organize your tests, share setup
- global befores and afters let you effectively test the DOM
- nested describes, nested example groups in RSPEC

What about continuous integration? there’s a ScrewUnit server, navigate URLs – only run those in that directory. There are callbacks when a suite ends/begins — integrated into CruiseControl

on GIT hub, MIT license

support for async libs? unsolved problems, most people at the company stub out async.

What about user interactions? serious attention on event and DOM testing. Nothing in particular to facilitate that except before and after. JQuery is a good approach…