---
title: 'mental models of persistence'
date: '2004-08-03T09:04:15-07:00'
status: publish
exported_permalink: /2004/08/mental-models-of-persistence
author: sarah
excerpt: ''
type: post
id: 133
category:
    - Uncategorized
tag: []
post_format: []
---
It is a challenge to introduce a new model of UI to the web. People are clearly frustrated by the standard web application experience where interaction has devolved into a series of forms. The RIA model provides an opportunity to solve this problem.

Jonathan Boutelle writes about [User Mental Models of Persistence in RIAs](http://www.jonathanboutelle.com/archives/04_06/flash-persist.html). When we have the opportunity to keep some state on the client and let people choose when to save or cancel, what should we do? Should we return to the desktop application model of requiring an explicit save?

I agree that requiring a person to save their work can cause real problems. While this is the standard approach in desktop applications, perhaps its worth re-thinking.

In the user experience of a web application, changes are more lightweight. At almost every click, you expect your changes to be saved. This is usually the case in this environment where every click implies a server round-trip. Perhaps this side effect of a bizarre user interaction model actually introduces a nice model for persistence.

The web presents different kinds of tasks than a desktop application. I’m not writing 100,000 lines of code when I use a web application. You aren’t writing a novel. We’re answering questions, filling in bits of data. There may be a lot of questions, the transaction may have complicated dependencies, and we all may be entering a googleplex of data, but this data is of a fundamentally different form than the most of the documents we create on our desktops.

Web applications are by their nature transient. We are more likely to use them for one minute than for an hour, and I would guess that we use many more different web apps from different vendors than we use desktop applications.

Perhaps a natural approach to a persistence model in this evironment is to simply make it easy as easy to change data that has been submitted as to submit it in the first place. This is possible in an HTML web application and I frequently see well-designed web apps that provide appropriate links and checkboxes to modify submitted data. Using this model of persistence, it is essential to let people easily see their “state” — where they are and what data they have entered so far. It is in this area where many web apps fail and where RIAs offer opportunities to improve the user experience. With a persistent UI on the client, it is easier to provide appropriate cues to the person using the application.