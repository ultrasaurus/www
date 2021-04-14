---
title: 'MacRuby and Hot Cocoa'
date: '2009-04-17T09:31:16-07:00'
status: publish
exported_permalink: /2009/04/macruby-and-hot-cocoa
author: sarah
excerpt: ''
type: post
id: 1028
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
great session by[ Rich Kilmer](http://gogaruco.com/speakers/index.html#kilmer) at Golden Gate Ruby Conference.

[MacRuby](http://www.macruby.org/), started toward the end of ’07. It has two ambitious goals:

- Make Mac OSX the best platform for Ruby developers
- Make Ruby the best Cocoa programming language on OSX

Apple has the higher level APIs in Objective-C. RubyCocoa (2001) mostly written in C will bridge Ruby &amp; Objective-C. Quite verbose. Rich showed a “hello world” that was about a page of code in small type. Problem: it’s a bridge. Thereare holes, expensive (slow), messaging syntax is diferent. Ruby uses green threads (it is not re-entrant) — only one native thread can enter the Ruby runtime at any time. Tricky garbage collection, etc.

The development of MacRuby leveraged the key observation that Ruby is actually similar to Objective-C. MacRuby replaced the Ruby 1.9 garbage collector with the Objective-C garbage collector. Ruby’s hash is actually an NsMetuable dictionary. Every Ruby class is an Objective-C class. You can use MacRuby, at runtime to add methods to an Objective-C object.

MacRuby is 0.4. Syntax is better, but still a lot of code for “Hello World”

**HotCocoa**  
In the MacRuby “hello world” a lot of the code is in configuring, setting up the app, wiring things together. [HotCocoa](http://www.macruby.org/trac/wiki/HotCocoa) is just a library that helps simplify this setup process.

Much more concise, but it isn’t magic. ‘window’ returns an NSWindow, it isn’t obscured, just decorated. You have all the NSWindow methods available,

Hello World turns into 7 lines of code! \[update: [nice post](http://pivotallabs.com/users/edward/blog/articles/779-gogaruco-talk-macruby-hotcocoa) with code snippets\]

hotcocoa &lt;app&gt; (similar to rails &lt;app&gt;) will generate all the files needs for a Mac application. Framework is dropped in there, so you can give the code to someone and they don’t need

HotConsole: written in MacRuby and it is irb, but {}.methods(true,true) will show you all of the methods in an MSMutable dictionary, but otherwise {} behaves just like a Ruby hash. Also let you interactively create native Mac OS widgets (create a window, add a button, make it do something) all by typing in a few lines into this interactive console.

**MacRuby Experimental**

LLVM replaces yarv. In this, using MacRuby the jit generates machine code. This makes it 4-5x faster than 1.9 (which is 4-5 times faster than 1.8). Goal is to pass all of 1.9 Ruby specs, and it is well on its way to doing this. Also plans to make it reentrant. Goal is to automatically generate GrandCentral code hich allows the code to run across all the cores in the machine. Rich expects this to be complete by the end of the year. This could also be applied to compiling ahead of time which would enable running the code on a certain devices that don’t run Ruby, yet run OSX code :)