---
title: 'getting started with r'
date: '2012-10-23T01:02:12-07:00'
status: publish
exported_permalink: /2012/10/getting-started-with-r
author: sarah
excerpt: ''
type: post
id: 3689
category:
    - general
tag: []
post_format: []
---
I installed the “roasted marshmallows” version of R (2.15.1) from [www.r-project.org](http://www.r-project.org/), which went smoothly on my MacBookPro running Lion. I was happy to find its REPL ran easily on the command line in Terminal.

> R is a free implementation of a dialect of the S language, the statistics and graphics environment for which John Chambers won the ACM Software Systems award. S was consciously designed to blur the distinction between users and programmers. S is a high-level programming language, with similarities to Scheme and Python. It is a good system for rapid development of statistical applications.  
> — [R fundamentals](http://faculty.washington.edu/tlumley/Rcourse/R-fundamentals.pdf)

R has amazing built-in primitives and libraries for what scientists like to do with data and incredible graphing options. I struggled to find good, simple resources to approach learning R as a programmer. I loved this [tutorial](http://www.stat.cmu.edu/~fienberg/Stat36-315/SomeFundamentalsofR.pdf). Here are my cliff notes:

The most fundamental objects are vectors — basically an array, where index starts at 1.  
Names of objects are case sensitive  
Comments starts with ‘#’

Examples:

```
n <- 25
v1 <- c(2,5,1,9)        # create a vector, combine a list of columns
v2 <- numeric(4)        # initialize a vector of specific length (with zeros)
v3 <- rep(3, 10)        # initialize a vector with number: repeat 3, 10x
v4 <- 1:4                  # specify a vector using the range 1-4
v4 <- 4:1                  # you can count down, 4,3,2,1
v4 <- 3:-1                 # even to negative numbers: 3,2,1,0,-1
v4 <- seq(1, 1.5, by=.1)   # easy to generate a sequence of equality spaced non-integers
v5 <- c(v3, v4, 7)        # c will combine or concatenate vectors
```

```
v2[1] <- 4         # use bracket notation to access (or set) an element
v2[1:3] <- 4:6     # you can even access (or set) a range
```

For those of us who already know it from Math class (or computer graphics), vector math in R works the way you would expect:

- when an operation involves a vector and a number, the number is used to modify each element of the vector as specified by the operation
- when arithmetic involves two vectors of the same length, then the operation applies to elements with the same index.

Adding vectors of different length doesn’t really make sense in real life (although maybe there’s an application for that I don’t know about), but R conveniently defines that the shorter vector is repeated as often a needed to match the length of the longer vector.

Like many languages, and more importantly, like Math, functions are a name with its arguments enclosed in parentheses. Here are some common ones:

```
max(v1)
mean(v1)
sum(v1)
prod(v1)
length(v1)
unique(v1)
```

By using parentheses for grouping, one can combine several expressions that involve  
functions.

```
(sum(v2^2) - (sum(v2)^2)/length(v2)) / (length(v2) - 1)
```

A simpler way to get the same result would be to use the `var` function.

```
var(v2)
```

The standard deviation is computed by using the expression `sqrt(var(v2))`

Comparisons are cool.

```

> 1  1:2  v6  v6[v6 < 3]    # find all elements in a vector which are  length(v6[v6 < 3])    # count how many are < 3
[1] 2
```