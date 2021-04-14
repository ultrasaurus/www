---
title: 'OpenLaszlo 3.0 released'
date: '2005-04-27T10:38:50-07:00'
status: publish
exported_permalink: /2005/04/openlaszlo-30-released
author: sarah
excerpt: ''
type: post
id: 165
category:
    - Uncategorized
tag: []
post_format: []
---
I am pleased to announce the official release of [OpenLaszlo 3.0](http://www.openlaszlo.org), previously known as Laszlo Presentation Server. The new name is in honor of Laszlo’s commitment to its open source platform. Since the initial release, which allowed folks to download the source in a zip file, you can now find…

– [source code access](http://openlaszlo.org/wiki/Source_Access) (in subversion)  
– open [bug tracking](http://www.openlaszlo.org/jira)  
– developer [wiki](http://openlaszlo.org/wiki/Main_Page)  
– active developer [mailing lists](http://openlaszlo.org/development/lists/)  
– [IDE4Laszlo](http://alphaworks.ibm.com/tech/ide4laszlo/)

Kudos to [Oliver](http://osteele.com/), [Tucker](http://pt.withy.org/ptalk/), [Henry](http://people.csail.mit.edu/people/hqm/), the rest of the [Laszlo](http://www.laszlosystems.com/) team, and members of [the community](http://www.openlaszlo.org/development/contributors/) for making it happen!

You can [downlaod](http://www.openlaszlo.org/download) the new release and enjoy the awesome new features. Here are my favorites:

\* SOLO (or Standalone Open Laszlo Output) deployment mode that creates a standalone file that can be used with any web server, including those that don?t allow an installation of a J2EE servlet. **No Laszlo server required.**

\* **Unicode support** for source files and datasets. The framework text components also support Unicode editing.

\* A **drawing API** that implements a subset of the [WHAT-WG](http://www.whatwg.org/specs/web-apps/current-work/#graphics) graphics API, enabling JavaScript code to create graphics on the client, on the fly.

\* **Dynamic librarie**s that can be used to significantly reduce the initial download size of an OpenLaszlo application.

\* Optimizations for Flash Player version 6, with support on over 96% of consumer browsers, and optimizations and support for the Flash Player version 7 for even faster performance under managed deployment. **Both size and speed improvements — woo hoo!**

\* Client text optimizations, allowing the use of embedded fonts for total visual control, or HTML-style client fonts for **smaller application size and faster text editing**.

\* Better HTML integration through a **resizable canvas** allowing OpenLaszlo applications to be sized proportionally to the enclosing HTML page. This is really nice and well integrated — you can specify constraints like width=”${canvas.width-20}”.

\* **Better JavaScript integration** with functions in OpenLaszlo applications making calls to JavaScript in the surrounding HTML page.

\* Better navigation capabilities as OpenLaszlo applications can intercept the **browser ?back? button** and use it to move around among program states. Simple API to control history state — see LzHistory for details.

\* Laszlo Systems is available to help developers who are using OpenLaszlo via [hands-on training courses, technical support, webinars, and consulting](http://www.laszlosystems.com/services) to help developers over the periodic hurdles that come up when using a new platform. **Laszlo trainings are awesome — you should sign up.**

If you haven’t already, download [OpenLaszlo 3.0](http://www.openlaszlo.org/download)!