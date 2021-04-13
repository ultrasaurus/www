---
title: 'Scaffolds != Rails'
date: '2009-01-01T20:03:00-08:00'
status: publish
permalink: /2009/01/scaffolds-rails
author: sarah
excerpt: ''
type: post
id: 601
category:
    - code
tag: []
post_format: []
---
In pretty much every blog tutorial generate scaffold plays a central role; however, the rails guides don’t say much about scaffolding. I wasn’t sure where to go next in my development, as I asked in my [last post](https://www.ultrasaurus.com/code/2008/12/rails-2-day-4-rcov-and-bdd.html#review): “Adding attributes and other models: do I scaffold again or just write code?”

I’ve spent some time reading about scaffolding on the Rails lists, and have saved some enlightening posts from various folks. Most of the interesting discussion took place just a few months after the introduction of Rails 2 when the generated scaffold code apparently underwent significant changes to become more REST-like and the dynamic scaffold command was removed from the core of Rails (but is still available as a plugin).

What was dynamic scaffolding?

> &gt; 1) In a controller class to bind controller to its respective model as in  
> &gt; class ContactController &lt; ApplicationController  
> &gt; scaffold contact # contact here is the name of the model called  
> &gt; contact  
> &gt; end
> 
> This style of scaffolding has been removed from Rails 2.0. It used to be referred to as dynamic scaffolding, but it didn’t really help people learn about Rails or give them a way to modify the generated interface, so we killed it.  
> — nice [response by DHH](http://www.ruby-forum.com/topic/151197#667127) to a new Rails developer

Many of the Rails folks are clearly not fans of scaffolding at all and some argue that it is at best good marketing and at worst causes people to become rigid in their use of Rails. Rails is “opinionated,” but it is also designed to be flexible.

What is Scaffolding?
--------------------

> Scaffolds != Rails
> 
> They’re a starting point, and as such just give you something to start with. Scaffolds aren’t meant to be your whole application, so the code is treated just like code that’s written independent of them: If your object model changes, then you need to change your views and controller logic to match. —[ Jeremy McAnally](http://www.ruby-forum.com/topic/137337#610859)

> Just look at the generator as a secretary who can type all the “vanilla” code for you, then edit the migration to add the specifics… I need longtext for my notes fields, but the scaffold just uses text… so I always edit the migrations after they’re generated.
> 
> But listing your fields on the generate command does get those fields auto-populated into the views, letting the “secretary” do more of your typing for you.– [Ar Chron](http://www.ruby-forum.com/topic/155848#686755)

> it does what the name implies (“scaffold”, remember?), which is A Good Thing. In other news, the “preferred way of working” is still, after all those years, to actually writing code while knowing wtf is going on. — [Johannes Holzer](http://www.ruby-forum.com/topic/137337#612740)

What is Bad about Scaffolding
-----------------------------

> …scaffolding really is such an insignificant part of Rails that its flaws should have no bearing on your decision of whether or not to use Rails. Rails isn’t a visual toolkit, it’s a serious development framework. You just have to make it over two humps in the learning curve: the Rails API hump and then later the Dynamic Ruby hump and you’ll be golden. — [dasil003](http://www.ruby-forum.com/topic/137337#637101)

> my biggest problem with the new scaffolding is that it reinforces the notion that a “resource” is a controller/model stack. That, in turn, means that it discourages recognition of those cases where a resource might involve something other than a one-to-one  
> correspondence between a controller and a model.
> 
> In REST, there’s nothing about the concept of “resource” that implies database persistence, or persistence at all for that matter. Of course, Rails is a database-centered technology, not an all-purpose embodiment of every nuance of “resource”. Still, I think the  
> scaffolding presents too monogamous a picture of controller/model relations, if I may put it that way. The result is that people worry that if they do something in one controller that involves two models, they’ve done something “unRESTful”. That’s a red herring. — [David A. Black](http://www.ruby-forum.com/topic/137337#640861)

> I was confused about it; Roy Fielding (I think it was) explained it like this: a resource is like your P. O. Box; you know where it is; it never changes; and the postal workers know where it is, it never changes. But, what you’ll find in there? Whatever the postal workers  
> think is appropriate. The analogy is imperfect, because you can’t do content negotiation at your P.O.Box. Imagine if you could say, “I only want first-class mail, please, no bulk mailings, English versions if available” and then the analogy is pretty good, I think.
> 
> My very first ReST Web Service was written in Python, and serves geographic conversions for Northern Ohio. (GeoGeeks: available at http://uber.engineer.co.summit.oh.us/ws/spc3401/ ) There’s no real reason to expect anyone to request any given resource more than once, so it’s not a database, it’s just a calculation. It’s not very browser oriented. It also doesn’t do CRUD — just “R.” If I’d learned Rails 2.0 scaffolding first, I might have had even more “unlearning” to do  
> before I got straightened around.
> 
> Rails 2.0 is “ReSTish” and that’s good, but it’s still browserfied. The adaptation of ReST to the browser by Rails is very, very clever, but perhaps a little distracting. Interested people might look at [http://pragdave.pragprog.com/pragdave/2007/03/the\_radar\_archi.html](http://pragdave.pragprog.com/pragdave/2007/03/the_radar_archi.html) for an example of why providing a ReST Web Service shouldn’t be conflated (mentally) with manipulating it via the browser. — [Ron Phillips](http://www.ruby-forum.com/topic/137337#640873)

> &gt; However, as far as I could tell, Rails now makes it really hard to
> 
> &gt; deviate from RESTful approach, and that forces me, the newbie, to
> 
> &gt; stick to it.
> 
> This just described why I think scaffolding is bad. It indirectly forces newcomers to do things a specific way. If you use the scaffolding, you start building controllers based off the code there. If you learned to create a controller and views without the scaffolding, you’d be more free to do things as you see fit.– [Branko](http://www.ruby-forum.com/topic/137337#640864)

Scaffold should not Substitute for Documentation
------------------------------------------------

> Railes substitues proper “getting started” documentation for scaffolded  
> code generation which makes it really tough on newcomers. People who’ve  
> been doing Rails as long as I have don’t really care because we don’t use scaffolding. However, I work with newbies all the time and it’s much easier to start them on Rails 1.x and move to Rails 2.0 and REST later. The original scaffold generator was very good for explaining how controllers work with models and views. link\_to used a hash and not a named route. Named routes are cool, but they are confusing to a newbie. Same with  
> respond\_to.
> 
> The only upshot for Rails 2.0 scaffolding is that it’s much more production-ready. — [Brian Hogan](http://www.ruby-forum.com/topic/137337#640912)

> In training people in Rails, I definitely do not start with REST and resources. map.resources is essentially a macro that creates a bunch of named routes for you — so if you don’t know what a named route is, you can only do it in a black-box and parrot-like way. Learning named routes doesn’t make much sense until you understand routes, and routes don’t make sense until you know the basics of the request cycle… and so forth. So I would never introduce someone to Rails by telling them to write map.resources in routes.rb and trying to proceed from there. — [David A. Black](http://www.ruby-forum.com/topic/137337#640955)

Scaffold == Marketing
---------------------

> I think part of the problem is that “scaffolding” should not be part of any Rails developer’s vocabulary. Scaffolding is too limiting and “opinionated” to be useful in 99% of real-world applications. Not to mention all the RESTful issues that David A. Black has already  
> mentioned. You can’t really be RESTful AND be scaffolding.
> 
> In my humble opinion, “scaffolding” is the marketing tool to convince people to check Rails out. I know it worked on me a few years back. But, for most, it will quickly become forgotten. —[Fred](http://www.ruby-forum.com/topic/137337#640991)

Scaffold has its Place
----------------------

> Philosophically, the name scaffold was chosen early on to suggest a temporary structure upon which you can lean as you start building but one which you intend to take down as the main structure begins to sustain itself. In that regard the 2.x implementation is more sound philosophically: the scaffold exists in the early stages of development in a way that will always go away over time. — [AndyV](http://www.ruby-forum.com/topic/137337#662790)