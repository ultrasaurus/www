---
title: 'declarative web GUI'
date: '2003-11-19T10:10:20-08:00'
status: publish
exported_permalink: /2003/11/declarative-web-gui
author: sarah
excerpt: ''
type: post
id: 78
category:
    - Uncategorized
tag: []
post_format: []
---
*For thousands of years, philosophers and scientists have attempted to explain the cosmos in terms of dual opposing but coexistent principles: good and evil, yin and yang, matter and energy, mind and body, waves and particles, and, of course, programming code and markup languages.*

Programming and markup currently coexist in an uneasy truce. In theory, programming languages can do anything the computer is capable of, but they’re often clunky for the job of laying out text, images, and controls in a simple visual interface. Markup is great for defining highly textured pages of text and images that adapt to different screen sizes and environments, but is hopelessly inept when it comes time to interact with the user in any nontrivial way. — [Code Name Avalon, MSDN](http://msdn.microsoft.com/longhorn/default.aspx?pull=/msdnmag/issues/04/01/Avalon/default.aspx)

Declarative programming has been actively used for web application since the early years of the web. PHP and CFML enabled easy access to server-side logic and services by encapsulating them in tags that felt like HTML.

Initially, on the client-side, Javascript provided the mechanics that enabled DHTML to drive richer experiences. Although its hard to separate the potential effectiveness of this model from the headaches inherent in the lack of cross-platform support that fell out of the browser wars of the late ’90s, the later emergence of declarative GUI shows more potential for providing the next generation web experience.

[XUL](http://www.xulplanet.com/) was probably first on the scene. It may at first look like HTML, PHP, JSP, or CFML markup because of all the angle brackets, but the tags represent more powerful objects and ones that people can interact with.

LZX from [Laszlo Systems](http://www.laszlosystems.com/) is the declarative web GUI language from which I draw my conclusions. I’ve developed desktop application UI in C/C++, then web applications in Shockwave and Flash, and even some for plain-old-HTML. I imagine a new user experience for the web that leverages lessons learned from desktop UI and “multimedia” yet is appropriately evolved for this new space.

It is neat to see a plethora of emerging technologies using this kind of approach. At the PDC, Microsoft unveiled [XAML](http://msdn.microsoft.com/longhorn/default.aspx?pull=/msdnmag/issues/04/01/Avalon/default.aspx) (to be released with Longhorn in 2006) and this week Macromedia formalized its [Flex](http://www.macromedia.com/macromedia/proom/pr/2003/introducing_flex.html) stratgey (the previously code-named Royale product to be released mid-2004). In addition to [XUL](http://www.xulplanet.com/) from Mozilla and [LZX](http://www.laszlosystems.com/lps/lzxplorer2/lzxplorer.htm) from Laszlo that are already released, there’s [XWT](http://www.xwt.org) and [similar tech](http://www.xwt.org/faq.html#similar). One can only hope that the innovations of language and platform will drive a the development of a better human experience of the world wide web.