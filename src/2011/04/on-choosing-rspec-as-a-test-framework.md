---
title: 'on choosing RSpec as a test framework'
date: '2011-04-01T06:42:18-07:00'
status: publish
exported_permalink: /2011/04/on-choosing-rspec-as-a-test-framework
author: sarah
excerpt: ''
type: post
id: 3068
category:
    - general
tag: []
post_format: []
---
There was [some discussion](http://www.rubyinside.com/dhh-offended-by-rspec-debate-4610.html), if you can call it that, on twitter yesterday about the proliferation of RSpec and Cucumber, over Test::Unit. I don’t believe that Twitter is an effective medium for well-reasoned debate. I do believe that it is worth discussing why we like one technology over another, so we can learn from each other and possibly refine our approach.

Since I started using RSpec there has been some evolution in the world of ruby test frameworks. I understand that Test::Unit now supports marking a test case “pending” and we can use strings to describe test cases with *it* syntax. It is great to see the test frameworks borrow ideas from each other and to be part of such a thriving ecosystem.

A couple of years ago, I [evaluated ruby unit test frameworks](https://www.ultrasaurus.com/sarahblog/2009/08/ruby-unit-test-framework) for teaching a class. I found it a happy result that based on my evaluation of test output, I chose RSpec for teaching over Test::Unit, since that is what I use for development. I don’t belong to a [cargo cult](http://twitter.com/dhh/status/52815575465992194) with test coverage falling from the sky. My reasons for using RSpec have not changed, but I think it is worth elaborating on why I continue to believe that RSpec is the right choice. I look at [teaching](#teach) and [development](#dev) as two separate use cases.

<a name="dev">For Development</a>
---------------------------------

I practice test-driven development where RSpec really shines, but even when I occasionally must use a *test last* approach, I find RSpec to be a good solution.

I love the simplicity of starting to code, by writing something like this:

```

describe Whatever do
   it "should be empty when it is created"
   it "should fly faster than the speed of light"
   it "should sparkle in the moonlight"
end
```

I start with pending tests, then write the code to make them fail and in the process I design my API and refine my implementation. I can easily focus on that initial inspiration because my test failures contain the language of that design. Nested describes and it strings are concatenated to form sentences, which I can easily review with the –format documentation (or -f d) option:

Here’s an example of that from one of the exercises I use in teaching Ruby:

```

$ rspec --format documentation perf_spec.rb

PerformanceMonitor
  runs code
  reports how long it takes
  runs code a number of times
  reports the average

Finished in 0.00414 seconds
5 examples, 0 failures
```

I look forward to checking out [Turn](https://github.com/TwP/turn) in Rails 3.1 which looks like it offers a similar kind of synopsis. I choose RSpec for my projects, but I will happily use Test::Unit if I’m contributing to another project where it is well-loved. I can still accomplish what I need to do for testing with Test::Unit, I just don’t find it to be as easy to *use*.

David Hansson [argues that Test::Unit is simpler](http://twitter.com/dhh/status/53481175909531648), but I think what he means is that it is simpler to learn. [David says](http://twitter.com/dhh/status/53601066520018944) this is “mostly based on feedback from people learning Rails and RSpec at the same time. And then being introduced to t/u.”

It is helpful to separate how easy something is to learn from how easy it is to use. I first heard this difference clearly articulated by [Douglas Engelbart](http://en.wikipedia.org/wiki/Douglas_Engelbart) in describing his approach to the development of the [Augment (NLS) system](http://en.wikipedia.org/wiki/NLS_%28computer_system%29). He invented the mouse and a chorded keyboard, so you could use one with each hand. It took some time to learn to use them, but once you knew how, you were very fast at creating and editing documents. He loved to draw the analogy of learning to ride on a child’s tricyle versus learning to ride a bike. A bicycle is harder to learn to ride, but lets you go much faster.

3 + \_\_ = 5 is simpler to understand than 3 + x = 5, but once you start bring able to work with variables, you have more powerful tools that feel simpler to work with. You need to understand addition and subtraction, before you can absorb the conceptual complexity of a variable, but once you get the concept of variables, going back to fill-in-the-blanks equations is awkward and would be even harder for complex equations.

I think the only aspect of RSpec that is hard to learn is the *should* syntax, as contrasted with the Test::Unit *assert* which many people are familiar with from junit (the Java unit test framework). I think you can now use asserts in RSpec, if you like ’em, but I don’t. I do agree the syntax is a little weird at first, but for me it really helps me remember what I’m testing. I’m not a big fan of positional arguments, especially when they are similar, but act differently, because I sometimes forget which is which.

In Test::Unit, when I want to assert that num is equal to 4, I write

```

assert_equal(num, 4)
```

In RSpec, I write:

```

num.should == 4
```

I might make an error and write assert\_equal(4, num), but I would never write 4.should == num. The latter just feels wrong, whereas with assert I need to think about the order of the parameters. Some people are probably really good at remembering that, but I think I’m like most people who have to work at remembering arbitrary binary things.

Lastly, the reason I most value RSpec is in its clarity of output for a test failure, which I covered in detail in my [earlier comparison](https://www.ultrasaurus.com/sarahblog/2009/08/ruby-unit-test-frameworks). When I’m working on production code and a test fails, that is when I want to be most efficient and when I want to have the least cognitive load. I don’t mind that I spent a little more time familiarizing myself with the RSpec syntax and writing clear descriptions of my tests, because when I see a failure, I see a high level description of the failure and can easily parse the specific technical failure without extraneous text.

<a name="teach">For Teaching (and learning)</a>
-----------------------------------------------

I agree that trying to learn how to develop tests in RSpec while learning Ruby and Rails all at the same time is very challenging. I don’t recommend that. I think it is easiest to learn Ruby first, then learn Rails, and while learning both use tests as a kind of lesson planner in the test-first teaching style that has been [independently developed](https://www.ultrasaurus.com/sarahblog/2009/09/learning-through-testing/) by so many engineers. (You can learn more about Test First Teaching with [Ruby Koans](http://rubykoans.com/) and at [testfirst.org](http://testfirst.org/).)

**But why use RSpec for teaching?**  As I’ve said, my initial bias was toward using Test::Unit for teaching. Like David, I thought it was simpler for people to understand that instance methods were being executed as test cases. However, with a teaching approach where I deliver failing tests to students as exercises for them to solve, I feel that the format of the output for failing tests is critical and RSpec still has much cleaner failure reports. Students only have to be able to read the tests, not generate them, and I find that people can quickly do that. Later, after they understand Ruby and Rails, developing tests with RSpec is straightforward since they have already become familiar with reading and understanding the syntax.

Even after reviewing results from the [test framework comparison](https://www.ultrasaurus.com/sarahblog/2009/08/ruby-unit-test-frameworks), I was still leaning toward Test::Unit because I thought it would be easier to explain. Then I started to think about how I would explain this:

```

require 'test/unit'
require 'whatever'

class WhateverTest < Test::Unit::TestCase
    def test_something_is_nil
        assert_equal(nil, Whatever.something)
    end
end
```

which we run with:

```

$ ruby test_whatever.rb
```

I imagined myself saying…

> Just like any other ruby file, we can run our test on with the “ruby” command. In our test file, you can see that WhateverTest is simply a subclass of Test::Unit::TestCase, and then we define instance methods with each aspect of our code that we want to test. Then… um… when Ruby reads the class definition it executes the instance methods of that class.

Eek. There’s no way I wanted to say that to people on their first introduction to Ruby. I didn’t want to introduce that sometimes classes and instance methods work differently — at least not on day 1!

I concluded that there is a whole lotta magic in every test framework and you need to reach a certain level of sophistication with a language before you can understand how a test framework does its job. And just as I used a C compiler long before I ever knew how it really worked, I figured students could learn to how to make failing RSpec tests pass without needing to understand all of the nuances of syntax and how it all works. I also teach that there are other test frameworks and usually demonstrate Test::Unit. After people know Ruby, Rails and one testing framework, I figure they can make an informed choice.

No teaching methodology is perfect. I’ve found this works for most students and is more effective than the old “build something that does X” methodology. At least after they finish the exercise, they know that they accomplished the assignment. The RSpec output does a good job of surfacing the Ruby and Rails error messages that I am trying to teach, and along the way, I believe I am introducing students to best practices in terms of development.