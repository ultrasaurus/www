---
title: 'freedom in ruby and code'
date: '2010-11-16T06:37:52-08:00'
status: publish
permalink: /2010/11/freedom-in-ruby-and-code
author: sarah
excerpt: ''
type: post
id: 2922
category:
    - general
tag: []
post_format: []
---
After my [last post](https://www.ultrasaurus.com/sarahblog/2010/11/seek-to-inspire/), I had a twitter conversation with @dhh about his talk and my reflections on it. I’m still not sure he understands that his talk wasn’t “weird-cool” like his example of \_why, nor do I think it was an example of “weird-angry” that the Ruby community would disdain. Instead it is an alternate brand of weird, on the verge of weird-creepy — over the top for some, but merely boring and off-topic for me. I heard from one person via email that the keynote (and some panel I didn’t attend) caused a first-time RubyConf attendee to feel out of place at the conference — not likely to attend again. I didn’t get a sense of leaving in a huff, rather that this was a closed community with an in-crowd and a sense of humor not shared. I believe there a wide space between delightful and avant-guard experimentation in code and art, and the status quo of corporate America. However, David Hansson and others seem to fear that if they can’t use NSFW language and metaphor that soon we’ll all be wearing suits to RubyConf and the wild creativity of the Ruby community will be stifled. I think not.

I do believe Dave when he says that he sought to inspire…  
[![I can't imagine a more inspiring topic than freedom. I was certainly fired up! But glad you liked Dave Thomas' talk.](http://img.skitch.com/20101116-pphxp3iwbue6ytn8bf1f9sat67.png "freedom is inspiring")](http://twitter.com/#!/dhh/status/4268662210957312)

Over twitter, he re-stated his thesis for me:  
[![@ultrasarus tweet: @dhh wondering.. did you have a call-to-action in mind? or just that we should appreciate (defend?) our Ruby freedoms? sorry if I missed it / @dhh replies: @ultrasaurus If you don't know and appreciate the freedoms that you have, you're much more likely to casually lose them.](http://img.skitch.com/20101116-b1nj3ecaq5816k5qrjrrkmgcq4.png "@dhh reply on twiter")](http://twitter.com/#!/dhh/status/4285649351868416)

What does freedom mean with respect to code?
--------------------------------------------

David referred to [Maslow’s Hierarchy of Needs](http://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs), suggesting that there is a parallel hierarchy of programming languages. I think assembly language should be considered the bottom of the pyramid, since it allows programs to survive using a primitive communication with the machine and agree that Ruby supports the top of the pyramid.  
![Maslow's Hierarchy of Needs](http://img.skitch.com/20101116-je6b6738eh31k7pep9hqq3c7qw.medium.jpg)

### Self-actualization

The top of the pyramid includes: morality, creativity, spontaneity, problem solving, lack of prejudice, acceptance of facts  
Examples:

- Open / Dynamic language (spontaneity and creativity)
- Strong support for and widespread practice of testing supports (lack of prejudice, acceptance of facts)
- Ruby Gems allows for experimenting with new versions of libraries
- rubygem.org and gem push (creativity, spontaneity)

### Esteem

The next level includes: self-esteem, confidence, achievement, respect of others, respect by others. These aspects are in some ways strongly supported by the community where there is technical support for publishing our work and strong systems of acknowledgment.  
Supporting Examples:

- Ruby Gems 
  - Gem specification with author attribution
  - rubygems.org download stats
- GitHub 
  - free for open source projects
  - fork
- Blogging, Ruby Meetups, Regional Conferences: diverse venues and respect given to people who publish words as well as code, and who talk about their work

Where we still need work:

- respect by others: there is a difference between playful and juvenile, growing up doesn’t mean becoming like our parents, we can take responsibility for our actions and our impact on others and still have fun
- respect of others 
  - We’ve made great strides in the last year or two with the diversity of Ruby VMs to support various technical communities. Java, at times reviled by members of our community, can also now be appreciated for its JIT and other tools with JRuby. As Matz noted, diversity is tough, but worth embracing.
  - We still need to do a lot of work on making Ruby work for people who run Windows. It is not particularly helpful to tell someone who wants to experiment with Ruby that they need to buy new hardware.
  - Sexism and racism still exist. At its best, open source is a meritocracy. At worst, it is a white boy’s club. Go out of your way to not be *that guy*.

Defending Freedom of Code
-------------------------

I agree that the Ruby community uses the freedom of the Ruby language to great benefit. As the community grows, we are in danger of settling into patterns established by our pundits or the conventions of last year’s gems (which reflect last year’s thinking). Each of us needs to understand the core principles by which we code and practice those, in order to retain our freedoms. I’d like to share some examples that would have worked better (for me) in the keynote, which could have been suitable replacements for what I felt were off-topic metaphors.

One of the points David Hannsson made in his keynote is about the freedom from declaring types. It reminded me of Oliver Steele’s article [Test vs. Type](http://osteele.com/archives/2003/08/test-versus-type) — originally referencing JavaScript and Python, but the same principles apply to Ruby. David talked of critics who speak of “enough rope to hang yourself” and asked, rhetorically, if hanging was really the most common use case for rope. Should we focus on preventing one rare use case rather than supporting all of the other useful ways to use rope? Instead of being afraid of what liberty allows, we can provide effective measures to protect ourselves. With Ruby, we do that by having strong technical and social support for testing.

The Ruby test framework explosion in the past few years has been a bit overwhelming to many of us and was at first addressed by blog post tutorials and talks at meetups and conferences. Many Rubyists have also worked hard to support the freedom to use your test framework of preference. Here are some examples:

- Cucumber auto-detects and configures itself based on whether you have webrat or capybara installed
- Rails 3 has plug-in generators so that any test framework can generate its own tests for scaffold, model, etc.
- Rspec lets you configure what mocking library you want to use.

In general, Rubyists value freedom of choice. When we can easily experiment with different frameworks and libraries, we can make well-reasoned decisions without overly valuing the status quo. As software developers, we need to work hard to overcome inertia in order to move forward and continue develop great code year after year. A few more examples:

- Rack: allows us to mix and match web servers
- Rails 3 Routes can be any Rack endpoint, allowing us to mix Rails and Sinatra in the same web app (and potentially other frameworks)

I’d be interested in hearing about other examples of how Rubyists are using the flexibility and freedom that are inherent in the language to create an ecosystem that protects us from the inherent risks, defends those freedoms and promotes programmer happiness and creativity.