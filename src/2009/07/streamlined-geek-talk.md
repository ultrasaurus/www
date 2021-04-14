---
title: 'streamlined geek talk'
date: '2009-07-16T05:01:07-07:00'
status: publish
exported_permalink: /2009/07/streamlined-geek-talk
author: sarah
excerpt: ''
type: post
id: 1807
category:
    - general
tag: []
post_format: []
---
Last night [Wolfram Arnold](http://www.rubyfocus.biz/) and I gave a talk at the SF Ruby Meetup about a recent collaboration where we created specs, documentation and tests using cucumber to streamline workflow and communication between client and server engineers.

It was Wolf’s idea to start the talk with a role play of the real-life situation that we were faced with at the outset of the project. He convinced me to do it as improv, which was a lot of fun, but for those who missed here’s the script that I had written out earlier:

> **Biz Guy** (ring): Hey Pat, this is Charlie. I’ve got an investor pitch in the morning and I just tried the app on my Nokia phone and I’m no seeing search results any more. Can you look into it?  
> **Client Engineer**: I haven’t touched the code in months. It must be the server code.
> 
> **Biz Guy** (ring): Hi Sarah, this is Charlie. The mobile app isn’t working on my Nokia phone and Tony says he hasn’t changed the code in months. You said that server engineer you hired was really good, maybe he could fix it by tomorrow.  
> **Manager**: hmmm… I’ll check.
> 
> **Manager** (ring): Hey Wolf, this is Sarah. Did you make any changes lately that could have affected the mobile client?  
> **Server Engineer**: No… none of the APIs have changed and all of the tests pass. In fact, the mobile app demo on the website works and that uses the same APIs, so it must be a client problem.
> 
> **Manager** (ring): Hey Pat, this is Sarah. Glen told me the mobile app isn’t working, but the demo on the web does work. I understand they use the same APIs, so I’m guess the issue is in the mobile client code.  
> **Client Engineer**: Actually, the mobile app uses a slightly different authentication than the app on the web  
> **Manager**: Oh really, is that documented?  
> **Client Engineer**: well, there is detailed documentation of the platform SDK that the mobile phone doesn’t support http header responses so the auth token needs to be sent back in the post body  
> **Manager**: I see. Unfortunately, our server engineer isn’t actually familiar with the mobile platform SDK.

This is a critical problem in my experience and a very common one. Whenever you have API documentation, it is usually incomplete, inaccurate or both, often despite the best intentions of everyone involved. In this case, we solved the problem of documenting and testing XML APIs by writing cucumber scenarios which serve as both the documentation and tests. By making the documentation executable with published results in a continuous integration system, we always have up to date documentation.

- Cucumber BDD framework: <http://cukes.info/> and[ http://wiki.github.com/aslakhellesoy/cucumber](http://wiki.github.com/aslakhellesoy/cucumber) Webrat (gem)
- [Using DB fixtures in cucumber](http://wiki.github.com/aslakhellesoy/cucumber/fixtures)
- Using XML fixtures to compare server response: [xmlsubsetmatcher library](http://github.com/mightyverse/xml_subset_matcher/tree/master) (there’s a gem spec in the github repo, but it is not yet working as a gem)
- Example: [http://github.com/mightyverse/cucumber\_xml](http://github.com/mightyverse/cucumber_xml/tree/master)

The slides from the talk are [posted on slideshare](http://www.slideshare.net/sarah.allen/streamlined-geek-talk-1727826):

<div id="__ss_1727826" style="width: 425px;text-align: left">[Streamlined Geek Talk](http://www.slideshare.net/sarah.allen/streamlined-geek-talk-1727826 "Streamlined Geek Talk")<div style="font-size: 11px;font-family: tahoma,arial;height: 26px;padding-top: 2px">View more [presentations](http://www.slideshare.net/) from [Sarah Allen](http://www.slideshare.net/sarah.allen).</div></div>