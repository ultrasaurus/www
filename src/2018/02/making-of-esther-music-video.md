---
title: 'making of esther music video'
date: '2018-02-03T14:29:49-08:00'
status: publish
exported_permalink: /2018/02/making-of-esther-music-video
author: sarah
excerpt: ''
type: post
id: 6477
category:
    - general
tag: []
post_format: []
---
In 1991, the Company of Science &amp; Art created a music video for Phish. It featured richly colored pastel drawings by Scott Nybakken with just a little bit of vector art and compositing that was likely done in Photoshop 1.0.

The Esther animation (below) was recorded in real-time from Apple Macintosh IIfx running PACo a software-based animation engine developed by The Company of Science &amp; Art

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="578" loading="lazy" src="https://www.youtube.com/embed/XvVdFyiJkzY?feature=oembed" title="Original Phish Esther video by CoSA" width="770"></iframe>

At the time that this music video was made, CD-ROMs were new and Apple Macintosh computers had recently started supporting color monitors. The IIfx was the high-end of the Mac product line, and I remember that computer had 8MB of RAM, which was the most of any Mac in the office.

The sound file had to be annotated with sync points, which were produced by importing the audio into SoundEdit and then adding labels using the graphical user interface and then I think the labels could be exported as its own file (or maybe it was embedded in the sound file, I don’t remember). We used HyperCard as the original user interface for PACo, so we could experiment with new features quickly. The software would combine the labels, audio and a folder full of images, and also allow you somehow to specify transition between the images.

Images were 8-bit color, which means that each pixel was stored as a number which was an index into a color palette. Some of the color shifts in the Esther flying sequence were animated by a specific animation technique that was accomplished by rotating the color palette while leaving the pixels on the screen unchanged. This allowed for faster transitions and smoother animations than would otherwise have been possible. Even the fastest personal computer at that time was too slow to redraw the full screen at the framerate required for animation to look smooth. Notice that where elements are animated only a portion of the screen changes at any one time, such as with the church window sequence (2:07) and the spinning girl (3:40).

It was really fun to work with Scott Nybakken and John Greene who created effects that seemed to stretch beyond what was possible with the software and hardware.