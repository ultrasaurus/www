---
title: 'holy disappearing blog entries'
date: '2005-01-04T02:45:50-08:00'
status: publish
exported_permalink: /2005/01/holy-disappearing-blog-entries
author: sarah
excerpt: ''
type: post
id: 151
category:
    - Uncategorized
tag: []
post_format: []
---
I consider myself a fairly techno-savvy kinda gal. Most of the people on the internet have used software with my code in it. I can debug with the best of them. However, I really do like it when stuff just works.

I’ve loved moveable type and the whole notion of blogging. So what if I could code a whole web site in raw HTML? I could also type in binary, but who would want to? Hey, give me a simple form to fill out and I’ll find some spare minutes in my week to collect and publish my thoughts. I don’t need to make plans or data structures or any decision beyond which words to put into the box.

Tonight my lackadaisical attitude caught up with me. I was writing a (different) blog entry when I was suddenly confronted by:

 Saving entry failed: Can’t open file: ‘mt\_entry.MYD’. (errno: 145)

Eek! I rushed right back to copy and paste my latest words into a safe haven, then proceeded to investigate. Now “Sarah Allen’s Weblog Editing Menu” reports no entries, not zero, mind you, its:

 Entries: Comments: 192 Authors: 1

It’s like the entries never even showed up to play. The comments are winning and the author has surely lost. A quick glance at www.ultrasaurus.com reveals a completely blank page — I had to view source to be sure:

 &lt;html&gt;&lt;body&gt;&lt;/body&gt;&lt;/html&gt;

My life flashes before my eyes. All those moments when I could have backed up my data, yet didn’t. Being able to write software makes me no more eager to back up my data than being good at algebra makes me want to balance my checkbook. It’s worse than dust bunnies in the corners, dishes in the sink, or broken windows. You don’t ever see it, until its too late.

Belatedly I back up my files and consider a future perl script to suck all those files back into a database if the situation turns out to be unrecoverable. While the files download, I berate myself for not having upgraded movable type. I dig thru Media Temple’s nifty control panel and realize that I haven’t looked at this MySQL database since I set it up two years ago. I don’t remember how to do any of this. I’ve forgotten the passwords. I notice that I’ve somehow managed to chew up almost all of my allotted disk space. That can’t be good. After a little housecleaning, the home page is still blank.

I search google but the error string yields zero results and all my natural language descriptions generate helpful solutions for other problems. I finally give up and describe my failure in detail in the movable type support forum.

This leads me to my Eliza moment when I reproduce the error above and decide to search for part of the string. I discover dozens of helpful tips on how to repair exactly this MySQL problem using PHPmyAdmin which was thoughtfully provided by my ISP. I dig up the password and have to consult three different google results in order to find the exact steps through this challenging GUI:  
1\) click the check box next to the offending table  
2\) look all the way down to the bottom where you’ll see a drop-down menu  
3\) choose repair

I repair two tables that had reported that they were ‘IN USE’ and all is well. I reply to my very own forum posting at movable type and resolve to rotate my log files and clear out my mailspool… tomorrow.