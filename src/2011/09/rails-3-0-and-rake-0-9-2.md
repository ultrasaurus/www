---
title: 'rails 3.0 and rake 0.9.2'
date: '2011-09-11T08:37:17-07:00'
status: publish
exported_permalink: /2011/09/rails-3-0-and-rake-0-9-2
author: sarah
excerpt: ''
type: post
id: 3401
category:
    - code
tag: []
post_format: []
---
I really want to upgrade a Rails 3.0 project to Rails 3.1, but I’ve done a few spikes and it lacks test coverage, so I decided to pull in cucumber and write some features before moving forward.

I added cucumber-rails to my gemfile, and ran “bundle” and got this error:

```

/Users/sarah/.rvm/rubies/ruby-1.9.2-p290/lib/ruby/site_ruby/1.9.1/rubygems/specification.rb:289:in `load': uninitialized constant Psych::Syck (NameError)
```

What I really needed was to [update my Ruby Gems](http://blog.rubygems.org/2011/08/31/shaving-the-yaml-yacc.html) (bundle update –system) but before I discovered that I did “bundle update” which moved me forward to rake 0.9.2, so I started getting these warnings:

```

/Users/sarah/.rvm/gems/ruby-1.9.2-p290@pie-bakery/gems/psych-1.2.1/lib/psych.rb:93: warning: already initialized constant VERSION
/Users/sarah/.rvm/gems/ruby-1.9.2-p290@pie-bakery/gems/psych-1.2.1/lib/psych.rb:96: warning: already initialized constant LIBYAML_VERSION
WARNING: Global access to Rake DSL methods is deprecated.  Please include
...  Rake::DSL into classes and modules which use the Rake DSL methods.
WARNING: DSL method Bakery::Application#task called at /Users/sarah/.rvm/gems/ruby-1.9.2-p290@pie-bakery/gems/railties-3.0.0/lib/rails/application.rb:214:in `initialize_tasks'
```

So, I’ve learned from google, stackoverflow, various blogs and my twitter friend [@excid3](http://twitter.com/#!/excid3) that I need to update my Rakefile to include:

```

require 'rake/dsl_definition'
require 'rake'
include Rake::DSL
```

That lets me use rake (yay!). I still have the following two warnings:

```

/Users/sarah/.rvm/gems/ruby-1.9.2-p290@pie-bakery/gems/psych-1.2.1/lib/psych.rb:93: warning: already initialized constant VERSION
/Users/sarah/.rvm/gems/ruby-1.9.2-p290@pie-bakery/gems/psych-1.2.1/lib/psych.rb:96: warning: already initialized constant LIBYAML_VERSION
```

which I’m hoping will go away with the Rails 3.1 upgrade, but I thought I would write up the rest of it in case it helps other wayward souls on their journey.