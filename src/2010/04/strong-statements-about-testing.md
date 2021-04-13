---
title: 'strong statements about testing'
date: '2010-04-21T22:22:39-07:00'
status: publish
permalink: /2010/04/strong-statements-about-testing
author: sarah
excerpt: ''
type: post
id: 2512
category:
    - general
tag: []
post_format: []
---
I enjoyed “strong statements” in [Shannon Behrens’ SF Ruby talk](http://jjinux.blogspot.com/2010/04/ruby-introduction-to-behavioral-driven.html) tonight. I didn’t agree with all of them, but not vehemently so. I do strongly agree with the following.

- Not all tests have the same value
- Some tests don’t provide enough value to justify their existence 
  - perhaps they take too long to write
  - perhaps they are too brittle
  - perhaps they test things that you don’t actually care about
- Blackbox testing the behavior of code by using its public interface is much more valuable than whitebox testing its implementation
- A strong emphasis on testing is no substitute for good design (attributed to Yehudah Katz)
- Not testing error handling code is as bad as not writing error handling code  
  Exploratory testing by someone else is crucial

Shannon states that “integration tests have more value than unit tests.” I would say instead that some unit tests that rely heavily on mocking have a high risk of not achieving their goals, and in these cases integrations tests have more value. (For example, I typically test Rails controllers through integration tests rather than unit test.) However, when a class is relied upon as the foundation for my app, unit tests for that class are more valuable than integration tests because they help me find and fix bugs faster than the integration tests. But I agree that integration tests are essential.