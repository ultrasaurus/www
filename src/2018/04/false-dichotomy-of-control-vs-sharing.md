---
title: 'false dichotomy of control vs sharing'
date: '2018-04-20T05:57:24-07:00'
status: publish
permalink: /2018/04/false-dichotomy-of-control-vs-sharing
author: sarah
excerpt: ''
type: post
id: 6589
category:
    - general
tag: []
post_format: []
---
Email is the killer app of the Internet. Amidst many sharing and collaboration applications and services, most of us frequently fall back to email. Marc Stiegler suggests that email often “just works better”. Why is this?

Digital communication is fast across distances and allows access to incredible volumes of information, yet digital access controls typically force us into a false dichotomy of control vs sharing.

Looking at physical models of sharing and access control, we can see that we already have well-established models where we can give up control temporarily, yet not completely.

Alan Karp illustrated this nicely at last week’s Internet Identity Workshop ([IIW](https://www.internetidentityworkshop.com/)) in a quick anecdote:

> Marc gave me the key to his car so I could park in in my garage. I couldn’t do it, so I gave the key to my kid, and asked my neighbor to do it for me. She stopped by my house, got the key and used it to park Marc’s car in my garage.

The car key scenario is clear. In addition to possession of they key, there’s even another layer of control — if my kid doesn’t have a driver’s license, then he can’t drive the car, even if he holds the key.

When we translate this story to our modern digital realm, it sounds crazy:

> Marc gave me his password so I could copy a file from his computer to mine. I couldn’t do it, so I gave Marc’s password to my kid, and asked my neighbor to do it for me. She stopped by my house so my kid could tell her my password, and then she used it to copy the file from Marc’s computer to mine.

After the conference, I read Marc Stiegler’s 2009 paper [Rich Sharing for the Web](http://www.hpl.hp.com/techreports/2009/HPL-2009-169.pdf) details key features of sharing that we have in the real world that are illustrated in the anecdote that Alan so effectively rattled off.

These 6 features (enumerated below) enable people to create networks of access rights that implement the Principle of Least Authority (POLA). The key is to limit how much you need to trust someone before sharing. “Systems that do not implement these 6 features will feel rigid and inadequately functional once enough users are involved, forcing the users to seek alternate means to **work around** the limitations in those applications.”

1. **Dynamic**: I can grant access quickly and effortlessly (without involving an administrator).
2. **Attenuated**: To give you permission to do or see one thing, I don’t have to give you permission to do everything. (e.g. valet key allows driving, but not access to the trunk)
3. **Chained**: Authority may be delegated (and re-delegated).
4. **Composable**: I have permission to drive a car from the State of California, and Marc’s car key. I require both permissions together to drive the car.
5. **Cross-jurisdiction**: There are three families involved, each with its own policies, yet there’s no  
  need to communicate policies to another jurisdiction. In the example, I didn’t need to ask Marc to change his policy to grant my neighbor permission to drive his car.
6. **Accountable**: If Marc finds a new scratch on his car, he knows to ask me to pay for the repair. It’s up to me to collect from my neighbor. Digital access control systems will typically record who did which action, but don’t record who asked an administrator to grant permission.

Note: Accountability is not always directly linked to delegation. Marc would likely hold me accountable if his car got scratched, even if my neighbor had damaged the car when parking it in the garage. Whereas, if it isn’t my garage, bur rather a repair shop where my neighbor drops off the car for Marc, then if the repair shop damages the car, Marc would hold them responsible.

How does this work for email?
-----------------------------

The following examples from Marc’s paper were edited for brevity:

- **Dynamic**: You can send email to anyone any time.
- **Attenuated**: When I email you an attachment, I’m sending a read-only copy. You don’t have access to my whole hard drive and you don’t expect that modifying it will change my copy.
- **Chained**: I can forward you an email. You can then forward it to someone else.
- **Cross-Domain**: I can send email to people at other companies and organizations with permissions from their IT dept.
- **Composable**: I can include an attachment from email originating at one company with text or another attachment from another email and send it to whoever I want.
- **Accountable**: If Alice asks Bob to edit a file and email it back, and Bob asks Carol to edit the file, and  
  Bob then emails it back, Alice will hold Bob responsible if the edits are erroneous. If Carol (whom Alice  
  may not know) emails her result directly to Alice, either Alice will ask Carol who she is before accepting  
  the changes, or if Carol includes the history of messages in the message, Alice will directly see, once  
  again, that she should hold Bob responsible.

Further reading
---------------

Alan Karp’s [IoT Position Paper](https://alanhkarp.com/publications/Access-Control-for-IoT.pdf) compares several sharing tools across these 6 features and also discusses ZBAC (authoriZation-Based Access Control) where authorization is known as a “capability.” An **object capability** is an unforgeable token that both designates a resource and grants permission to access it.