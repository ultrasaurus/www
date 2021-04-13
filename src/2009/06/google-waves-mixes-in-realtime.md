---
title: 'google waves mixes in realtime'
date: '2009-06-01T19:30:38-07:00'
status: publish
permalink: /2009/06/google-waves-mixes-in-realtime
author: sarah
excerpt: ''
type: post
id: 1434
category:
    - general
tag: []
post_format: []
---
It is not a new idea to mix synchronous and asynchronous communication, in other words, mixing real-time, like chat, and store &amp; forward, like email. I have always felt that Internet communications application are oddly modal, where the UI is largely driven by the protocol. It was one of the things that led me to join Jonathan Gay in creating the Flash Media Server. The primary use case of Flash video has, of course, been simple broadcast, but we built in flexible APIs that allowed Tivo-like behavior for video and a seamless mix of real-time and persisted data with Shared Objects.

Google Waves seems to have a quite nice implementation of a new model of communication, allowing people to seamlessly move between real-time chat and email-like messaging. Some of the social interactions are very experimental and may or may not fly, but it was fun to [see what they came up with](http://wave.google.com/) and the joy with which it was demonstrated by one of its creators, Lars Rasmussen.

I agree with Lars when he said “UI changes the way you think. He notes how you think of written communucation as a document or as a message, but waves doesn’t make that distinction. I actually think that distinction is healthy. I experience a conversation. I craft a document. I’ve also noticed that I find myself subverting the intention of the UI in various applications that I use, most notably email. I’ll use my drafts folder for initial drafts of documents and notes that I never intend to send as an email message. I think it more likely that the UI paradigm that will catch on will be an evolution of today’s ubiquitous applications rather than something that feels as different as Waves. We are already seeing the mix of real-time with email with presence indicators alongside the sender’s name in Apple Mail and collaboration features invading the staid Microsoft desktop applications.

Nonetheless, I found the shared editing with interspersed conversation intriguing and its magical transformation into a finished document appealing. With live concurrent editing in Waves, people can edit separate parts of the document at the same time. They’ve done a nice job in supporting languages that require IME (Input Method Editor), like Chinese, and right to left languages, like Hebrew.

The spell-checker component was impressive independent of the communications framework it plugs into. Lars demonstrated that it could find mistakes that could only be detected in context “I like been soup. How have you bean?” The live spellchecker is an extension. It can “watch” a document and then make live edits and act as a collaborator just like a human would. Yes-No-Maybe gadget is another example, allowing people to vote as part as a conversation. At the very end they demonstrated live translation that appeared to work much better than the current Google translate. An agent, nicknamed “Rosie” does live translation between any pair of 40 languages while you type. The visual feedback is distracting, but the technology is impressive. I wonder when that magic will be accessible outside of Waves…. or maybe Google Translate has seen an upgrade since I last used it a few weeks ago.

Google is betting that in making Waves an open system (providing a reference implementation, documenting the [protocol](http://www.waveprotocol.org/) and making available a free production-ready system) they will gain adoption — certainly they are aggressively removing barriers. Federation allows someone to independently deploy a different server that uses the Wave protocol. Analogous to different email servers all implementing the same protocol.

The main barrier is whether people will adopt a different paradigm when the old ones are good enough. I don’t have access to the software since I missed Google I/O, but they seem to be offering a nice set of UI widgets for embedding along with web APIs. They went so far as to say that by embedding these widgets, “your users get to use a familiar UI.” I thought that an interesting assumption of success where such revolutionary (as opposed to evolutionary) new interaction models don’t typically gain traction.

Nonetheless, I plan to fill out their web form and see if they will let me play in their [sandbox](https://services.google.com/fb/forms/wavesignupfordev/).