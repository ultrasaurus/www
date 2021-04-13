---
title: 'ruby unit test frameworks'
date: '2009-08-31T06:59:46-07:00'
status: publish
permalink: /2009/08/ruby-unit-test-frameworks
author: sarah
excerpt: ''
type: post
id: 1997
category:
    - code
tag: []
post_format: []
---
In preparation for teaching Ruby in a class with [test first teaching](https://www.ultrasaurus.com/sarahblog/2009/08/test-driven-teaching/). I decided to evaluate a few test frameworks. I thought initially to use Test::Unit, since it seemed easy to understand and ships with Rails. Wolfram Arnold argued that Test::Unit would [burden the new folks with legacy](http://twitter.com/wolframarnold/status/3336210949). Alex Chaffee also [advocated RSpec](http://twitter.com/alexch/status/3320591021), but [other](http://twitter.com/jacobrothstein/status/3320555832) [friends](http://twitter.com/jamieflournoy/status/3323143202) from the Twittervese had good things to say about shoulda. Some folks declared it to be simply a [matter of taste](http://twitter.com/noelrap/status/3319780641).

Even so, I wanted to make an informed decision and refine my palette for Ruby tools, so I wrote a simple exercise in each of Test::Unit, Shoulda and RSpec.

Test::Unit
----------

```

require 'test/unit'
require 'pig_latin'
 
class PigLatinTest < Test::Unit::TestCase
    include PigLatinTranslator
 
    def test_simple_word
        s = translate("nix")
        assert_equal("ixnay", s)
    end
 
    def test_word_beginning_with_vowel
        s = translate("apple")
        assert_equal("appleay", s)
    end
 
    def test_two_consonant_word
        s = translate("stupid")
        assert_equal("upidstay", s)
    end
end
```

With the above code saved as “test\_pig\_latin.rb” you run it by simply executing it with Ruby.

```
$ ruby test_pig_latin.rb
Loaded suite test_pig_latin
Started
FFF
Finished in 0.01091 seconds.

  1) Failure:
test_simple_word(PigLatinTest) [test_pig_latin.rb:9]:
 expected but was
.

  2) Failure:
test_two_consonant_word(PigLatinTest) [test_pig_latin.rb:19]:
 expected but was
.

  3) Failure:
test_word_beginning_with_vowel(PigLatinTest) [test_pig_latin.rb:14]:
 expected but was
.

3 tests, 3 assertions, 3 failures, 0 errors
```

- - - - - -

Shoulda
-------

Notice in the code below that Shoulda is simply and extension to Test::Unit. The PigLatinTest also subclasses Test::Unit::TestCase, just as the example above; however, the code inside the test case looks substantially different (and more readable in my opinion). You can actually mix Shoulda tests (below) with regular TestCase test methods (above) in the same TestCase. This is an advantage to Shoulda over RSpec if you have a codebase that already has lots of unit tests; however, I have also used RSpec and Test::Unit in the same project (you just have to remember to ‘rake test’ and ‘rake spec’).

```
require 'rubygems'
require 'shoulda'
require 'pig_latin'

class PigLatinTest < Test::Unit::TestCase
  include PigLatinTranslator

  context "#translate" do

    should "translate a simple word: nix" do
      s = translate("nix")
      assert_equal("ixnay", s)
    end

    should "translate a word beginning with a vowel: apple" do
      s = translate("apple")
      assert_equal("appleay", s)
    end

    should "translate a two consonent word: stupid" do
      s = translate("stupid")
      assert_equal("upidstay", s)
    end

  end
end
```

With the code above saved as “test\_shoulda\_pig\_latin.rb” you use the same process as above by just executing the file with ruby.

```
$ ruby test_shoulda_pig_latin.rb
Loaded suite test_shoulda_pig_latin
Started
FFF
Finished in 0.008268 seconds.

 1) Failure:
test: #translate should translate a simple word. (PigLatinTest)
 [test_shoulda_pig_latin.rb:12:in `__bind_1251676444_52936'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `call'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `test: #translate should translate a simple word. ']:
<"ixnay"> expected but was
<"translation">.

 2) Failure:
test: #translate should translate a two consonent word. (PigLatinTest)
 [test_shoulda_pig_latin.rb:22:in `__bind_1251676444_58860'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `call'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `test: #translate should translate a two consonent word. ']:
<"upidstay"> expected but was
<"translation">.

 3) Failure:
test: #translate should translate a word beginning with a vowel. (PigLatinTest)
 [test_shoulda_pig_latin.rb:17:in `__bind_1251676444_59935'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `call'
 /Library/Ruby/Gems/1.8/gems/thoughtbot-shoulda-2.10.2/lib/shoulda/context.rb:351:in `test: #translate should translate a word beginning with a vowel. ']:
<"appleay"> expected but was
<"translation">.

3 tests, 3 assertions, 3 failures, 0 errors
```

- - - - - -

RSpec
-----

```
require "pig_latin"

describe "#translate" do
  include PigLatinTranslator

  it "should translate a simple word" do
    s = translate("nix")
    s.should == "ixnay"
  end

  it "should translate a word beginning with a vowel" do
    pending
    s = translate("apple")
    s.should == "appleay"
  end

  it "should translate a two consonent word: stupid" do
    pending
    s = translate("stupid")
    s.should == "upidstay"
  end

end
```

The code above is saved in a file called “pig\_latin\_spec.rb” and run it using the ‘spec’ command. You will need to have installed the rspec gem (sudo gem install rspec).

```
$ spec pig_latin_spec.rb
F**

Pending:

#translate should translate a word beginning with a vowel (TODO)
./pig_latin_spec.rb:11

#translate should translate a two consonent word: stupid (TODO)
./pig_latin_spec.rb:17

1)
'#translate should translate a simple word' FAILED
expected: "ixnay",
     got: "translation" (using ==)
./pig_latin_spec.rb:8:

Finished in 0.035728 seconds

3 examples, 1 failure, 2 pending
```

Conclusion
----------

I like RSpec best since I find the output to be most readable. I love the pending keyword, which allows me to set up the tests as an exercise for the class with only one test failing. I find it helps focus on exactly one test and one failure. I considered going with Shoulda because the tests are just as readable as RSpec, even if the output takes some learning to read, because of my initial thought that Test::Unit held less magic. However, on closer inspection, I realized that Test::Unit has one significant magical incantation: you merely declare a class and when that class is defined, it runs the test. This seemed not the kind of topic I would want to teach in an intro class. Even some experienced programmers might struggle with understanding the mechanism that allows such a construct to function. I concluded that all of the test frameworks require serious magic, and picked RSpec since I found it to be most usable for test writing and analysis of the output.

Caveat: this exercise was for pure Ruby. In Rails, I wonder if Shoulda tests would be more concise, making them easier to write and read and, therefore, making it worth the steeper learning curve on reading the output.