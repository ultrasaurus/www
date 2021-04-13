---
title: 'Yahoo&#8217;s BrowserPlus sneek peek'
date: '2008-06-07T20:12:10-07:00'
status: publish
permalink: /2008/06/yahoos-browserplus-sneek-peek
author: sarah
excerpt: ''
type: post
id: 388
category:
    - Uncategorized
tag: []
post_format: []
---
I checked out Yahoo’s sneak peek of [BrowserPlus](http://browserplus.yahoo.com/) this morning — looks like there is some interesting stuff there. It think they have a good approach by getting feedback from people using apps before they open up the APIs to developers. I have always believed that to get the UI right, you need the user experience to drive the APIs not the other way round.

**Key Features**  
\* Drag-and-drop from the desktop to the browser (my favorite!)  
\* Upload to FlickR  
\* Desktop Notifier (integrating with Growl on the Mac and Snarl on Windows)  
\* Image editing: rotate, crop, and effects: ‘sepia’, ‘swirl’, ‘solarize’, ‘oil\_paint’, and ‘grayscale’.  
\* Text-to-Speech  
\* PStore (local storage: I wonder what the limit is here)

**Geek Features**  
\* Ruby Interpreter  
\* JSONRequest  
\* IRC Client

The [API documentation](http://browserplus.yahoo.com/services/) is available, but right now you can only use it if you work for Yahoo. However, with the documentation out there, including a slick doc browser, they seem pretty serious about opening this up to external developers.

BrowserPlus also has a plugin architecture, so the features can be updated without restarting the browser or even refreshing the page! This will put them in a very good position when it comes to adoption, but the way they present the plugins is a bit odd from an end user perspective. I can dig allowing Yahoo to install an image editor, but do I really care that the app I’m using is written in Ruby? I’ve got a little security geek background and I don’t even understand implications of allowing a “RubyInterpreter” to be installed — is it sandboxed? does it allow file system access? This is weird territory from a usability perspective. How’s a normal person to tell what’s safe or not? Hard to tell what the model is here… am I trusting the site or trusting the software vendor? Right now they are the same for BrowserPlus, but they’ll need to clarify this before they open it up

**Installation Experience**  
Continuing with my series evaluating the initial experience for [Adobe Air and Gears](https://www.ultrasaurus.com/sarahblog/archives/000424.html), here’s a click-through slide show of getting started with BrowserPlus:

<div id="__ss_453927" style="width:425px;text-align:left"><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">[![SlideShare](http://static.slideshare.net/swf/logo_embd.png)](http://www.slideshare.net/?src=embed) | [View](http://www.slideshare.net/sarah.allen/browswerplus-install?src=embed "View BrowswerPlus Install on SlideShare") | [Upload your own](http://www.slideshare.net/upload?src=embed)</div></div><small>Privacy Policy</small>

BrowserPlus may gather, store and transmit to Yahoo! the following anonymous information about your usage of the BrowserPlus for diagnostic and software improvement purposes:  
o Your device’s platform (i.e., osx, win 32, XP).  
o The version number of BrowserPlus that you have installed.  
o A unique identifier assigned to your installation of BrowserPlus. Yahoo! will NOT associate this unique identifier, your browsing activity or the web sites you visit to you or any of your personally identifiable information.

From time to time, Yahoo! may automatically download the latest version of BrowserPlus and notify you when it’s ready to install. You will have the choice to cancel or proceed with the installation.

Certain internet sites you visit may request that you download a corelet that will plug into BrowserPlus and help to optimize your online experience while on that site. You will have the choice to cancel or proceed with the installation.

To learn more, please read our BrowserPlus privacy information at http://info.yahoo.com/privacy/us/yahoo/browserplus.

Certain sites may request the you download a **corelet**? Are you kidding me? How about you just use an English work like “extension” or even to quasi-english “plugin” — I think it just confuses people to create new language for an old concept.

**Conclusion**  
BrowserPlus is a promising new contender in this space with a new angle. Even though AIR and Gears have been out (at least for developers) for a while, there is no clear winner and I don’t expect that to be decided for a while yet. BrowserPlus worth watching. If you are going to check out one demo, I’d recommend the [flickr uploadr](http://browserplus.yahoo.com/demos/uploadr/).