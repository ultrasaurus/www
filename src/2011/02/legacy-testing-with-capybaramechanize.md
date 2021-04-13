---
title: 'legacy testing with capybara/mechanize'
date: '2011-02-15T23:11:00-08:00'
status: publish
permalink: /2011/02/legacy-testing-with-capybaramechanize
author: sarah
excerpt: ''
type: post
id: 3057
category:
    - general
tag: []
post_format: []
---
I spent a little time working on some tests for a legacy web app that we plan to re-write in Ruby. Before the big re-write, I thought it would be wise to write some integration tests to call the app via http and verify responses. I wanted to use vanilla http and not have the overhead of launching a browser and was frustrated that Capybara didn’t have a driver to suit my needs.

I started down the path of writing tests from scratch using Net::HTTP, but figured that there had to be someone else who had run into this before. [@kakutani](http://twitter.com/kakutani) told me about [capybara-mechanize](https://github.com/jeroenvandijk/capybara-mechanize) which seems to be exactly what I need.

Here’s my first really basic experiment using RSpec to test a well-known web site:

```

require 'capybara/rspec'
require 'capybara/mechanize'
Capybara.default_driver = :mechanize

describe 'web app' do
  include Capybara

  before do
    Capybara.app_host = "http://www.google.com"
  end

  it "has a copyright" do
    visit '/'
    page.should have_content('© 2011')
  end

end
```