---
title: 'ruby application frameworks'
date: '2009-04-17T15:47:41-07:00'
status: publish
exported_permalink: /2009/04/ruby-application-frameworks
author: sarah
excerpt: ''
type: post
id: 1062
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
Panel discussion at [Golden Gate Ruby Conference](http://gogaruco.com/)

[Shoes](http://shoooes.net/), Tim Elliott, framework for creating GUI apps. It is an application that embeds Ruby. It is written in C. It is designed to lower to bar for programming and make it fun. Not an MVC framework. Writing an app is more like writing a script. Written to be compiled an shared with your friends.

[RAD](http://rad.rubyforge.org/), Greg Borenstein, open source hardware platform for doing hardware hacking. RAD is a framework for programming the Arduino physcial computing platform using Ruby. The Ruby code is coonverted into C code which is then compiled and run on the Arduino microcontroller. Working on a test suite that comes with a shoebox full of hardware, so you can check if things blink or bleep in the right order to see if your tests pass.

[Adhearsion](http://adhearsion.com/), Jay Phillips, a way of building telephony applications. You call into a phone number, then the Ruby call services the phone call. First app he wrote was using RAD to make it so he could make a phone call to unlock his door — he says everyone should go out and buy an Aduino controller and a bunch of LEDs and build something fun tonight. Interesting thing about Ruby is that it allows you to “play with other people’s code.” He described a plugin system that was actually adopted from RAD.

[Sinatra](http://www.sinatrarb.com/), Blake Mizerany, creator of Sinatra. Sometimes MVC is too much. Ruby is great for this. Closures are awesome. As Rack grows, Sinatra has been getting smaller. Sinatra is a really strong Rack citizen.

Merb, Yehuda Katz lead maintainer. (not talking about Merb) Hard thing about maintaining a framework is that they start with a clear mission, but as people build apps with the framework, there are requests where its hard to tell if this request is pushing application code into the framework The best thing about Ruby is that all code is executed code. You can define methods anywhere. What is hard about Ruby. It isn’t a slow language, but nothing is free. The challenge is how to right lightweight code, yet is robust.

Rails, Josh Peek from the Rails and [Rack](http://rack.rubyforge.org/) core teams. … interested in seeing how code can be shared between frameworks to strengthen the ecosystem.

**What features of the Ruby language make it effective for frameworks?** meta-classes and closures (e.g. ActiveRecord), “i don’t consider languages without closures to be powerful languages” (yehuda katz), defining methods on the fly, open classes, community (grass roots, people agree that they want to share code, this is unusual, agility in the community: moving to git and github, Rack, Ruby gems, RSpec, test-driven development as part of the project), the agility of the community attributed to the agility of the language.

**Is there anything about Ruby that encourages open source?** the fact that it is a scripting language. It is hard to hide your code. The fact that Rails and Ruby are MIT Licensed, so corporations aren’t afraid to use it. Even if 90% don’t give back, it increases the number of people who do. Makes it so people feel free to try stuff out and modify it (and the fact that there are tests!) There is high level of inter-operability with the “host language” for different Ruby implementations.

“If you are writing a framework, you should be writing it in the same way that you recommend people write plugins. It’s really hard, but you have to do this.” — Yehuda Katz

“Allowing people to write test for their plugins is essential.” — Jay Phillips

**What about the proliferation of Ruby implementations in different languages?** kick-ass, as long as we keep holding the implementations to a high standard of compatibility.

**Why was github so successful? Why did so many projects move to git and to github so quickly?** main benefit of github is the social network aspect. When you put your code up on github, you aren’t creating an open source project, you are just sharing your code. This decreases the overhead. It increases people contributions. “I think it has totally revolutionized the way people create open source software” (Jay Phillips) Moving to git let’s you make really large changes and merge them back. Things that are possible in git, would have been impossible in svn — you would fork forever instead of merging back in. (Yehuda Katz)

**How to get the community to move to Ruby 1.9?** get Rails to be on 1.9. **Why do you want the community on 1.9?** speed improvements. Yehuda Katz: If you are doing something computationally expensive you might want to be on 1.9. I benchmark everything. Usually 1.9 is 2x and JRuby is 2.5x, but 1.9 has outliers of slowness. I don’t think there is huge benefit to the community in moving to 1.9 (but I do think it is important that we all do move forward) Jay Phillips: when JRuby and all the gems move to 1.9, the community will. If I switch to 1.9 syntax, I will break JRuby, and I can’t do that.