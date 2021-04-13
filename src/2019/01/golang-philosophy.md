---
title: 'golang philosophy'
date: '2019-01-18T08:16:43-08:00'
status: publish
permalink: /2019/01/golang-philosophy
author: sarah
excerpt: ''
type: post
id: 6719
category:
    - Uncategorized
tag: []
post_format: []
---
In learning a new programming language, it’s helpful to understand it’s philosophy. I seek to learn patterns that are idiomatic, and more importantly: why the syntax is the way it is. This allows me to write original code more quickly, gaining an intuition for simple things like when to look for a library and when to just write code.

I rarely find good resources for learning a new language that are targeted at experienced programmers. So I’ve developed a habit of looking for language koans. Inspired by [Ruby Koans](http://rubykoans.com/), these are unit tests which guide a programmer through basic language constructs by presenting a failing test and let you write simple code to learn the syntax of a language. These tests typically include a bit of text that helps newcomers reflect on what is special and interesting about this particular programming language.

In learning Go, I found [cdarwin/go-koans](https://github.com/cdarwin/go-koans), which helped me to reflect on the philosophy of golang, the Go programming language.

The koans caused me to meditate on the basics, leading me to read more and reflect. While [about\_basics.go](https://github.com/cdarwin/go-koans/blob/master/about_basics.go) is quick to solve technically, it sparked my curiosity on two points.

1. The uninitialized variable
-----------------------------

I really wanted the comments in the `go-koans` to be a bit more like Zen koans (or Ruby koans), so I wrote these:

```
// listen to the darkness of an unset variable
// what is the code that is not written?
// consider the emptiness of a string

// create meaning from emptiness
// undefined structure isn't

```

“Make the zero value useful” —[Go Proverbs](https://go-proverbs.github.io/)

It reminds me of the [Zen teacup parable](http://bengtwendel.com/your-teacup-is-full-empty-your-cup/). An empty cup has utility, even before it is filled.

2. The implications of a string
-------------------------------

One of the most deceptively simple types in modern programming languages is the string. In Go, there is a [built-in string type](https://golang.org/pkg/builtin/#string) with short, unsatisfying descriptive text.

[Strings, bytes, runes and characters in Go](https://blog.golang.org/strings) explains that strings are a read-only slice of bytes (at runtime). Go source code is UTF-8, so string literals always contain UTF-8 text (except for [byte-level escapes](https://golang.org/ref/spec#String_literals).

Strings always cause me to reflect on how memory management works in a language. In my search for basic answers about how and when memory happens in string operations, I read about [allocation efficiency in high-performance Go services](https://segment.com/blog/allocation-efficiency-in-high-performance-go-services/) which includes a nice explanation of heap vs stack memory allocation in Go.

Reflections
-----------

At this point, I don’t know what I need to know about this new programming language. I just like to know what the code I’m typing actually does. Learning syntax is boring, so I need to occupy my mind with something more interesting while I practice typing unfamiliar sequences of text. To write good code, I need to know so much more than the syntax, but I need to be careful not get get too attached to certain details. For example, future compiler versions change the patterns of how code is transformed into machine operations. However, if I attach just a little deeper meaning to these syntax constructs and get a feel for what my code ends up doing under-the-hood, I can more quickly understand the implications of the code I write.

When I emerge from these learning meditations and I can finally construct this new syntax without thinking and start to solve actual problems that matter to humans, then I will have created these little trails in my mind that lead to empty spaces, which have shape and meaning, like the Go zero value and the Zen teacup.