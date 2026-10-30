---
title: 'truthiness in ruby'
date: '2015-12-13T23:10:24-08:00'
exported_permalink: /2015/12/truthiness-in-ruby
id: 5737
category: general
---
I found myself confronting some unexpected truths in Ruby the other day…

```
2.2.2 :001 > 1 and 0
 => 0
2.2.2 :002 > 0 and 1
 => 1
```

In most programming languages, 0 is false and 1 is true, or more accurately we say that 1 is “truthy.” In popular culture, [truthiness](http://www.cc.com/video-clips/63ite2/the-colbert-report-the-word---truthiness) is believing something to be true from gut feelings, rather than relying on those pesky facts. Google defines truthiness as “the quality of seeming or being felt to be true, even if not necessarily true.” This is closer to what programming languages mean. 1 is 1, but it treated as true if used within a conditional.

```
2.2.0 :001 > 1 == true
 => false
2.2.0 :002 > if 1
2.2.0 :003?>   puts "1 is truthy"
2.2.0 :004?> else
2.2.0 :005 >   puts "this doesn't happen"
2.2.0 :006?> end
1 is truthy
```

In Ruby, every number, every value is an instance of an object:

```
2.2.0 :007 > 1.class
 => Fixnum
2.2.0 :008 > true.class
 => TrueClass
2.2.0 :009 > "potato".class
 => String
```

So every object, is a thing, which has a value and evaluates to true in a conditional expression, which means 0 is truthy…

```
2.2.0 :001 > if 0
2.2.0 :002?>   puts "0 is truthy"
2.2.0 :003?> else
2.2.0 :004 >   puts "never gets here"
2.2.0 :005?> end
0 is truthy
```

So, both 0 and 1 will act like true in a conditional. [@MarmiteJunction notes](https://twitter.com/MarmiteJunction/status/676464619708358656) that this works completely as expected:

```
(1 and 0) ? true : false #true
(0 and 1) ? true : false #true
```

The last piece of the puzzle is the behavior of `and` which is one of the “boolean operators” and I usually think about them as evaluating to true or false, but that’s not exactly how they work.

```
2.2.0 :006 > "cat" or "dog"
 => "cat"
2.2.0 :007 > "nuts" and "berries"
 => "berries"
```

Each of boolean expressions above are truthy, but are not `true`. The OR expression will return the first truthy value, and the AND expression will return the last one. In other contexts, I’m used to the commutative property of AND and OR, but in Ruby that’s not at all true:

```
2.2.2 :001 > 1 and 0
 => 0
2.2.2 :002 > 0 and 1
 => 1
```

hmmm.