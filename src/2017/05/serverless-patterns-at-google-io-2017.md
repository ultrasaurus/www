---
title: 'serverless patterns at google i/o 2017'
date: '2017-05-20T10:01:27-07:00'
status: publish
exported_permalink: /2017/05/serverless-patterns-at-google-io-2017
author: sarah
excerpt: ''
type: post
id: 6225
category:
    - general
tag: []
post_format: []
---
At Google I/O last week, we presented [how to build robust mobile applications for the distributed cloud](https://events.google.com/io/schedule/?section=may-18&sid=f2aa8aa1-e92d-4a64-a388-9d11956d3068&gclid=Cj0KEQjw0v_IBRCEzKHK0KiCrKMBEiQA3--1NuaEJInrBDuS9pPgIgA3Icy3SabhPPzbcEgJzlmETb4aAmnv8P8HAQ) about building mobile apps in this new world of “serverless development.” When people hear “serverless” sometimes they think we can write code on the server that is just like client-side code, but that’s not really the point.

We have many of the same concerns in developing the code that we always have when we write client-server sofware — we just don’t need to manage servers directly, which drastically reduces operational challenges. In this talk we dive into some specific software development patterns that help us write robust code that scales well.

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="433" loading="lazy" src="https://www.youtube.com/embed/9Fmsw5yzW5I?feature=oembed" title="How to Build Robust Mobile Applications for the Distributed Cloud (Google I/O '17)" width="770"></iframe>

Speakers:

- **Sarah Allen** (me!) I lead the engineering team that works at the intersection of [Firebase](https://firebase.google.com/) and [Google Cloud](https://cloud.google.com) on the server side.
- **Judy Tuan** introduced me to Firebase over 5 years ago, when she led our team at AngelHack SF (on May 3, 2012) to build an iPhone app that would paint 3D shapes by waving your phone around using the accelerometer. That event happened to be Firebase’s first public launch, and she met Andrew Lee who convinced her to use Firebase in our app. She’s an independent software developer, and also working with [Tech Workers Coalition](https://techworkerscoalition.org/).
- **Jen-Mei Wu** is a software architect at [Indiegogo](https://www.indiegogo.com), and also volunteers at [Liberating Ourselves Locally](https://oaklandmakerspace.wordpress.com/), a people-of-color-led, gender-diverse, queer and trans inclusive hacker/maker space in East Oakland.

Jen-Mei kicked off the talk by introducing a use case for serverless development based on her work at the maker space, which often works to help non-profits. They are limited in their ability to deploy custom software because they work with small organizations who are staffed by non-technical folk. It doesn’t make sense to set them up with a need to devote resources to updating to the underlying software and operating systems needed to run a web application. With Firebase, the server software is automatically kept up to date with all the needed security patches for all of the required dependencies, it scales up when needed, and scales down to zero cost when not in active use.

The primary use case that motivated the talk from my perspective is for businesses that need to get started quickly, then scale up as usage grows. I found it inspiring to hear about how Firebase supports very small organizations with the same products and infrastructure that auto-scale to a global, distributed network supporting businesses with billions of users.

The concept for this talk was for some *real-world developers* (Judy and Jen-Mei) to envision an application that would illustrate common patterns in mobile application development, then I recruited a few Firebase engineers to join their open source team and we built the app together.

Severless Patterns
------------------

We identified some key needs that are common to mobile applications:

- People use the app
- The app stores data
- The app show the data to people
- There is some core business logic (“secret sauce”)
- People interact with each other in some way

The talk details some of the core development patterns:

- Server-side “special sauce”
- Authentication &amp; access control
- Databinding to simplify UI development

The App: Hubbub
---------------

> Ever go to a conference and feel like you haven’t connected to the people you would have liked to meet? This app seeks to solve that! Using your public GitHub data, we might be able to connect you with other people who share your technical interests. Maybe not, but at least you’ll have lunch with somebody.

You authenticate with GitHub, then the app creates a profile for you by pulling a lot of data from the GitHub API. Your profile might include languages you code in, a list of connections based on your pull request history or the other committers on projects that you have contributed to. Then there’s a list of events, which have a time and place, which people can sign up for. Before the event, people will be placed in groups with a topic they might be interested in. They show up at the appointed time and place, and then to find their assigned group, they open a *beacon* screen in the app which shows an image that is unique to their group (a pattern of one or more hubbubs with their topic name) and they find each other by holding up their phones.

We built most of the app, enough to really work through the key development patterns, but didn’t have time to hook up the profile generation data collection and implement a good matching algorithm. We ended up using a simple random grouping and were able to test the app at Google I/O for lunch on Friday. Some people showed up and it worked!

[![](../../../uploads/2017/05/hubbub-in-action.jpg)](https://www.ultrasaurus.com/wp-content/uploads/2017/05/hubbub-in-action.jpg)

You can see the code at: <https://github.com/all-the-hubbub>

- - - - - -

Many thanks to all the people who joined our open source team to develop the app:

- [Ali Berlin Johnson](https://twitter.com/berlinjohnson)
- [Justin Rosenthal](https://twitter.com/justinrosenthal)
- [Susan Goldblatt](https://twitter.com/thatgoldblatt)
- [Tim Stirrat](https://twitter.com/timstirrat)
- [Margie Roswell](https://github.com/mroswell)
- [Erik Haddad](https://twitter.com/erikhaddad)
- [Brendan Lim](https://twitter.com/ok)

and who helped with the presentation:

- Virginia Poltrack, graphics
- Yael Kazaz, public speaking, story-telling coach
- [Puf](https://twitter.com/puf) and [Megan](https://twitter.com/mkrilanovich), rehearsal feedback
- [Todd Kerpelman](https://twitter.com/ToddKerpelman) our Google I/O mentor
- Laura Nozay and all of the wonderful Google I/O staff who made the event possible