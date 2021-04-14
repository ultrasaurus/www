---
title: 'r: functions and avoiding loops'
date: '2015-04-07T18:30:22-07:00'
status: publish
exported_permalink: /2015/04/r-functions-and-avoiding-loops
author: sarah
excerpt: ''
type: post
id: 3719
category:
    - code
tag: []
post_format: []
---
After [getting started](https://www.ultrasaurus.com/2012/10/getting-started-with-r/) with the basic syntax and some frequently used functions, I needed to learn to write some code.

I enjoyed this nice [intro to functions](http://www.statmethods.net/management/userfunctions.html).

```

myfunction <- function(arg1, arg2, ... ) {
   statements
   return(object)
}
```

We can put functions (or any code) in a text file and load it from the R command line:

```

source("mycode.R")
```

where mycode.R is in the same directory as where I’m running R or a full path to the script.

But then I got stuck in how to transform my data table. As much as I wanted to iterate using loops, I felt that was a very un-R-like solution. I found some good patterns in [@xieyihui](https://twitter.com/xieyihui)‘s [gory loops](http://yihui.name/en/2010/10/on-the-gory-loops-in-r/) post.

If you need to make a string, you can use `paste` like Ruby’s join method:

```

> words  words
[1] "one"   "two"   "three"

> paste(words)
[1] "one"   "two"   "three"

> paste(words, collapse="")
[1] "onetwothree"

> paste(words, collapse=",")
[1] "one,two,three"

> paste(words, collapse=", ")
[1] "one, two, three"
```