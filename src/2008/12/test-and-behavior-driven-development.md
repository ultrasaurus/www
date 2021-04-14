---
title: 'test- and behavior-driven development'
date: '2008-12-21T09:36:41-08:00'
status: publish
exported_permalink: /2008/12/test-and-behavior-driven-development
author: sarah
excerpt: ''
type: post
id: 464
category:
    - general
tag:
    - software
    - testing
post_format: []
---
I did a bit of reading about test-driven development (TDD), which led me to behavior-driven development (BDD). I started out by looking at some [slides on TDD](http://andrzejonsoftware.blogspot.com/2008/04/tdd-with-rails-slides-from-my-talk-at.html) by Andrzej Krzywda which provide a nice overview:

- TDD (at a high level) is about visualizing goals
- Software developers are responsible for the visualization of other people’s goals
- Guidelines: 
  - write tests BEFORE writing production code
  - have many tests
  - 3D rule = Defense (Tests), Design, and Documentation
  - there is always exactly one test failing
- Definitions 
  - Acceptance test: a test from the user’s perspective
  - Unit test: a test of a class

Andrej argues that Rails focuses on acceptance tests because it is a mature community (from a TDD perspective) and because of the available tools. I’m not sure why REST makes it so controllers don’t need testing, but it makes sense to me that the focus is on tests of the model. Andrej goes on to introduce behavior-driven development (BDD). He recommends that you start with user stories. RSpec is a tool that helps with that. With BDD, you create executable specifications, not tests. You want to look at what your code does, not the internals of how it does it.

Bryan Helmkamp (via [Andrej’s blog](http://andrzejonsoftware.blogspot.com/2008/05/story-driven-development.html)) provides a quote from Robert Martin:

> Unit tests: “Make sure you write the code right.”
> 
> Scenarios: “Make sure you write the right code.”

“BDD is what you are doing already if you are ding TDD very well” notes Dave Astels, one of the creator’s of RSpec in “[Beyond Test Driven Development: Behaviour Driven Development](http://video.google.com/videoplay?docid=8135690990081075324&pl=true)“, Google TechTalk March 17, 2006. Further notes from that talk:

- If you focus on testing your classes, then the structure of your test code mirrors the structure of your production code. What happens when you refactor and you change that structure? do you then re-write your tests? If you focus on behavior you don’t have to. When you refactor, the behavior of your application doesn’t change
- Get away from state-based testing. If you depend on specific variables in your code, the inner state of your app, that will be a barrier to re-factoring. Instead of focusing on assertions, set expectations.

I found the link to Dave Astel’s talk in a [good thread on RSpec](http://www.ruby-forum.com/topic/94721) that is worth reading, where I also found the following memorable quotes:

> “any time your code does something unexpected, write a test.”
> 
> — [Eric Hodel](http://www.ruby-forum.com/topic/94721#195326)

> When I do TDD, I approach it with a Jeckle and Hyde perspective. When Iwrite a test, I am writing a specification of how the code should work.
> 
> When I start writing code, I become the laziest programmer you can imagine, writing only enough code to pass the specification as it is written at that moment. If it is not called out in the spec, it doesn’t get written.
> 
> When I switch back to test writing, I cuss out that lazy programmer (i.e. me just a few moments ago) and write additional specs to force the code to do exactly what I want.
> 
> The tension between Dr. Jeckle (the spec writer), and Mr. Hyde (the programmer) causes Dr. Jeckle to write better specs and Mr. Hyde to write lean, correct code.
> 
> — [Jim Weirich](http://www.ruby-forum.com/topic/94721#195102)