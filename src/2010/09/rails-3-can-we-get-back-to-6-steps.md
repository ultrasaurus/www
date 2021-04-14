---
title: 'rails 3: can we get back to 6 steps?'
date: '2010-09-22T02:54:03-07:00'
status: publish
exported_permalink: /2010/09/rails-3-can-we-get-back-to-6-steps
author: sarah
excerpt: ''
type: post
id: 2810
category:
    - general
tag: []
post_format: []
---
I think Rails 3 is awesome and kudos to the core team and hoards to contributors that made it happen. However, I am sad that it has gotten more verbose to create a Rails app from scratch. I know not everyone likes scaffold and not everyone uses rspec, but this is a common use case, and it gets a little worse if you use cucumber, like we do in the [workshops](http://sfrubyworkshops.com/). In fact any test framework gem dependency is going to have this kind of a problem. I teach novices periodically and frequently use scaffold in my own work for prototyping and for experimenting with new gems. The fact that I have to open up an editor and modify my gem file creates a context switch, plus I’ve got a couple of extra commands to type. There used to be 6 commands, now there are 8 to get the most basic webapp running. I think we can do better…

———– old steps ————–  
$ rails myapp  
$ cd myapp  
$ script/generate rspec  
$ script/generate scaffold note title:string content:text  
$ rake db:migrate  
$ script/server

———– new steps ————–  
$ rails new myapp  
$ cd myapp  
$ vi Gemfile

group :development, :test do  
gem ‘sqlite3-ruby’, :require =&gt; ‘sqlite3’  
gem “rspec-rails”, “&gt;= 2.0.0.beta.22”  
gem “webrat” # currently generated view specs require this  
end

$ bundle install  
$ rails generate rspec:install  
$ rails generate scaffold note title:string content:text  
$ rake db:migrate  
$ rails server

I wonder if there should be something like the git config command. Such as:

rails gem rspec

Ideally it would run the generator if there is one and edit the Gemfile. Ideally it would allow the specification of multiple gems with an optional parameter to call bundle install at the end:

rails gem rspec webrat –install

This would allow all of the goodness of bundler without the cognitive overhead (till you need it).