---
title: 'sinatra: simple ruby web app library'
date: '2009-04-17T10:05:24-07:00'
status: publish
permalink: /2009/04/sinatra-simple-ruby-web-app-library
author: sarah
excerpt: ''
type: post
id: 1036
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
talk by Aaron Quint, [quirkey.com](http://www.quirkey.com/), at [Golden Gate Ruby Conference](http://gogaruco.com/)

very simple framework, define a route, where it goes, return a string  
Sinatra is not a framework, doesn’t dictate how to create your code. It is a library. A ruby library for making Web applications.

**Why?** HTTP as a language? with REST and other conventions, it is cool to think of it as a way of two apps speaking to each other. If your library needs to “speak HTTP,” Sinatra is a good way to do that. It’s a nice layer on top of rack.

Aaron described a vision where all libraries would have web apps interfaces: to allow you to configure your library or inspect information. These are designed to be available on localhost, not designed for the “global web.”

For example: Aaron wrote ‘[gembox](http://code.quirkey.com/gembox/)‘ for Ruby Gems, which will display in a browser the list of installed gems. Simply calls the gem APIs, but provides a UI on it instead. The app is very little code, low effort for a significant return.

Vegas: super simple Sinatra starter. Provides simple options for running the app (startup, saving pid, etc.) (this is a cool idea right now, just a simple class right now)

Would be neat to be able to search for all gems that have Sinatra or Vegas interfaces. Question from the audience about security issues. This is still pretty early in development, but there are some neat ideas here and potentially useful tools.