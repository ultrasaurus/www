---
title: 'rspec: mixing transcations and truncation database clearner strategies'
date: '2014-01-18T11:23:46-08:00'
status: publish
permalink: /2014/01/rspec-mixing-transcations-truncation-database-clearner-strategies
author: sarah
excerpt: ''
type: post
id: 4936
category:
    - code
tag: []
post_format: []
---
I’m using capybara-webkit for integration testing with rspec, which is awesome, because it is faster than other full-browser testing solutions, like Selenium, but it is slower than RackTest (default for RSpec testing). RSpec provides a nice way to specify an alternate driver when running Javascript tests, but configuration can be a little tricky. I got this working via this [excellent blog post](http://www.livinginthepast.org/2013/11/24/today-we-went-to-the-bad-place.html) via [Sarah Mei](https://twitter.com/sarahmei), who was pairing with me for the day.

I think it is important to actually understand the code that I copy/paste, so I took a little time to read up on the details which I’ve summarized below.

Favorite Testing Gems
---------------------

I won’t elaborate on RSpec, the concepts in this post likely applies to test-unit as well. I written before about why [RSpec is my favorite](https://www.ultrasaurus.com/2011/04/on-choosing-rspec-as-a-test-framework/).

### Rack::Test

When using RSpec in Rails, we use the rspec-rails gem, which configures a bunch of stuff that makes it easy to get started. By default, integration tests will use [rack-test](https://github.com/brynary/rack-test), a lovely little gem that supports methods like get, post, put and delete and handles the rack request and response objects. (via [platformatec](http://blog.plataformatec.com.br/2012/06/improving-the-integration-between-capybara-and-rspec/)) It maintains cookies and follows re-directs, but is far from a full-browser, most notably, pages won’t execute Javascript. Rack::Test is quite lightweight, with tests running in the same process as your Rails code. Its speed is a huge advantage and worth retaining for your tests that don’t need more.

### Capybara

Capybara is the world’s largest rodent, and the Ruby community is also the name of a [favorite gem](https://github.com/jnicklas/capybara) for testing the content of web pages. (A successor to [Bryan Helnkamp](https://twitter.com/brynary)‘s WebRAT, so named for Ruby Acceptance Testing, which instigated the rodent naming theme) Capybara is wonderful with its support for many “drivers” which allow for a consistent API across different solutions that offer different levels of browser support, with different performance characteristics.

### Capybara::Webkit

Thoughtbot kindly created the [capybara-webkit](https://github.com/thoughtbot/capybara-webkit) gem a few years ago, which I’ve found to be more reliable and performant than Selenium, and is my favorite choice for testing pages that need Javascript.

One of its creators, Joe Ferris, explains how it works (via [stackoverflow](http://stackoverflow.com/questions/15945349/database-cleaner-issue-with-capybara-webkit))

1. Capybara boots up your rack application using webrick or thin in a background thread.
2. The main thread sets up the driver, providing the port the rack application is running on.
3. Your tests ask the driver to interact with the application, which causes the fake web browser to perform requests against your application.

### Database Cleaner

The [DatabaseCleaner](https://github.com/bmabey/database_cleaner) gem is super helpful for our typical Rails app that relies on a database. We always want a “clean slate” when we start our tests and this nifty gem gives us a bunch of options with a consistent interface for various database choices.

Configuration
-------------

To configure these solutions correctly, it is critical to understand that with Capybara::Webkit our target app code is running in a separate process from our tests. This means that when we set up our test data RSpec is running in one process and needs to actually write to the database, then our app code reads from the database from another process. Wheras with Rack::Test, the tests and the target code runs in the same process. That’s why we can’t use a “transaction” strategy to reset our test environment with Capybara::Webkit. Instead we use the “truncation” strategy, which simple blows away all of the data after each test run.

### Why bother with transactions?

Truncation will work just as well with Rack::Test as transcations, so why introduce the complexity of two different configurations? The [Database Cleaner README](https://github.com/bmabey/database_cleaner) explains: “For the SQL libraries the fastest option will be to use :transaction as transactions are simply rolled back.” Sarah Mei elaborated on this by reminding me that the commit to the database is what takes the most time, and the transaction is never committed, it is simply rolled back at the end of your test. Transactions are pretty speedy, so we want to only use the truncation method when absolutely necessary.

### Just Show me the Code

Here’s the configuration that was [documented by Eric Saxby](http://www.livinginthepast.org/2013/11/24/today-we-went-to-the-bad-place.html) from Wanelo, which worked for me as well:  
``

```
config.use_transactional_fixtures = true

config.before(:each, js: true) do
  self.use_transactional_fixtures = false
  ActiveRecord::Base.establish_connection
  DatabaseCleaner.strategy = :truncation
  DatabaseCleaner.start
end

config.after(:each, js: true) do
  DatabaseCleaner.clean
  ActiveRecord::Base.establish_connection
  self.use_transactional_fixtures = true
end

```

### How does this work exactly?

We are set up to use [transactions](https://relishapp.com/rspec/rspec-rails/docs/transactions) by default, which is built into rspec-rails and does not rely on DatabaseCleaner. Then, for our JS tests, we tell RSpec not to use transactions and instead instruct DatabaseCleaner to set up before each test runs with `DatabaseCleaner.start` and then clean up after with `DatabaseCleaner.clean`.

I have no idea why `ActiveRecord::Base.establish_connection` is needed, but if we don’t do that, then `rake spec` hangs after my first JS test with this ominous warning:

``

WARNING: there is already a transaction in progress

Perhaps someone reading this can explain this detail, but happy to have a configuration that works and hope this helps other folks who want fast tests that run reliably.