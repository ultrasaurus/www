---
title: 'customer-driven development'
date: '2017-06-19T06:08:36-07:00'
status: publish
exported_permalink: /2017/06/customer-driven-development
author: sarah
excerpt: ''
type: post
id: 6276
category:
    - general
tag: []
post_format: []
---
Sometimes when I talk about customer use cases for software that I’m building, it confuses the people I work with. What does that have to do with engineering? Is my product manager out on leave and I’m standing in?

I’ve found that customer stories connect engineers to the problems we’re solving. When we’re designing a system, we ask ourselves “what if” questions all the time. We need to explore the bounds of the solutions we’re creating, understanding the edge cases. We consider the performance characteristics, scalability requirements and all sorts of other important technical details. Through all this we imagine how the system will interact. It is easier when the software has a human interface, when it interacts with regular people. It is harder, but just as important, when we write software that *only* interacts with other software systems.

Sometimes the software that we are building can seem quite unrelated from the human world, but it isn’t at all. We then need to understand the bigger system we’re building. At some point, the software has a real-world impact, and we need to understand that, or we can miss creating the positive effects we intend.

On many teams over many years, I’ve had the opportunity to work with other engineers who get this. When it works there’s a rhythm to it, a heartbeat that I stop hearing consciously because it is always there. We talk to customers early and often. We learn about their problems, the other technologies they use, and what is the stuff they understand that we don’t. We start describing our ideas for solutions in their own words. This is not marketing. This influences what we invent. Understanding how to communicate about the thing we’re building changes what we build. We imagine this code we will write, that calls some other code, which causes other software to do a thing, and through all of the systems and layers there is some macro effect, which is important and time critical. Our software may have the capability of doing a thousand things, but we choose the scenarios for performance testing, we decide what is most normal, most routine, and that thing needs to be tied directly to those real effects.

Sometimes we refer to “domain knowledge” if our customers have special expertise, and we need to know that stuff, at least a little bit, so we can relate to our customers (and it’s usually pretty fun to explore someone else’s world a bit). However, the most important thing our customers know, that we need to discover, is what will solve their problems. They don’t know it in their minds — what they describe that they think will solve their problems often doesn’t actually. They know it when they feel it, when they somehow interact with our software and it gives them agency and amplifies their effect in the world.

Our software works when it empowers people to solve their problems and create impact. We can measure that. We can watch that happen. For those of us who have experienced that as software engineers, there’s no going back. We can’t write software any other way.

Customer stories, first hand knowledge from the people whose problems I’m solving spark my imagination, but I’m careful to use those stories with context from quantitative data. I love the product managers who tell me about rapidly expanding markets and how they relate to the use cases embedded in those stories, and research teams who validate whether the story I heard the other day is common across our customers or an edge case. We build software on a set of assumptions. Those assumptions need to be based on reality, and we need to validate early and often whether the thing we’re making is actually going to have a positive effect on reality.

Customer stories are like oxygen to a development team that works like this. Research and design teams who work closely with product managers are like water. When other engineers can’t explain the customer use cases for their software, when they argue about what the solution should be based only on the technical requirements, sometimes I can’t breathe. Then I find the people who are like me, who work like this, and I can hear a heartbeat, I can breathe again, and if feels like this thing we are making just might be awesome.