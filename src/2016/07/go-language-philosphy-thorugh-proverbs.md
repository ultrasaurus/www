---
title: 'go language philosphy thorugh proverbs'
date: '2016-07-02T11:52:08-07:00'
status: publish
permalink: /2016/07/go-language-philosphy-thorugh-proverbs
author: sarah
excerpt: ''
type: post
id: 6001
category:
    - general
tag: []
post_format: []
---
Rob Pike’s [Go Proverbs](https://www.youtube.com/watch?v=PAAkCSZUG1c&feature=youtu.be) convey many elements of the Go programming language philosphy in a way that is approachable and fun. He compares with the game of Go, which is “easy to learn, and hard to master.” Inspired by the “Go Proverbs Illustrated” book about patterns in playing the game of Go, he crafted a set of proverbs about the Go programming language. His goal is that proverbs should be “short, poetic, general, about more than the Go programming language. Contradictory is OK. Life and programming are full of contradictions.” These are ideas to explain to beginners or maybe in a code review. He notes that there are probably many more. These proverbs seek to capture the ideas that make programming in Go different.

[![](../../../uploads/2016/07/noun_skill_share_14291.png)](https://thenounproject.com/term/skill-share/14291/)The proverbs with my notes from the talk are listed below. I also found a lovely post with [code illustrations](http://www.gregosuri.com/2015/12/04/go-proverbs-illustrated/) by [Greg Osuri](https://twitter.com/GregOsuri), as well as [graphically illustrated deck](https://github.com/ajstarks/go-proverbs) with nice icons chosen from the [noun project](https://thenounproject.com/) and if you have additional proverbs to suggest, there’s now a [github repo](https://go-proverbs.github.io/).

**“Don’t communicate by sharing memory, share memory by communicating”**  
Passing on a channel enables safe concurrent, even parallel operations.

**“Concurrency is not parallelism.”**  
These are often confused by beginners. How these are thought of in the Go community is that they are important to keep separate. Concurrency is a way that you structure your program to make it easier to understand and scalable, and parallelism is simply the execution of multiple Go routines in parallel — somewhat a less interesting topic than concurrency.

**“Channels orchestrate; mutexes serialize”**  
Mutexes are fine-grained and very small, and they tend to serialize execution. If you put a mutex on a variable, then only one thing can ever happen to that variable at any one time (and that is often very important, and sometimes exactly what you want). In the big picture of your program, channels give you a way to structure your program and arrange how the pieces work. As an example, how the “Select for loop” uses channels to orchestrate your program.

**“The bigger the interface, the weaker the abstraction”**  
In Java, you think about interfaces having lots of methods. In Go, we have interfaces which are not declared to be satisfied, they are satisfied implicitly, but even more important is the culture around interfaces that is captured by this proverb. The smaller the interface is the more useful it is. This is a Go-specific idea, we want to make little interfaces, so that we can build components that share them.

**“Make the zero value useful”**  
You want to make it so that you can use a type without initializing it (if you can).  
For example: Bytes buffer or sync mutex — you don’t have to call an init function, you don’t have to call any methods. There is nothing wrong with calling a constructor, sometimes you need that; however, if you can avoid it to make the program nicer, it just means there’s less API there which is always a good thing.

**“interface{} says nothing.”**  
When you are programming and have an empty interface, think very hard about whether that is really what you want…or whether there is just a little something that is really necessary to capture what you need. Sometimes you do need an empty interface, but it is rare. It is overused, especially by beginners. You see this in almost any question on stackoverflow in Go.

**“Gofmt’s style is no one’s favorite, yet gofmt is everyone’s favorite.”**  
Experienced Go Programmers will say “I don’t like how it formats, but I really like that it formats.”  
“A little copying is better than a little dependency.”  
You can make your programs compile faster and be simpler if you keep the dependency tree really, really small. Sometimes you don’t need that whole library, you just need those three lines of code, that you can just copy and it’s fine.

**“Syscall must always be guarded with build tags.”**  
Syscall isn’t portable — that is the point. If you import it, you must have a build tag for the architecture and operating system that syscall invocation is valid for. If you think you have a portable thing you are using the wrong package. Check out ‘os’ or something else.

**“Cgo must always be guarded with build tags.”**  
Same as above. If you are calling C, god knows what it does! It’s very non-portable. It needs to be built for specific architectures and operating systems.

**“Cgo is not Go.”**  
A lot of people in the early days would write about how a favorite feature of Go was how easily it connected to C, but lots of times it shouldn’t be necessary, it takes you out of the Go universe and you lose the benefits of Go if you are coding in C.

**“With the unsafe package there are no guarantees.”**  
A lot of people use “unsafe” and then complain that things don’t work… that’s the point, don’t use “unsafe” unless you are prepared to have your program break one day.

**“Clear is better than clever.”**  
Amen. There are languages that celebrate cleverness. Go celebrates simple clear code. The Go philosophy values code readability.

**“Reflection is never clear.”**  
Common Stackoverflow question of people wanting to use reflect and complaining that it doesn’t work. It doesn’t work, because it is not for you. Very, very few people should be playing with this. Powerful, yet very difficult to use. We should encourage beginners to step away from using reflection and use the language proper.

**“Errors are values.”**  
Beginners struggle with this. Too often people write “err != nil” — they think about substituting try/catch. Errors are just values…

**“Don’t just check errors, handle them gracefully.”**  
Think about whether you should be doing something with errors. People are too quick to just return an error up the tree, instead of designing how it should work. A big part of writing good Go code is getting the error handling right up front. Of any program really, but its easier to program with errors as just values, and easier to do it gracefully.

**“Design the architecture, name the components, document the details.”**  
Think of really good names for the pieces. If the names are good, the code will be easy to understand and the design will be clear inside your pogram, and programming your system will feel natural. Names should express your design.

**“Documentation is for users.”**  
Think about what the function is for, not what it does. You want to write something that the programmer using your function will find helpful.