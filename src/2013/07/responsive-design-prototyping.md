---
title: 'responsive design prototyping'
date: '2013-07-26T11:49:25-07:00'
status: publish
permalink: /2013/07/responsive-design-prototyping
author: sarah
excerpt: ''
type: post
id: 4180
category:
    - general
tag: []
post_format: []
---
[A Response-Able Process to Responsive Design](http://capitalcamp.org/content/response-able-process-responsive-design) talk by Mal Jones ([@skeletonjones](@skeletonjones)), Brian Verhoeven ([@beverhoeven](https://twitter.com/beverhoeven)) and Corey Lafferty ([@coreylafferty](https://twitter.com/coreylafferty)) introduced their agile process and a new open source prototyping tool that they built.

In 2011, they made responsive default for advocacy sites and content sites. **We’re no longer building cars, we’re building transformers**. How did they change their process?

Start with mobile story boards, then page description diagram. Pick three things on each page that are important, then three more, then the rest. Involve client in that prioritization — force them to choose.

Agile process. Prototype the unknowns — in the browser. They needed to be able to experiment. They need to be able to see how it looked and felt like on a phone. They looked at a lot of tools, but nothing really met their needs:

- fast sketching of ideas
- how elements respond in an actual environment (the web)
- A/B testing
- supports iteration

They ended up creating [Proty](http://www.protytype.com/), which can be used by coders and non-coders. If you are a coder, you can edit the HTML, but that isn’t required. Mobile first, breakpoints second (from sass). Each of the responsive sized gets its own file, but they aren’t mutually exclusive.

- Small gets loaded first
- Medium only what you need for the medium size that is not in the small (just the diffs)
- Large, same thing, just what you need in the desktop, that is not in medium + small.

How do we use Proty? we use it first for creating wireframes that are live and responsive to different sizes. You can add notes to the page, for clients or other team members.

We also use Proty for:

- technical tests / proof of concepts.
- style guides

This process helped us transition designers to learning HTML and CSS. Also helps with the agile process where there is overlap between dev and design roles.

Note: prototyping is not a magic way to create a web site once the design is complete. You still have to build a web site. If parts can be reused, great! but that’s not expected.

Responsive design cannot be an afterthought. It not a feature — it is how you build every feature. Identify what works on mobile and what doesn’t. Be able to recognize challenges early with embedded content, such as large document files, large tables of numbers, video, etc.

Brad Frost has a great list of [responsive design patterns for navigation](http://bradfrost.github.io/this-is-responsive/patterns.html). They like the “hamburger” menu (love that name for the icon with three little lines that typically triggers the main screen to reveal a side menu — see Path, Facebook, and many others now).

Don’t do the “hide &amp; cry” — just because someone is on a mobile phone, they still deserve to see all of your content!

Notes from the audience:

- checkout style\_guide module.
- Canvas will be hosting a devicelab in DC in the next few months.

For more info follow: [@forumone](https://twitter.com/forumone) and [@protytype](https://twitter.com/protytype)