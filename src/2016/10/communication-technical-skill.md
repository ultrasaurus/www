---
title: 'communication is a technical skill'
date: '2016-10-04T20:57:54-07:00'
status: publish
exported_permalink: /2016/10/communication-technical-skill
author: sarah
excerpt: ''
type: post
id: 6070
category:
    - general
tag: []
post_format: []
---
(11/16 update: [full video](https://www.youtube.com/watch?v=coye0AllVuY) now online)

For Rocky Mountain Ruby last week, I opened my talk with inspiration from Jim Weirich, a legendary developer, inspiring teacher and a great communicator. The short video clip was from a prior Rocky Mountain Ruby, where Jim Weirich shared a song he had composed for [\_why day](https://engineering.shopify.com/17488384-whyday-is-friday):

https://www.youtube.com/watch?v=8yoTHh6D9R0

Here are my notes from the talk which aren’t exactly what I said, but provide a bit of the story…

The ruby community has a lovely culture of openness where people share their work publicly with permissive open source licenses, providing the opportunity for serendipitous collaboration. We actively invite people to use our gems with easy installation steps, documented on clean easy-to-read home pages. We showcase whimsical code snippets hoping to inspire developers, peak the curiosity of someone new or just share our joy in our new creation. As with Jim’s song, we love sharing our code, and we like to read and learn from code written by other developers.

Just in case you think this kind of effort only makes sense for mature projects like Bundler and Sinatra, I picked a random repo from one of my favorite developers, [Sarah Mei](https://twitter.com/sarahmei): a small app [embloggen](https://github.com/sarahmei/embloggen) with 33 commits, developed over just a few days. The application took shape in the first day with 14 commits, and we can see that she wrote a README on that same day.

And this isn’t a unique process. I took a look at Jekyll, a popular static website generator, written in Ruby that now powers github pages. It has over 8000 commits and 625 contributors. I went back in time to 2008. There was no README that first day, but a couple of weeks later, we see a description of AutoBlog. It is still something that is only used for this developer’s own use. I’m not sure what “blog like a developer” is supposed to mean, but its a start, and there are install instructions and a license. That starting point must have made it easier to iterate a month later, with a better explanation of what it is and how it works. The README is starting to be friendlier, and more clear, but still geared mostly for a developer audience, which communicates something about the state of the project as well.

**We usually think of software as being made of code, but it is really made of people.** We imagine what the software should do, and through our code, we turn ideas into reality.

I chose three example of what I think of as good communication — some that I have participated in or that I merely witnessed. I believe the best communication has three parts:

1. Big Vision
2. Concrete Step
3. The Path

Don’t be afraid to communicate your big vision. How will the future change because what you are creating exists? What will it feel like when you get there? Then… what are the small concrete parts that people can experience now which make them believe, and cause them to understand that it is possible. Finally, connect the dots. Describe the path where all the small parts, the ones that exist now and the ones yet to come add up to changing the world!

Bridge Foundry
--------------

Bridge Foundry has a vision of the future where the makers of technology are reflective of our society, where all people have equal access. This is not only the right thing to do from a fairness perspective; we also believe that the only way we will solve the very real and critical problems of our time is to leverage all of the talent and potential available on this planet.

One of the key activities of this organization are workshops where we outreach to women and underrepresented minorities and teach coding, with a specific language or framework.

It seems simple, but it is a carefully designed experience that was co-created by our early volunteers and students. We always seek to involve a diverse teaching and organizing team. We offer childcare, and make sure there is plenty of good food. If installation is needed, we get that out of the way the night before.

Then students can focus on learning to code in a full day, where every need is met, and they feel supported. Students and volunteers alike often think this is about learning the process of coding, the syntax and the patterns, and it is, but the primary thing we are doing is sharing this culture: our joy of coding and working together collaboratively. This is the culture that most of us live every day at our jobs, but it is invisible to those outside the industry, and is sometimes surprising to those who only know tech culture from headlines or TV.

Through the workshops and participation in our local meetup, we demonstrated results at a small scale, we iterated, and measured impact. We found that individuals taking the small step of teaching weekend workshops could see it happen. They were inspired by making an impact on just a few people, and we shared the information about how the effects were adding up. In just 6 months, our local SF Ruby meetup went from 2% to 18% women. We illustrated the path from the simple step of volunteering, teaching what you know in a fun weekend experience, to changing the industry.

Firebase
--------

Next I will share an example from the business of building a software product. In my new job, I work on the Firebase team.

The Firebase Product Manager, James Tamplin, gets up every other week in front of the whole team to give us product and customer updates. He starts every meeting by saying that we are working to “help developers build better apps and grow successful businesses.” And that’s great, it keeps us aligned internally, but I wondered… now that we’re inside Google can we communicate that mission as effectively? So I googled “Firebase mission” and could only find pre-acquisition statements… and then… I noticed on our [home page](https://firebase.google.com/)… there it is:

“*App success made simple* The tools and infrastructure you need to build better apps and grow successful businesses”

For an outsider, it looks like marketing fluff, but it’s not. This is our mission. It is not enough to just say this words. We need small things we can do to align the team in building toward this vision. You can’t see it from the outside, but I think it adds up to a difference you can feel. We have these practices, which I believe are key to making this vision a reality.

Our whole team has this relentless focus on the first fifteen minutes of the developer experience. Throughout the development process, in meetings or spontaneous conversations, someone will ask “how does this affect the initial experience?”

One of my colleagues, Joey Yang, told me a bit more detail about this developer experience that is so important to the Firebase team. He described the user experience as the “sum total of every interaction the user has about the product.”

It’s not just our code and documentation, it’s social media and stack overflow. It’s not jut your blog, it’s other people’s blog posts. Someone’s first fifteen minutes might be interacting with another person in the community who is not you! Or it might be through your github repo, conference talks, meetups or hackathons.

“Your product is not just your code — if it takes you more than five minutes to get up and running, then you will spend your time elsewhere” — Joey Yang

I first met Firebase team in May 2012 at a hackathon. I had no idea at the time that I was experiencing a company philosophy! I later learned that they had a policy that “even if you weren’t using Firebase, we would help you out… even if you were using a competing product. Generating good will from the interaction was important to us.”

So my team was at AngelHack back in 2012 making an app that let people sketch 3D shapes in the air. Firebase helped us send paths to the server instantly, to be rendered on a webpage with WebGL. This was just a hobby app, something delightful and fun, a way to stretch our developer skills and our imagination. Firebase treated us with as much reverence and excitement as they did people who were building a business on their product. They invited us to their launch. They showcased our success. Of course, we knew that this was their success as well, but we were center stage.

Rack
----

I started learning Ruby on Rails in December 2008. Rails 2.2 had just been released. I witnessed the adoption of Rack by Rails and by all of the Ruby frameworks. As a developer in the community, it felt like one day, everyone decided that Rack was a good idea, and then everything just got easier. I don’t know the actual history, but I did a little research and was intrigued by what I found.

In February 2007, Chris Neukirchen wrote a blog post [introducing rack](http://chneukirchen.org/blog/archive/2007/02/introducing-rack.html).

> I noticed that there is a lot of code duplication among frameworks since they essentially all do the same things. And still, every Ruby web framework developer is writing his own handlers for every webserver he wants to use.

He observed that HTTP is actually quite simple and expressed it as a simple API:

```

class HelloWorld
  def call(env)
    [200, {"Content-Type" => "text/plain"}, ["Hello world!"]]
  end
end
```

This is actually a very simple Rack application. Chris presented something which could be adopted rather easily, and when adopted by a single web server was not that revolutionary, but with each server and framework that adopted it, it became easier for everyone. It didn’t need to be adopted all at once to save time and effort. It was a good idea. It was really *only* an idea. He did write some helper libraries, but no one had to use them.

Rack was just an idea, a thought, that simplified the approach to connecting different pieces of web software.

Communication is What We Do
---------------------------

I find it confusing that anyone could even suggest that communication is a different skill that is optional for programmers. This is what we do. We write our code in programming **languages**. We define things and then they exist. We make real things using language.

When I was a kid, I wanted to be a wizard, with magic where you could know the name of a thing, sketch it in the air and make it real. We do that with software. When we write code, we simply define a thing and run the code, to make it real.

“Wizards channel arcane forces through extensive study, hidden knowledge, and intricate preparation. To a wizard, magic is an art form, an expressive and powerful method by which he or she seeks to control the world around them” — <http://mortal-affairs.wikia.com/wiki/Wizards>

New Languages
-------------

There seems to be an explosion of new languages or old ones that people are suddenly using more often. This seems driven by combination of fast processors and new problems of building distributed systems that require better handling of concurrency, and new user experience patterns with mobile and all sorts of connected devices.

To understand what these new languages are for, it helps me to think of them in context of history and language design trends. This invention is a conversation between the past and the future we’re creating. Software developers exchange ideas through experimentation.

Closing Thoughts
----------------

Learn a new language. Make a new language. Code is communication. Figure out what you want to say: make things that communicate your intention. Experiment! Maybe you can make the thing that will give us all new magical powers.

slides:

<iframe allowfullscreen="" frameborder="0" height="356" loading="lazy" marginheight="0" marginwidth="0" scrolling="no" src="https://www.slideshare.net/slideshow/embed_code/key/3ZQNVhs6OtUpfh" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" title="Communication is a Technical Skill" width="427"> </iframe>

<div style="margin-bottom:5px">  **[Communication is a Technical Skill](https://www.slideshare.net/sarah.allen/communication-is-a-technical-skill "Communication is a Technical Skill")**  from **[Sarah Allen](https://www.slideshare.net/sarah.allen)**</div>