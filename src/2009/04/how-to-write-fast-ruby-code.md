---
title: 'how to write fast ruby code'
date: '2009-04-17T16:22:57-07:00'
status: publish
permalink: /2009/04/how-to-write-fast-ruby-code
author: sarah
excerpt: ''
type: post
id: 1083
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
Carl Lerche talks about how to write fast ruby code. Yes, ruby is scalable. Scaling != speed. Focus of this talk is on speed. Ruby is fast enough for the vast majority of use cases.

> “Slow code is your fault.”

How can I write fast code?  
1\. **Write slow code**: well-structured code that is easy to read. Don’t worry about performance the first time around. You can’t tell from the beginning what matters.  
2\. **Use the scientific method**.

1. Define the question
2. Gather information: where is time/memory being spent?
3. Form Hypothesis: why is this chunk of code slow/memory hog
4. Perform an experiment and collect data
5. Publish results (restart if needed)

Need questions like: “why is action X taking 600ms? ” why is 60% of a Merb dispatch cycle in content negotiation?” Why are my mongrel instances growing to 300MB of memory”

Some useful tools:

- [RBench](http://github.com/somebee/rbench/tree/master)
- [ruby-prof](http://ruby-prof.rubyforge.org/) to generate profile data / [kcachegrind](http://kcachegrind.sourceforge.net): for reading profile data
- explain analyze log files
- New Relix / five runs
- memory\_usage\_logger
- Bleak\_house (memory leaks)

Garbage collector is a conservative mark and sweep garbage collector. When it runs all your code stops. Each run can take 50-150ms. Triggers befre grabbing more system memory (every 8MB).

Avoid creating unecessary objects. Understand the difference between Ruby methods (e.g. the difference between reverse! and reverse).

DataMapper’s identity map is pretty awesome.

Beware of modifying large strings.

Don’t concat strings just to pretty print them across lines. Do this instead:

```
     s = "Here is my long string" 
           " that continues"
```

Beware of closures.

No code is the fastest code. Be lazy. Don’t run code till you have to.

“Compiling your code.” Iterating is slow. Ruby’s AST is fast. (This is a little crazy, but sometimes you need it.)

Make sure you have great tests, then when you optimize you can make sure you didn’t break anything.