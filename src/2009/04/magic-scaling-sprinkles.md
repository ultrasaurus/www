---
title: 'magic scaling sprinkles'
date: '2009-04-18T08:08:35-07:00'
status: publish
permalink: /2009/04/magic-scaling-sprinkles
author: sarah
excerpt: ''
type: post
id: 1097
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
[Nick Kallen](http://magicscalingsprinkles.wordpress.com/), Twitter, author of popular open-source projects such as NamedScope, Screw.Unit, and Cache-Money, gave a compelling talk yesterday at the [Golden Gate Ruby Conference](http://gogaruco.com/). Nick’s easy-going presentation style and thoughtfully prepared examples made a complex topic easy to follow. Nonetheless, my notes are sparse since most of my attention was devoted to listening and absorbing.

> “Your website is a distributed network service.”

While the talk was entitled “Magic Scaling Sprinkles,” Nick dispelled the idea that any magic technology would solve scalability problems; instead, he shared some fundamental concepts of computer science underlying scalability:

- distribution
- balance
- locality

Two important concepts: **throughput** and **latency**

For example: 1 worker is able to complete a job in 1 sec. 1 job/sec is the *throughput* (number of jobs per unit time). 1 sec is the *latency* (elapsed duration from start of job to the end of a job). Latency is an efficiency question. Throughput is a scalability question. Focus of this talk on scalability.

Nick wrote a very simple echo server, ran a load test. Then added:

```
100000.times { Time.now }    # represents an intense loop. memory alloc + system call
sleep rand *3  #an efective representation of blocking i/o
```

complete code is on [github](http://github.com/nkallen/gogaruco/tree/master)

How many can we run in parallel? How many can we run per machine? How many can we run per core?

The code uses a statistics library, statosaurus, that they use at twitter (Nick’s github example contains a version of [statosaurus](http://github.com/nkallen/gogaruco/blob/2c80e891c5ecbeebada5b20d316a724ecec8170d/util/statosaurus.rb) which he says contains the key parts of the proprietary twitter package). Recommendation: **log everything** extensively, thread transaction ids throughout your logs. Essential for tracing down failed distributed transactions. (In SQL queries, HTTP headers, etc.)

For this example, he logs the following:

- a time stamp
- a transaction id
- wall-clock time: amount of elapsed real time
- system time: amount of time the process has spent in the CPU while in kernel mode
- user time: amount of time the process has spend in the CPU while in user mode

Note: `system time + user time < wall-clock time` Since there is wait time (simulated by sleep) or if there are too many process on the machine at the same time for the number of cores, so your process is waiting in the “run queue.” That latter excessive context switching is what we want to investigate.

Generally if we take the wall-clock time and divide by (system time + user time) we get the optimal number of processes per core. This leads us to a distribution strategy.

Nick talked about different mechanisms for distribution: TCP Proxy, DNS (compelling for a chatty protocol), client (has some serious drawbacks for maintenance/upgrades). In this case, proxy is an optimal solution.

Use a strategy of “least connections” aka “by business” which is more effective than round robin.

True efficiency: never do the same work twice.

**Locality**: analogy to tape drive, where if you write close to where you last wrote or read, then it will be significantly faster due to spatial locality. The same applies to hard drives and databases.  
Cache is a spatial locality that keeps the data near the code. Put the requests on processes where the data is most likely to be cached. Sticky sessions can be an essential technique.