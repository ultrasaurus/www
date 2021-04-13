---
title: 'truthiness in ruby'
date: '2015-12-13T23:10:24-08:00'
status: publish
permalink: /2015/12/truthiness-in-ruby
author: sarah
excerpt: ''
type: post
id: 5737
category:
    - general
tag: []
post_format: []
---
I found myself confronting some unexpected truths in Ruby the other day…

`<br></br>2.2.2 :001 > 1 and 0<br></br> => 0<br></br>2.2.2 :002 > 0 and 1<br></br> => 1<br></br>`

In most programming languages, 0 is false and 1 is true, or more accurately we say that 1 is “truthy.” In popular culture, [truthiness](http://www.cc.com/video-clips/63ite2/the-colbert-report-the-word---truthiness) is believing something to be true from gut feelings, rather than relying on those pesky facts. Google defines truthiness as “the quality of seeming or being felt to be true, even if not necessarily true.” This is closer to what programming languages mean. 1 is 1, but it treated as true if used within a conditional.

`<br></br>2.2.0 :001 > 1 == true<br></br> => false<br></br>2.2.0 :002 > if 1<br></br>2.2.0 :003?>   puts "1 is truthy"<br></br>2.2.0 :004?> else<br></br>2.2.0 :005 >   puts "this doesn't happen"<br></br>2.2.0 :006?> end<br></br>1 is truthy`

In Ruby, every number, every value is an instance of an object:

`<br></br>2.2.0 :007 > 1.class<br></br> => Fixnum<br></br>2.2.0 :008 > true.class<br></br> => TrueClass<br></br>2.2.0 :009 > "potato".class<br></br> => String<br></br>`

So every object, is a thing, which has a value and evaluates to true in a conditional expression, which means 0 is truthy…

`<br></br>2.2.0 :001 > if 0<br></br>2.2.0 :002?>   puts "0 is truthy"<br></br>2.2.0 :003?> else<br></br>2.2.0 :004 >   puts "never gets here"<br></br>2.2.0 :005?> end<br></br>0 is truthy<br></br>`

So, both 0 and 1 will act like true in a conditional. [@MarmiteJunction notes](https://twitter.com/MarmiteJunction/status/676464619708358656) that this works completely as expected:

`<br></br>(1 and 0) ? true : false #true<br></br>(0 and 1) ? true : false #true<br></br>`

The last piece of the puzzle is the behavior of `and` which is one of the “boolean operators” and I usually think about them as evaluating to true or false, but that’s not exactly how they work.

`<br></br>2.2.0 :006 > "cat" or "dog"<br></br> => "cat"<br></br>2.2.0 :007 > "nuts" and "berries"<br></br> => "berries"<br></br>`

Each of boolean expressions above are truthy, but are not `true`. The OR expression will return the first truthy value, and the AND expression will return the last one. In other contexts, I’m used to the commutative property of AND and OR, but in Ruby that’s not at all true:

`<br></br>2.2.2 :001 > 1 and 0<br></br> => 0<br></br>2.2.2 :002 > 0 and 1<br></br> => 1<br></br>`

hmmm.