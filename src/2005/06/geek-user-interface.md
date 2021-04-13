---
title: 'Geek User Interface'
date: '2005-06-18T11:01:02-07:00'
status: publish
permalink: /2005/06/geek-user-interface
author: sarah
excerpt: ''
type: post
id: 169
category:
    - Uncategorized
tag: []
post_format: []
---
When I started at [Laszlo](http://www.laszlosystems.com) over two years ago, there were two kinds of engineers at the company, those who used emacs and those who used vi — roughly divided by coasts, with emacs in the east and vi on the left. I had thought that no one would use vi by choice, that it was only used when people were stuck with no other option, remotely logged into a server. I had learned to use vi a bit in college. Just enough to hobble around: dd, d$, cw, :q, :w, :q!. I was horrified. Who thought up these bizarre key bindings? I left college for jobs writing desktop applications, secure in my certainty that this appalling example of software engineering would surely die a quiet death, drifting into historical obscurity.

Lo and behold! vi was alive and well in San Francisco, installed on desktops where a perfectly usable GUI editor might be found. I was in for a bit of culture shock, and it ran in both directions. [Adam Wolff](http://www.laszlosystems.com/~adam/blog/) asked in my interview what my favorite editor was. I told him I didn’t have one. He was taken aback, but I had been working for over ten years in an environment where my choice of compiler dictated the editor I used — from Think C in 1990 to Visual C++ in 2002. I was impressed with Adam, but I couldn’t believe that someone so apparently intelligent and savvy about user interface design and development could possible choose vi as an editor. I took the job, but remained puzzled.

Seeing Adam in action, my perspective on vi was forever changed. At Laszlo, the engineers who give presentations have this knack of illustrating the [LZX language](http://www.laszlosystems.com/lps/laszlo-in-ten-minutes/) by writing an application from scratch starting with a blank page. It is impressive and fun to watch. When Adam does this it is performance art. His hands never leave the keyboard. His attention is focused on the audience and the task at hand. Using vi’s folding features, he can keep key parts of the application on screen, even in a small window. Watching him use vi, it looked easy and fun. I saw that there was method behind the madness of the seemingly bizarre key bindings. It is geared to optimizing your finger positions on a good old qwerty keyboard.

Despite these apparent benefits, I opted out of that learning curve. Instead I settled into happy coding for with IDEA from IntelliJ, until a couple of months ago when my world slowed to a crawl. I sadly discovered that my IBM laptop had misplaced half its RAM. I could no longer run tomcat, Firefox, IE, Thunderbird, and IDEA and get anything done. While I awaited a replacement computer, I discovered that if I ran tomcat, Firefox, and vi — just the bare necessities, I would stay just under 512 MB of RAM. Even though I was more proficient in Notepad and I had deadlines looming, I settled in for a steep learning curve.

I am fortunate to be immersed in a particular flavor of geek culture where people enjoy sharing know-how. In fact, the vi-o-philes in the offices were downright delighted to help me configure my vimrc or teach me new commands while coding together. [Scott Evans](http://www.antisleep.com/) even bought me my very own [vi reference mug](http://www.cafepress.com/shop/geeks/browse/Ne-25_N-3807_bt-2_pv-geekcheat.11507711).

As it turns out, there are patterns in the key combinations that make it so that once you learn all the variations on one command, you know how to use a whole lot of them. So, with my knowledge of dd (delete line), d$ (delete to the end of line), cw (change word), I learned that dw means delete word. Then when I learned about yy (to ‘yank’ a line into a buffer to later ‘put’ with p), I automatically know yw and y$. When I learned how to delete 3 lines with 3D, I also learned what 3Y means. Also, vi has gotten better since I was in school (I use [gvim](http://www.vim.org/) on Windows which has menus and even lets you use the mouse!)

![](http://www.bootstrap.org/chronicle/pix/t20.jpg)This is Geek User Interface design, as opposed to the “human” interface design of the Graphical User Interface. It rewards people who are pretty good at remembering arbitrary, but useful sequences of letters.

This experience reminds me of [Doug Engelbart](http://www.bootstrap.org/) and his bicycle analogy. “The tricycle may be easier to learn and use, but it is hard work to travel even a short distance. Riding a bicycle calls for considerably more skill, with bumps and bruises expected as one learns, but the effort-to-performance ratio is dramatically higher. The high-performance knowledge workers of the future, as perceived by Engelbart, are expected to be very skillful.” ([2F1B](http://www.bootstrap.org/chronicle/pix/pix.html#2F1B))

So I’ve got a new machine, which is has enough RAM for a GUI editor, but I’m still using vi. I don’t know whether I’ll stick with it, but I’m pleased that the common commands are now etched into my muscle memory. If I decide to leave vi for a while, I can always go back, like riding a bicycle :) Sometimes I miss an interactive tree-view to navigate XML hierarchy. I find that grep is no match for a really nice multi-file search UI, but I would miss the simplicity of ‘/’ for searching within a file. I plan to install Eclipse with the latest version of [IDE4Laszlo](http://www.alphaworks.ibm.com/tech/ide4laszlo) and give that a whirl. We’ll see.