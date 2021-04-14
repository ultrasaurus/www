---
title: 'sf ruby meetup'
date: '2009-04-03T20:00:49-07:00'
status: publish
exported_permalink: /2009/04/sf-ruby-meetup
author: sarah
excerpt: ''
type: post
id: 976
category:
    - general
tag: []
post_format: []
---
Last week I attended the [March SF Ruby Meetup](http://www.meetup.com/sfruby/calendar/9781300/). (Some day I hope to attend a meetup where I don’t personally double the number of women, but at least I wasn’t all alone, and the guys treated me as more of a geek than a girl, which is always a good sign.) I found the talks engaging and learned a few things.

There were three short talks (see notes below):

- [CellGuided](#cellguided)
- [Heroku](#heroku)
- [GitHub](#github)
- [Announcements](#announce)

<a name="cellguided">  
</a>

<a name="cellguided">CellGuided</a>
-----------------------------------

Rajiv Aggarwal has created a treasure hunt application [Cell Guided](http://www.cellguided.com/). Rajiv generously shared details about what it took to build it and highlighted the various libraries and APIs he used for mapping and geo-coding.

Geocoding using [GeoKit](http://geokit.rubyforge.org/) (requires Google API Key)

- from street address: GeoKit::Geocoders::Muitgeocoder.geocode
- from ip address: GeoKit::Geocoders::IpGeocoder.geocode

extends ActiveRecord

```
Whatever.find(:all, :origin => [37.39, -122.39], :within => 50)
Whatever.find(:all, :origin=>'100 Spear st, San Francisco, CA', :within=>10)
```

Maps using [ym4r](http://ym4r.rubyforge.org/)

Displays static or dynamic maps that you can interact with. For printing, couldn’t use the same API (since sometimes the Javascript wasn’t done by the time the print happened, sometimes the map would be blank), instead using the static map API worked.

They use a ‘QR code’ on the flyer to encode the URL of the website. Pretty cool. Aside from an audience member: McDonalds in Thailand uses it on the packaging to tell you how many calories are in that food item!

Q: How much Javascript did you have to write? “about a page”

<a name="heroku">  
</a>

<a name="heroku">Heroku</a>
---------------------------

Adam Wiggins, one of the co-founders of Heroku, demonstrated how easy it is to deploy a Ruby on Rails app to Heroku and talked about some additional neat features, as well as their (not yet final) plans for pricing the service.

- instant Ruby deployment
- deply integrated thru Ruby gem &amp; git

how to:

1. get heroku account
2. sudo gem install heroku
3. automatically adds a git remote

you can use your own URL if you like, but by default it will make one up for youto make it easy to experiment. memcahce in beta right now. ‘heroku console’ will give you access to the console. The severs are locked down at the Unix level: filesystem is read-only now and git submodule hacks won’t work anymore.

gem support?

- can vendor rails, but doesn’t work with binary gems
- create a .gems manifest
- coming from rubyforget, just add the name of the gem

What if RubyForge doesn’t have it yet?  
my-gem –source http://mygem.myserver.com

Rmagick? all installed, other gems that depend on OS binaries: email us

Q: how do you get your data in and out? A: taps .. streaming database import/export

How to move data from your database to heroku…

heroku db:push

you can also do:  
heroku db:pull

backup? EC2 – tripple re-dundant. You should keep your own backups, of course. They provide some tools. Also heroku bundle:capture

They have tested high traffic, easy to scale, built into the architecture. You’ll be sharing a db on the free apps.  
You would pay to have a dedicated database. You get 1-2 mogrel/thins for free, higher for pay. You could crank it up to 8 just for a day, easy command line control. Can you specify limits? analogy to google ad words, set a budget… still working out the details, which is one of the reasons we aren’t publicly posting pricing.

All 2.0 series of Rails are installed. If you want something else you can always vendor it.

Uses postgres.. not mySql

<a name="github">GitHub</a>
---------------------------

Chris Wanstrath from [GitHub](https://github.com/) gave an entertaining and detailed talk about the lesser known features of github. I was one of 2-3 people in the audience (of about 60-70) who raised their hands in answer to the question “who doesn’t have a github account?” Sitting near the front Chris challenged me to tell him what I didn’t like about GitHub. I had no gripes about the site, but hadn’t seen a reason to use github and had merely set up a remote repository on a dev server when needed to collaborate. Of course later in the week I realized I did have a GitHub account, I just wasn’t using it for posting. There’s probably no way you can write Ruby on Rails code for even just a few months and not have \*some\* reason to have an account on GitHub. After hearing Chris’ talk, I did have second thoughts about not using GitHub for my shared git repository. GitHub seems well-worth the price of admission with cool features for collaborating on shared code. Here are some highlights:

Cool visualizations  
(click on the images to link to the live graphs)

“Punch Card” graph, commit activity by day and hour:  
[![](http://img.skitch.com/20090404-cinaf3y46et54prptu47gkcngn.jpg)](http://github.com/defunkt/github-gem/graphs/punch_card)

Blocks represent “impact”. Impact is (lines added + lines deleted) for all non-merge commits during a week period.  
[![](http://img.skitch.com/20090404-fd8as1kwuc214fn7ff7e27mt7f.jpg)](http://github.com/defunkt/github-gem/graphs/impact)

Network Graph Viewer  
[![The github-gem Network - GitHub](http://img.skitch.com/20090404-6uwjqc9cspcrxg36yk7yxpjji.jpg)](http://github.com/defunkt/github-gem/network)

They also use rubanalytics to create a [view of page traffic](http://github.com/defunkt/github-gem/graphs/traffic) (based on the google analytics they were already using for githb).

Looking at source code…  
shift-select – highlight a section of code and send a URL  
l &amp; h, key nav for pagination  
on commits page, j &amp; k, c for commit

on a commit… on the URL, add .patch or .diff  
can wget the .patch, can apply it

Fork Queue — I guess only admins have it

They have a bug tracker in development. Lightweight, simple priority, modeled after gmail, same keyboard shortcuts.

Chris talked in detail about various implementations of a “job queue,” apiece of work that can be done in the background by a persistent worker. Nice presso, sorry no notes. Heroku doesn’t support this yet… working on it. Noted “workling” an emerging Rails plugin.

Odd langugage quote of the evening “We didn’t have to tie up the mongrel” (to a different audience this would mean something quite different!)

<a name="announce">Announcements</a>
------------------------------------

[CodeCon](http://www.codecon.org/2009/) – unconference, for hackers by hackers  
April 17-18