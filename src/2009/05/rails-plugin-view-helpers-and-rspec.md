---
title: 'rails plugin view helpers and rspec'
date: '2009-05-25T07:57:05-07:00'
status: publish
exported_permalink: /2009/05/rails-plugin-view-helpers-and-rspec
author: sarah
excerpt: ''
type: post
id: 1368
category:
    - code
tag: []
post_format: []
---
RSpec for View Helpers
======================

- To test a view helper, you need to test the plugin in the context of a rails app
- To verify that you can put the following code into your spec\_helper.rb (or just use [rspec-plugin-generator](http://wiki.github.com/pat-maddox/rspec-plugin-generator/installation-and-basic-use) by [Pat Maddox](http://www.patmaddox.com/blog/) which will generate this code for you) ```
  begin
    require File.dirname(__FILE__) + '/../../../../spec/spec_helper'
  rescue LoadError
    puts "You need to install rspec in your base app"
    exit
  end
  ```
- By convention, helper examples live in spec/helpers/ then their dependencies will get magically included. [<span class="name"> David Chelimsky notes</span>](http://www.ruby-forum.com/topic/187635#819442)  
  > All directories under spec/ are potentially magic – rspec will always  
  > look at spec/:directory/:filename and see if it has an example group  
  > type registered for whatever directory is. So if there \*is\* a foo  
  > example group type, it will be used for any spec file in spec/foos
- If you put helpers elsewhere, then you need to declare their type (or manually include dependencies) ```
  describe AppletHelper, :type => :helper do
  ```
- To send params in your test, you can just define them before calling your view helper. For example: ```
  describe DogHelper do
    it "should bark" do
      params[:debug] = "foo"
      html = helper.bark
      html.should have_tag("script")
    end
  end
  ```

What do you do when some behavior depends on RAILS\_ENV?
========================================================

- It’s not a good practice to switch around RAILS\_ENV in the test framework
- Better idea is use a method to check it and then stub that out
- Here’s an outline: [gist from Zach](https://gist.github.com/71a30f8d26928dfe9663)
- Here’s what I did: [EnvChecker](http://github.com/ultrasaurus/openlaszlo_plugin/blob/112c83bd4bc2b9f877e1326862fdc74594970f04/lib/env_checker.rb), [code](http://github.com/ultrasaurus/openlaszlo_plugin/blob/112c83bd4bc2b9f877e1326862fdc74594970f04/lib/applet_view_helper.rb#L44) and [example](http://github.com/ultrasaurus/openlaszlo_plugin/blob/67cce59b77dc8352d032ae122e318bebf8879f04/spec/applet_view_helper_spec.rb)

Stub tip
========

If you stub something and it appears not to be working, check when your module, class or method is loaded or created. Dynamic languages can be challenging. ([thanks David](http://www.ruby-forum.com/topic/187734#new))

References
==========

For more information, see

- [The RSpec Book](http://www.pragprog.com/titles/achbd/the-rspec-book)
- [rspec doc](http://rspec.rubyforge.org/rspec/1.2.6/)
- [rspec-rails doc](http://rspec.rubyforge.org/rspec-rails/1.2.6/)
- [Zach’s code review recap](http://wiki.railsbridge.org/projects/railsbridge/wiki/CodeReviewStudents)

These lessons learned while developing RSpec examples for a bug fix in [openlaszlo\_plugin](http://github.com/ultrasaurus/openlaszlo_plugin/tree/master) with help from [Zach Moazeni](http://simplechatter.com/), [RailsBridge](http://railsbridge.org/) mentor, and [David Chelmsky](http://blog.davidchelimsky.net/), on the [RSpec forum](http://www.ruby-forum.com/forum/32).