---
title: 'rails admin interface roundup'
date: '2009-07-05T07:23:32-07:00'
status: publish
permalink: /2009/07/rails-admin-interface-roundup
author: sarah
excerpt: ''
type: post
id: 1651
category:
    - code
tag: []
post_format: []
---
After my recent [ActiveScaffold post](https://www.ultrasaurus.com/sarahblog/2009/07/getting-started-with-activescaffold/), I heard about several newer alternatives from [Jaime Flournoy](https://www.ultrasaurus.com/sarahblog/2009/07/getting-started-with-activescaffold/#comment-781), [Mike Gunderloy](http://twitter.com/MikeG1/status/2442160429), and some more [web surfing](http://ruby-toolbox.com/categories/rails_admin_interfaces.html). I evaluated four plugins for admin UI, using the following methodology:

`<br></br>rails xxx_simple<br></br>cd xxx_simple/<br></br>./script/generate scaffold Task title:string notes:text  complete:boolean<br></br>rake db:migrate<br></br>`

plus whatever annotations to the code the plugin needed. Then I ran a little script to generate 500 records:

` 500.times do |counter|<br></br>  `curl -X POST -d "Another thing #{counter}More text with #{counter} thing" -H "Content-Type: application/xml" http://localhost:3000/tasks.xml`<br></br>end<br></br>`  
They all support related models, but I only have screen shots from my simple test. I’ve listed them below with the ones I liked best at the top.

typus
-----

[Typus](http://github.com/fesplugas/typus/tree/master) is the one I’m moving forward with. It has a clean interface and has nice configuration options. You can configure which columns are displayed and which are searched (with a nice UI touch of displaying the search criteria under the search box). It is actively maintained with quite a few contributors and a responsive [google group](http://groups.google.com/group/typus). I really like how relationships are displayed (for which I don’t have a picture, sorry). The only drawback (for me) is that it has its own auth and I don’t really want to introduce a separate set of admin users for the project I am working on, and I’ll be looking into making a change to support my own auth. By default, it adds it’s own typus\_users table, but this could be a plus for some.

`<br></br>script/plugin install git://github.com/fesplugas/typus.git<br></br>script/generate typus<br></br>rake db:migrate<br></br>./script/server<br></br>```

Now visit http://localhost:3000/admin and you will be prompted for your email address, from which it will automatically create the first admin user (pretty slick). The default UI looks like this:

![](http://img.skitch.com/20090705-fkut2mh3se18h2acxbfh1msgg4.jpg)  
![](http://img.skitch.com/20090705-qxnawftfwf9na6m4eacejxy41h.jpg) I ran into just one glitch where Rails reported "A copy of ApplicationController has been removed from the module tree but is still active!" but it was [easily fixed](http://groups.google.com/group/typus/browse_thread/thread/70fba777518e26e). The error didn't happen in my simple project, but did in my real app. Francesc Esplugas has looked into it and so far [can't reproduce it](http://groups.google.es/group/typus/msg/051eff4f5089c5f9?hl=en).

admin\_data
-----------

I really liked [admin\_data](http://github.com/neerajdotname/admin_data/tree/master). The simplicity of the install was breath-taking:  
`<br></br>ruby script/plugin install git://github.com/neerajdotname/admin_data.git<br></br>sudo gem install will_paginate<br></br>./script/server<br></br>`

that's it. Now visit http://localhost:3000/admin\_data and you'll see the following interface:

![](http://img.skitch.com/20090705-gs9rwj23bdn6au6d9ahekca3te.jpg)  
![](http://img.skitch.com/20090705-cj86eyr95cjnbw1gn7k1b3taq8.jpg)

I didn't try it, but I really like the admin\_data approach to integrating with the application's authentication: Add the following lines of code in an initializer at ~/config/initializers/admin\_data.rb

`<br></br># authorization check to see if the data should be shown to the user<br></br>ADMIN_DATA_VIEW_AUTHORIZATION = Proc.new { |controller|<br></br>   controller.send("admin_logged_in?") }<br></br># authorization check to see if the user should be allowed to update the data<br></br>ADMIN_DATA_UPDATE_AUTHORIZATION    = Proc.new { |controller| return false }<br></br>`

streamlined
-----------

[Streamlined](http://streamlinedframework.org/) is nice, but not as pretty as ActiveScaffold. Not compatible with Rails 2.3. This and active\_scaffold seem to be a little older than typus and admin\_data and require you to modify your code similarly. I thought it nice that it provided its own admin layout. In my simple test I applied the series of steps and nested route as with [active\_scaffold](//www.ultrasaurus.com/sarahblog/2009/07/getting-started-with-activescaffold/).  
`<br></br>  class MyNiftyController < ApplicationController<br></br>  layout 'streamlined'<br></br>  acts_as_streamlined`

 ...\[anything else you want to do\]  
 end  
  
![](http://img.skitch.com/20090702-n3wgfmeh4wiq1k7bhfpj3fw79a.jpg)  
![](http://img.skitch.com/20090702-q77sif7axcu6f15ardfiy7panx.jpg)

active\_scaffold
----------------

See my [previous post](https://www.ultrasaurus.com/sarahblog/2009/07/getting-started-with-activescaffold/) for details. This seems to be the grand-daddy of this genre of plugins and has a very active [google group](http://groups.google.com/group/activescaffold). I liked this plugin when I first tried it, but it hung when I applied it to my real app. Also, [@jamieflournoy notes](http://twitter.com/jamieflournoy/status/2445545932) that he didn't like the UI for editing related models as much as he did Streamlined.