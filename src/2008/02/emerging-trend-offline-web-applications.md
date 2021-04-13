---
title: 'emerging trend: offline web applications'
date: '2008-02-23T10:28:01-08:00'
status: publish
permalink: /2008/02/emerging-trend-offline-web-applications
author: sarah
excerpt: ''
type: post
id: 357
category:
    - Uncategorized
tag: []
post_format: []
---
Ryan Stewart [writes](http://blog.digitalbackcountry.com/?p=1286) about Adobe AIR’s mention in MIT Technology Review’s [top 10 emerging technology trends](http://www.technologyreview.com/read_article.aspx?ch=specialsections&sc=emerging08&id=20245) for 2008: “Context: Adobe will release AIR early this year; companies such as eBay, AOL, and Anthropologie have built applications using early versions of the software. Google is working on a competing platform called Gears.” (via [Ron Jeffries](http://blog.eronj.com/))

The trend is what is interesting. I think Gears has a more compelling approach. Adobe is first to market with a fully featured, yet still beta offering. Google Gears just released a .2 release. You have to really dig in the Gears site to get a sense of where they are going. They are in real need of wiki maintainer with a sadly out of date \[now updated\] [roadmap](http://code.google.com/p/google-gears/wiki/GearsRoadmap), but lurking on the email lists and getting deeper into the wiki there are some interesting clues that these folks are headed in the right direction.

“The [Gears mission](http://code.google.com/p/google-gears/wiki/ContributingToGears) is to add new capabilities to web browsers, enabling developers to create better applications.”

They have some interesting features in the works:  
\* [Desktop API](http://code.google.com/apis/gears/upcoming/api_desktop.html) is in in an “upcoming release.” (You have to build from source to try it out.) Instead of actually downloading an executable, this creates a desktop shortcut. You can have an icon that you double-click to go directly to your web application which has the same user experience as when you are online — bookmark or desktop application are just two ways to navigate to the same thing.  
\* [Notification API](http://code.google.com/p/google-gears/wiki/NotificationAPI) is a pretty new proposal, but an indication that the community is starting to plan how to integrate with native OS notifications, a task bar icon, etc.

Of course, Adobe AIR already has those features, plus drag-and-drop from the desktop, which is a feature web applications desperately need. It overcomes a major limitation of Flash by embedding the [WebKit](http://webkit.org/) browser, which is a smart move by Adobe. However, what most Adobe fans tout as a strength of AIR (that it is actually a desktop application), I see as a weakness. It borrows from the online/offline model that I was working on with Director and Shockwave in the late 90’s where the user experience and technical architecture is more like a client-server app than a webapp.

I’ve observed in focus groups and usability tests that most regular folks don’t know the difference between a web page and a desktop application. People are focused on the task at hand, getting the job done and are annoyed by arbitrary changes in how they get to what they need. Of course, they adapt. People don’t actually expect software to be particularly helpful or intuitive. Nonetheless, software designers and developers keep trying to get it right.

As people are more often connected, intermittently connected, and more reliant on connected tools for business notifications and communication, there is an increased need for web applications to have a desktop presence. I shouldn’t have to go to the ebay website or check my mail to find out whether I’ve won my latest bid. I want to be able to read my mail on an airplane AND in an internet cafe when I’ve left my computer at home. The gears approach is attractive because it will enable us to craft an experience which is not arbitrarily different for on- and offline experiences of the same application.

I’ve been following this tech just by reading for a few months, but this week, I spent a little time getting my feet wet. I installed two applications: [Ebay Desktop](http://desktop.ebay.com/) with AIR and [Google Reader](http://www.google.com/reader) with Gears. Please remember, that all of this stuff is pre-release software, so it is still subject to change.

Ebay Desktop and Adobe AIR
--------------------------

Installing Ebay Desktop with Adobe AIR beta 3, the first screens prompting me to install the new version of Flash were really confusing. Even after I installed Flash, it still told me to install Flash, so I still don’t know if I really needed that step. Then I had to navigate back to the original page manually after installing Flash and AIR. I expect that the first part of this awkwardness could have been better implemented on the ebay site and may not be a fault of the AIR technology, but the latter series of multiple progress bars and dialog boxes looks unavoidable. All told the install experience was over 10 minutes.

<div id="__ss_278882" style="width:425px;text-align:left"><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">[![SlideShare](http://static.slideshare.net/swf/logo_embd.png)](http://www.slideshare.net/?src=embed) | [View](http://www.slideshare.net/sarah.allen/ebay-desktop-adobe-air-install?src=embed "View 'Ebay Desktop Adobe AIR Install' on SlideShare") | [Upload your own](http://www.slideshare.net/upload?src=embed)</div></div>Remember the Milk and Google Gears
----------------------------------

\[UPDATE: my initial post was not an apples-to-apples comparison since it was an upgrade, I’ve changed this to reflect an initial install experience\]

Remember the Milk has really done a nice job with this. The installation took just a few minutes. After setting it up initially, I could go back and forth between online and offline without really thinking about it.

<div id="__ss_279409" style="width:425px;text-align:left"><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">[![SlideShare](http://static.slideshare.net/swf/logo_embd.png)](http://www.slideshare.net/?src=embed) | [View](http://www.slideshare.net/sarah.allen/remember-the-milk-offline-experience-with-google-gears?src=embed "View 'Remember The Milk Offline Experience with Google Gears' on SlideShare") | [Upload your own](http://www.slideshare.net/upload?src=embed)</div></div>The only momentary glitch was with the stupid IE Popup blocker which reloads the page. I wonder if there is anyway around that? I wrote about running into this issue on the [gowebtop blog](http://gowebtop.com/blog/2008/01/23/29/#popup) but I wonder in this case if there would be a way to create an in-page install to avoid this hiccup.

Technology Options for Offline Webapps
--------------------------------------

As a final note, Gears and AIR aren’t the only two players here, just the most talked about and seeming front-runners. Of others, I’ve collected the list below. My friend Max just told me about XULRunner and I haven’t had a chance to take a look at that yet.

**HTML solutions**  
\* [Google Gears](http://gears.google.com/) (open source, New BSD License, 0.2 release)  
\* [XULRunner ](http://developer.mozilla.org/en/docs/XULRunner)(open source, MPL, 1.7)

**Flash Wrappers**  
\* [Adobe AIR](http://labs.adobe.com/technologies/air/) (proprietary, beta)  
\* [Zinc](http://www.multidmedia.com/)  
\* [SWFStudio](http://www.northcode.com/)  
\* [SWFKit](http://www.swfkit.com/)  
\* [Jugglor](http://www.flashjester.com/)  
\* [Flash Desktops](http://www.trombettworks.com/)  
\* [mProjector](http://www.screentime.com/software/mprojector/)  
\* [ScreenWeaver ](http://screenweaver.org/)(LGPL)  
…