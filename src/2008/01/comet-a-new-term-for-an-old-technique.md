---
title: 'Comet: a new term for an old technique'
date: '2008-01-27T10:02:52-08:00'
status: publish
exported_permalink: /2008/01/comet-a-new-term-for-an-old-technique
author: sarah
excerpt: ''
type: post
id: 349
category:
    - Uncategorized
tag: []
post_format: []
---
The term ‘Comet’ was coined by Alex Russell, of [Dojo](http://dojotoolkit.org/) fame, in his [post](http://alex.dojotoolkit.org/?p=545): “An old web technology is slowly being resurrected from the depths of history. Browser features that have gone untouched for years are once again being employed to bring better responsiveness to UIs. Servers are learning to cope with a new way of doing things… Comet applications can deliver data to the client at any time, not only in response to user input. The data is delivered over a single, previously-opened connection. This approach reduces the latency for data delivery significantly.” Alex’s post has a nice picture. There is also a nice detailed technical discussion [here](http://ajaxpatterns.org/HTTP_Streaming) (from one of the comments).

I’m about as stunned as when Jesse James Garrett coined the term Ajax. Here is something that people have been doing for years; it is not a single technique, there is no spec, no RFC, instead it is a name for a programming method. I guess I’d feel better if it was called a “Comet pattern” and discussed purely amongst the geeks. However, like Ajax, Comet has become a marketing term, where it is easily confused with words like Web, which is backed by the precision of the HTTP spec, or email, which is clearly defined by SMTP, MIME, POP and IMAP.

Nevertheless, I suppose it is useful to have a catchy one-word name for common functionality. Just as the [gang-of-four](http://en.wikipedia.org/wiki/Design_Patterns) named common software methodologies, they called [Design Patterns](http://www.amazon.com/exec/obidos/redirect?link_code=as2&path=ASIN/0201633612&tag=ultrasaurus-20&camp=1789&creative=9325), or GUI elements (windows, menus, tabs) can have significantly different implementations and detailed capabilities, Comet has no underlying protocol or specification; it describes the capability of creating a socket-like connection over HTTP, of layering multiple requests and multiple responses over a single request-response of an HTTP connection.

In the late 90’s and early 2000’s, we called this “HTTP [tunnelling](http://en.wikipedia.org/wiki/Tunneling_protocol).” It was common for streaming and messaging applications to apply these techniques. (I led the Flash Media Server project when [RTMPT](http://en.wikipedia.org/wiki/RTMPT) was created.) These were native code applications which could implement a socket connection; however, most firewalls can be configured to prevent this. Most corporate or home firewalls will allow any traffic over port 80, but some actually look at the data going over the wire and restrict it to that which contains HTTP headers. Some firewalls go so far as to prohibit long-lived HTTP sessions, ensuring that each request ends before the response is returned and that each response has a limited length. Therefore, correctly implemented Comet applications do need to poll, in order to be compatible with all firewalls (a minor correction to Alex’s post).

As Alex reports, it is great to see these techniques becoming more ubiquitous, with even more adoption by the open source technologies that many of us rely on. Tomcat 6 is offering comet as part of their [advanced i/o](http://tomcat.apache.org/tomcat-6.0-doc/aio.html) — it’s not quite production ready, but it is getting there. Jetty is adopting [cometd](http://cometd.com/), which ties it’s implementation to a specific Javascript messaging model — fine if you are doing pure browser stuff but cumbersome to tie into Flash or a native app. It’s still early days, but open source adoption is an indicator that over time these techniques will become easier to integrate into end-user applications. I look forward to seeing more web applications that offer responsive interactions, multi-party support, and data notifications.