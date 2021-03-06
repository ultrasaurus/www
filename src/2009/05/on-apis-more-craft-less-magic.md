---
title: 'on APIs: more craft, less magic'
date: '2009-05-06T09:00:00-07:00'
status: publish
exported_permalink: /2009/05/on-apis-more-craft-less-magic
author: sarah
excerpt: ''
type: post
id: 1254
category:
    - general
tag: []
post_format: []
---
I’ve spent a lot of years creating developer tools. Even for the software that did not target developers, there were always APIs for other vendors to create extensions or to use internally between different modules. One the interview questions I like is “have you ever designed an API?” followed by “what do you (would you) consider in designing an API?” There’s typically a trade-off between flexibility and getting the job done concisely and with a great engineer this usually turns into an interesting conversation.

I’ve been using Rails for a while now and one of the things that seems awesome at first is the breathtaking speed at which you can create a basic web application with full XML and JSON APIs. For someone who doesn’t love picking which XML parser to use and digging through a DOM just to hook the client and server together, this is a beautiful thing. However, I’ve noted a peculiar absence in conventions for API design, and a void in tools for testing and documentation. (I am relatively new to Rails, so if I’ve missed some obvious resources, please let me know.)

Rails seems to assume that you want to expose your database object model transparently through your API. In my experience, this is rarely what you want to do. In fact, it is a crazy way to live. It kind of assumes that you have just one engineer that writes the client code and the server code and updates them both all the time. This makes complete sense for HTML which is closely integrated with the Rails model and controller code, but not when you have multiple code bases in various languages which are using the web services.

Instead, I typically think about the use cases that the client software needs and craft an API around that. Usually this is a small subset of the internal objects and methods. Also, in writing client-server software (which is what you are doing with Ajax, Flash or a mobile app), you want to keep the number of network requests small. For common use cases, it is a good idea to bundle calls together. There are a lot of approaches to this, and I’m currently looking at the Rails 2.3 nested model feature, but I think that solves just one common use case.

The other challenge with developing APIs is that over time your software changes… maybe your first version was wildly successful and now you have thousands (or millions) of people who have installed your code on their phone (or desktop). Now when you refactor your core models to improve performance and don’t change any behavior, you certainly don’t want to break everyone’s app or make them download new software. Even if you add features, you probably want the old versions of the app to keep working while you encourage people to download your new, better thing. There are a lot of well-used approaches for fixing this too.

I’d hate to see CORBA added to Rails, but this seems like an area where conventions (and maybe a little shared code) would be valuable.