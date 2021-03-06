---
title: debugging
date: '2005-01-09T17:56:06-08:00'
status: publish
exported_permalink: /2005/01/debugging
author: sarah
excerpt: ''
type: post
id: 152
category:
    - Uncategorized
tag: []
post_format: []
---
Back at my day job last week, I was faced once again with a mystery bug. This bug seemed to defy logic and the physical laws of the universe. The whole system behaved correctly, except for the undesired behavior.

I was tired. It really felt like someone else’s bug. It would take me a half hour just to write an isolated test case. (I could hear [Kent Beck’s voice](http://www.unikron.com/agitar1/) reminding me that developer testing really does save time.) Everyone on my team is supposed to write unit tests. Of course there wasn’t one for this particular unit. I considered chastising the developer in question and investigating the bug another day. Unfortunately usability testing was scheduled for the next day, and this bug was …ahem.. bugging me, and I felt it would affect the usability of the app.

A long time ago when I was working on a solo project and dispairing of ever finding a particular bug. I had been hunting for this bug on-and-off for days. It was a large, not particularly wonderful code base that I had adopted from an acquistion. There really was no one at the company who knew much about it. I was alone in my SF office and I was at my wits end. I remember calling my long-time friend and co-worker David Simons and asking “what if I never find this bug?” and he asked me “Has there ever been a bug you haven’t fixed?” Well sure, we always have to defer some bugs. “No,” he said, “one that had to be fixed.” Begrudgingly, I admitted, that I had actually fixed every bug I had ever set out to find. I hung up the phone, took a deep breath, and hunted it down.

At times like this when debugging seems bleak and hopeless I always ask myself that question and I reflected that this bug is not likely to be any harder to find than the most difficult bug I’ve ever fixed. In fact, this bug was likely to not even rank my top ten.

Also for this bug I did have a good clue. A colleague of mine had taken a look at it in the late afternoon and had discovered something I hadn’t noticed. I instrumented the code a bit and saw the same odd behavior.

I spent hours examining the state of run-time, puzzling over variables that did not have the appropriate value. I kept thinking I had discovered that cause of the bug, but my code changes had no effect on the sympton. I had found 8 different variables that proved that the state of the app is disastrously incorrect. After while, I noticed that the symptoms had changed from my original observations. The app was more broken that it was initially. I removed my instrumentation and voila the bug was fixed. I had actually fixed this bug an hour before, but I had introduced another problem with my debugging statements.

Aha! A Heisenbug, so called from the Heisenberg uncertainty principle. From quantum mechanics: “The more precisely the position is determined, the less precisely the momentum is known.” And more generally, Heisenberg introduced the notion that when you measure something, you change its behvior.

I find that the more experience I have debugging software the more I see patterns in the kinds of problems I find. Most of the patterns are not so delightfully named as the Heisenbug. I wonder… does anyone else have good names for common bugs?