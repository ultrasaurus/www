---
title: 'jruby on google app engine'
date: '2010-05-04T22:26:33-07:00'
status: publish
exported_permalink: /2010/05/jruby-on-google-app-engine
author: sarah
excerpt: ''
type: post
id: 2649
category:
    - general
tag: []
post_format: []
---
![app engine logo](http://rails-depot.appspot.com/images/appengine_ruby.png)John Woodell ([@johnwoodell](http://twitter.com/johnwoodell)) gave an excellent talk at the [App Engine Meetup](http://www.meetup.com/appengine/calendar/13303709/) this evening on using Ruby on Google’s AppEngine. After some highlights of App Engine and a tour of three real-world use cases, John gave a series of quick demos of what seem to be very well-documented resources for getting started. I built the simple “hello” Sinatra app during his talk which was pretty satisfying. I was distracted by my success with the first app, so I missed some of his Rails presentation, but it looks like the docs go through what he demo’d.

Overview
--------

Key Features

- No need to install or maintain your own stack
- “We do the scaling for you” -&gt; Google services via standard APIs
- Charge only for actual usage – Always free to get started
- Built-in application management console (pretty sweet)

Gotchas

- no native code
- no sockets or thread
- no writing to the files system
- 30 seconds to do your work, then the request times out (issues with initialization in Rails, but they’ve developed a “deferred dispatch” workaround)
- takes several seconds to “spin up” a new JRuby instance when your app first starts or your load spikes

Good things to know

- AppEngine datastore has no schema.
- Reads are always the same speed no matter how big your data store, writes are slower
- You use **DataMapper** rather than ActiveRecord.
- memcache API is available
- URL Fetch API is a drop-in replacement for Net::HTTP
- as of today, there will be a release where openssl “just works” for the first time

Matthew Blain, the engineer for the main bulkloader tool, gave a short talk about it. Bulkloader lets you put data into the AppEngine data store. You can use it to import data or to move from one AppEngine app to another. It currently supports limited input: csv and simple xml. It also supports “simple text” for output. You can write any connector you want.

Some real world references to people using Ruby on App Engine:

- [real world app using JRuby, Rails and App Engine](http://azazeal.xelixis.net/post/Starting-your-business-in-less-than-a-week-with-Rails-on-Google-App-Engine.aspx) ([azazeal](http://twitter.com/@azazeal))
- <http://www.codingforrent.com/>
- iPhone / iPad app with JSON interface: [blog post](http://www.johntwang.com/blog/2010/04/23/json-with-ruby-on-rails-on-google-appengine/) and [gist](http://gist.github.com/377353) by John Wang   
  \[update from John Woodell’s comment\]

Very nice [getting started guide](http://code.google.com/p/appengine-jruby/wiki/GettingStarted), which I followed to build a Sinatra app in about 5 minutes.

```
sudo gem install google-appengine
appcfg.rb generate_app hello
dev_appserver.rb hello
```

After this I had an app running locally at http://localhost:8080/ — I find it unsettling to hear that the dev app is running on whatever Ruby I have, but when I deploy it is JRuby. John reassures me that the only real glitch that I’ll run into is if I have a gem with native code, for which there aren’t also java extensions (or an alternate pure Ruby implementation).

Installation notes: hasn’t been tested with rvm, the env is there, so you don’t need it. gems are stored in a jar file, kept in .gems/bundler\_gems in your app directory

Then to deploy my app on App Engine, I needed to use my Google account to register an app. I picked the name “hello-sarah” which I then added to my config.ru. I also added a little snippet of Ruby code to the Rack app to report the current time, so I could tell it was mine.

![](http://img.skitch.com/20100505-kfetd3f8wsex4mradgc94s8m56.png)

Then I typed some magic words into my local command line:

```
cd hello/
appcfg.rb update .
```

Then my app was live at: <http://hello-sarah.appspot.com/>

Since I tweeted it, I got a chance to see how the application dashboard works. Here’s what it looks like for this app which was first deployed a few hours ago:  
![dashboard](http://img.skitch.com/20100505-fcre698bqgtxrw6bf2p298htwe.png)