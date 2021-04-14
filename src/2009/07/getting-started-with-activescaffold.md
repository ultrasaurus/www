---
title: 'getting started with activescaffold'
date: '2009-07-01T22:32:09-07:00'
status: publish
exported_permalink: /2009/07/getting-started-with-activescaffold
author: sarah
excerpt: ''
type: post
id: 1621
category:
    - code
tag: []
post_format: []
---
The [ActiveScafold](http://activescaffold.com/) plugin for Rails promises to be a huge time saver. In just a few easy steps, you can create a full web interface for your database, complete with inline editing and fold out panels. Of course, it helps to have some grasp about what it is doing or you can get [stuck like I did](http://groups.google.com/group/activescaffold/browse_thread/thread/bb541afdf9acda3) this morning. I’m no expert (yet), but since it is so very cool, I wanted to share what I’ve learned (with the help of Sean Dick and Ivan Storck at tonight’s SFRuby Hack session).

After installing the plugin, there are just 3 lines of code that magically generate the HTML pages, but the trick is knowing where to put them. There’s a [nice intro](http://wiki.github.com/activescaffold/active_scaffold/how-to-approach-active-scaffold-use-cases-benefits) on the github wiki that outlines common use cases:

- Prototyping
- Admin Interfaces
- Embedded, Widget-Style
- Data-Heavy Applications

The use case that led me to ActiveScaffold today was the creation of an admin interface. I’m working on a website and the end user stuff is pretty nice, but there are a bunch of tables where the data needs a little love… no one wants to launch the site without at least a few corrections in the data and it is crazy to either delay the launch while we build an admin interface or have an engineer make corrections with sql updates. Enter ActiveScaffold: a way to allow admins to make the changes they need with very little software development. (Later I expect we’ll need to add some fancy bits to the admin interface, but ActiveScaffold promises to be configurable and extensible enough when the time comes and the key point is that I don’t expect to need those features this week.)

ActiveScaffold for Admin
------------------------

Make a little app for this experiment:  
`<br></br>rails active_scaffold<br></br>cd active_scaffold<br></br>./script/generate scaffold Task title:string notes:text  complete:boolean<br></br>rake db:migrate<br></br>`  
Install the plugin, which is compatible with Rails 2.3.2 (yay!) and previous versions of rails (if you [install a specific revision](http://wiki.github.com/activescaffold/active_scaffold/getting-started))  
`<br></br>./script/plugin install git://github.com/activescaffold/active_scaffold.git<br></br>`  
Now we have an app that lets you create, view, edit and delete tasks. This is the end-user app, you could edit the views and remove controller actions to prevent editing, deleting and/or creation. We want to leave this interface as is, but create a separate set of pages to allow an administrator to view, create, modify and delete tasks.

Sean came up with the idea of using routes with a namespace to facilitate this. Here’s what we came up with:

In config/routes.rb add the following code:  
`<br></br>  map.namespace :admin do |admin|<br></br>   admin.resources :tasks<br></br>  end<br></br>`

Create a copy of /app/views/layouts/tasks.html.erb and call it admin.html.erb (in same folder), then add the following lines inside the &lt;head&gt; tag:  
``

Create app/controllers/task\_controller.rb:  
`<br></br>class Admin::TasksController < TasksController<br></br>   layout "admin"<br></br>   active_scaffold :task<br></br>end<br></br>`

Check it out:  
`<br></br>http://localhost:3000/admin/tasks<br></br>`  
![](http://img.skitch.com/20090702-tgy9a9y5g981xf589k6b3txjym.jpg)  
and when you click edit:  
![](http://img.skitch.com/20090702-mm8tr6jceckp7y78kbc495nwnq.jpg)