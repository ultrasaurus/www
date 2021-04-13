---
title: 'sandbox for ruby code'
date: '2009-04-17T11:08:13-07:00'
status: publish
permalink: /2009/04/sandbox-for-ruby-code
author: sarah
excerpt: ''
type: post
id: 1044
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
David Stevenson, [flouri.sh](http://flouri.sh/), talk “Playing With Fire: Running Uploaded Ruby Code in a Sandbox” at [Golden Gate Ruby Conference](http://gogaruco.com/)

A sandbox needs to:

- Limit functionality
- Make it so code can’t break out
- Separate code space
- Bounded execution time

**Sandbox gems**

- Freaky-freaky sandbox gem (MRI Ruby): it’s a gem, but you can’t use gem install. No support for 1.8.7 and later.
- JavaSand gem (JRuby): same API as the freaky-freaky sandbox, more actively maintained
- Rubinious has SubVMs, David doesn’t have experience with it

**acts\_as\_runnable\_code** is a sandbox helper:  
set up sandbox easily with referenced classes  
pass in top-level binding

Built an example in just a few minutes that allowed people to enter experession to be evaluated and opened to the audience (offering cupcakes to anyone who broke it!). Here’s some of the first experiments from the audience:

![Exprs: index](http://img.skitch.com/20090417-bb68kd3qyyn3yrimx2htyc1bna.jpg)