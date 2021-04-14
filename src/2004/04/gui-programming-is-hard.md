---
title: 'GUI Programming is Hard'
date: '2004-04-06T03:47:49-07:00'
status: publish
exported_permalink: /2004/04/gui-programming-is-hard
author: sarah
excerpt: ''
type: post
id: 115
category:
    - Uncategorized
tag: []
post_format: []
---
Yeah, but so is anything worth doing.

Humans are so finicky — they want everything done for them, but still have all the control. What’s up with that? We’re all waiting for that semantic network to lead us into internet nirvana. With a WSDL description for enough SOAP web services and we can write software that will do anything you want, but … um… you want it to be useful without a 3 day training session or your very own geek to assist you? uh…

I enjoyed [Eric Burke’s rant](http://www.oreillynet.com/pub/wlg/4649) (via [Evan Williams](http://www.evhead.com/archives/2004_04_01_archive.asp#108114217841672689)) and a few more points from [HMK](http://www.extragroup.de/weblog/hmk/archives/000687.html). I think it’s true that a good GUI just looks so easy that some folks don’t value it. It’s like a movie soundtrack. To most folks when it’s good, the movie just seems like a better movie, and when it’s bad, the plot drags and the characters seem to lack depth.

Here’s a few more points from my list:

\* Good GUI involves interaction design. You can’t draw a picture or a flow chart of it. To know if it’s going to work you have to prototype it or even fully implement some of it.

\* GUI seems more subjective than it is. Unlike a crash or some part of a program that gives an incorrect result, a usability bug can be hard to classify. I’ve known many folks who would say that if it’s just pixels on the screen, the bug is cosmetic, and therefore unimportant. A good UI engineer will classify it as simply “broken.” If the pixels are in wrong place, the end user loses confidence and the UI stops working.

\* Human interfaces require soft edges. Whether graphical or not, any thing that interacts with humans must be tolerant of mistakes. Unlike machine-to-machine interaction which can be programmed to stay within safe boundaries, humans cannot be expected to do so. There can’t be an edge condition which causes you to fall of a virtual cliff. Interfaces which are not resilient to unexpected user behavior often fail to be useful.