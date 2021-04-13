---
title: 'rails 2 day 4: rcov and more behavior-driven development'
date: '2008-12-29T09:39:07-08:00'
status: publish
permalink: /2008/12/rails-2-day-4-rcov-and-more-behavior-driven-development
author: sarah
excerpt: ''
type: post
id: 600
category:
    - code
tag: []
post_format: []
---
Today, we’ll follow modified steps, as recommended by [Matt Wynne](http://blog.mattwynne.net/) who suggested [refactoring to remove duplication](http://www.ruby-forum.com/topic/174015#762387) as an extremely important step:

1. Describe a feature
2. Execute the feature and Watch it fail
3. Write the code to make it pass
4. Refactor
5. Go to step 2

Also, since we’re using the generate scaffold command, we should remove unused code when refactoring as suggested in the original [Four Days on Rails](http://rails.homelinux.org/) tutorial. I’ll also be using RCov to look at how much the feature description covers the code. I think this is a helpful way of digging into what the scaffold command actually did. This tutorial picks up where [day 3](https://www.ultrasaurus.com/code/2008/12/rails-2-day-3.html) finished. You can skip day 1 or 2, if you already have installed Ruby on Rails and know a little bit about it.

Today we will:

1. [Install RCov](#install)
2. [Look at Code Coverage](#coverage)
3. [Write more scenarios](#more)
  1. [Create](#create)
  2. [Edit](#edit)
  3. [Delete](#delete)
4. [Refactor to remove duplication](#refactor)
5. [Review what we learned](#review)

- - - - - -

<a name="install"></a>

Install RCov
============

Elaborating slightly on the [nice instructions](http://github.com/aslakhellesoy/cucumber/wikis/using-rcov-with-cucumber-and-rails) on the cucumber wiki, Aslak recommends that you use [spicycode’s RCov](http://github.com/spicycode/rcov/tree/master) instead of the ‘official’ one, “as it currently segfaults too much for most people’s taste.”

```
<pre class="code">
gem sources -a http://gems.github.com
gem uninstall rcov
gem install spicycode-rcov
```

Second, you’ll need to open up the cucumber generated task file and set the rcov config option (add one line in bold).

`<strong>in todolist/lib/tasks/cucumber.rake</strong>`

> `<br></br>$:.unshift(RAILS_ROOT + '/vendor/plugins/cucumber/lib')<br></br>require 'cucumber/rake/task'<br></br>Cucumber::Rake::Task.new(:features) do |t|<br></br>  t.cucumber_opts = "--format pretty" <br></br>  <strong>t.rcov = true</strong><br></br>end<br></br>task :features => 'db:test:prepare'<br></br>`

<a name="coverage"></a>

Look at Code Coverage
=====================

Now when you run:

```
<pre class="code">
rake features
```

And you point your browser at: `http://localhost/todolist/coverage/`

You’ll see:

[![](http://farm4.static.flickr.com/3232/3145974854_eecc2243ec.jpg)](http://farm4.static.flickr.com/3232/3145974854_02eb274fae_o.png)

We can see that we don’t have complete coverage in two files: webrat.rb and tasks\_controller.rb The first doesn’t matter, since it is part of the test framework (in fact there ought to be some way to exclude that), but we need to be concerned that half of our generated controller code is untested. By clicking on the filename, we can see the detailed coverage where the lines of code that are not covered are highlighted in red:

[![](http://farm4.static.flickr.com/3093/3145974882_e734e02fd4.jpg)](http://farm4.static.flickr.com/3093/3145974882_6c91b6a2a2_o.png)

It is unsurprising that we’re covering just 40% of this file, since we’ve written just [a single of scenario so far](https://www.ultrasaurus.com/code/2008/12/rails-2-day-3.html).

<a name="more"></a>

More Scenarios
==============

Let’s look at what isn’t getting covered.

- show
- new
- edit
- update (called from edit)
- destroy
- create (called from new)

<a name="create"></a>

Create
------

To create a task, we can leverage quite a bit of webrat, plus a step we wrote before. Add the following scenario to the feature file:

**`in features/tasklist.feature`**

```
<pre class="code">
Scenario: Add a Task
When I go to the tasks page
When I follow "New task"
When I fill in "description" with "go shopping"
And I press "Create"
Then I should see "Task was successfully created."
And I should see "go shopping"
```

then run

```
<pre class="code">
rake features
```

![](http://farm4.static.flickr.com/3248/3146011820_a801cc35ac_o.png)

You’ll see that all of the new steps that I just wrote for the “add a Task” scenario magically worked. What just happened? You can see from the output of “rake features” that the first step was already defined in tasklist\_steps.rb ([see day 3](https://www.ultrasaurus.com/code/2008/12/rails-2-day-3.html)), but each of the others is defined in webrat\_steps.rb. With a little practice you’ll learn the webrat lingo, and it’ll save you a bunch of time. Pretty cool, huh?

Now if we go back to look at our code coverage (http://localhost/todolist/coverage/), the tasks\_controller.rb coverage is at 64.7%.  
[![](http://farm4.static.flickr.com/3098/3145039593_9c48642385.jpg)](http://farm4.static.flickr.com/3098/3145039593_eafa164a16_o.png)  
Clicking on the file, we can see the lines of code that are now tested. We’ve covered new and half of create. (Not quite sure what would cause that error condition, but we’ll move on for now.)

<a name="edit"></a>

Edit
----

Now we’ll do some behavior-driven development, since the auto-generated task list and edit workflow isn’t exactly what I wanted. This is what I see after adding the “go shopping” task manually:

![](http://farm4.static.flickr.com/3089/3145209431_565cc149db_o.png)

I don’t really need the “show” link (since my task only has its description as data and that’s shown in the list and since I’m removing that, I can just make the description itself as a link. So I want to add two scenarios to support my intended edit behavior:

- Clicking on the description link allows edit
- After Editing I return to the task list

```
<pre class="code">
Scenario: Clicking on description link allows edit
Given that I have created a task "go shopping"
When I go to the tasks page
When I follow "Go Shopping"
Then I should see "Editing Task"
```

![](http://farm4.static.flickr.com/3107/3145248655_c651d3f708_o.png)

As expected, the new scenario fails. Time to write the code! The list of tasks can be found in app/views/tasks/index.html.erb

![](http://farm4.static.flickr.com/3098/3146118822_bbf8cd83db_o.png)

As you can see that I’ve modified line 10 to link the description to the edit task page. Note that (h task.description) needs to be enclosed in parens. We want to keep the h, just to make sure that the description is properly escaped, in case it has special characters like ‘&lt;'. I also removed show and edit links. Now, when I run 'rake features' all of my steps pass. Yay!

But wait! I still have the “show” method in my controller. What’s up with that? If I look at my coverage report, it shows that it is being called. In my controller, both create and update redirect to @task (which is the “show” page), like I did in [day 2](https://www.ultrasaurus.com/code/2008/12/rails-day2.html#edit-controller), I’ll modify those to redirect to index instead.

`in <strong>app/controllers/task_controller.rb</strong>`

change:

`       format.html { redirect_to(@task) }`

to:

`format.html { redirect_to :action => "index"  } `

and remove the show method

Rerun ‘rake features’ just to make sure all is good. And you can now see that the tasks\_controller code coverage is at 62%. We’re calling edit, but not yet update… on to the next scenario.

```
<pre class="code">
Scenario: After Editing I return to the task list
Given that I have created a task "go shopping"
When I go to the tasks page
When I follow "Go Shopping"
And I fill in "description" with "buy bagels"
And I press "Update"
Then I should see "Task was successfully updated."
And I should see "Listing tasks"
And I should see "buy bagels"
```

When I run “rake features” the scenario passes. (Yay!) I don’t know how to hit the error condition in update either, but I’ll leave that for another day.

<a name="delete"></a>

Delete
------

I left delete for last since it is a bit trickier. With the design of the app, there is a “destroy” link for each task in the list, so I have to figure out which one to click.

 I found this handy step definition in an [example by Aslak](http://github.com/aslakhellesoy/cucumber_rails/tree/master/features/step_definitions/lorry_steps.rb):

```
<pre class="code">
When /^I delete the (d+)(?:st|nd|rd|th) lorry$/ do |pos|
visit lorries_url
within("table > tr:nth-child(#{pos.to_i+1})") do
click_link "Destroy"
end
end
```

When I first looked at that I thought `> tr:nth-child` was some wild new Ruby syntax, but the kind folk on the RSpec list [answered my question](http://www.ruby-forum.com/topic/174063#new) by pointing me to the [CSS selector doc](http://www.w3.org/TR/CSS2/selector.html#child-selectors). I had forgotten that &gt; was a CSS selector since I had never actually used that selector before. That hint combined with [a previous thread](http://www.ruby-forum.com/topic/171269) and some digging around to brush up my Ruby and Rail skills led me to a solution. Here is my scenario for delete:

```
<pre class="code">
Scenario: Delete a Task
Given that I have created a task "task 1"
When I go to the tasks page
And I click "delete" for "task 1"
Then I should see "Listing tasks"
And I should not see "task 1"
```

To make this work, I can define a unique DOM id for each of my table row, then I can find the id for “task 1” and then click the link inside that table row.

### 1) Define a unique DOM id for each table row

In `app/views/tasks/index.html.erb`, we have some Ruby code which iterates through the list of tasks (@tasks) and for each ‘task’ there is a table row. To add a unique id for the table row, I insert a snippet of ruby code within &lt;% … %&gt; which evaluates to a unique string. In this case I use the string “task” plus to id of the task itself, generating task4, task5 or whatever.

> `<br></br><% for task in @tasks %><br></br>  <tr id="<%="task"+task.id.to_s%>"><br></br>`

### 2) Find the id for “task 1”

Given the description of a task, I need to find its id. In the [ActiveRecord::Base API docs](http://api.rubyonrails.org/classes/ActiveRecord/Base.html), it describes some handy syntax for finding by attribute value. “Dynamic attribute-based finders are a cleaner way of getting (and/or creating) objects by simple queries without turning to SQL. They work by appending the name of an attribute to find\_by\_, find\_last\_by\_, or find\_all\_by\_.” Since the attribute I have is “description,” I can call

```
<pre class="code">
task = Task.find_by_description(desc)
```

to get the task object where the description attribute matches the given parameter.

### 3) Click the link inside the table row

Putting it all together I can create a step definition like this:

```

When /^I click "delete" for "(.*)"$/ do |desc|
task = Task.find_by_description(desc)
within("table > tr#task"+task.id.to_s) do
click_link "Destroy"
end
end
```

I run “rake features” and all is good. The only thing left to do is to rename the “Destroy” link to be “delete” as I described it and fix up the step to have a more general definition:

```
<pre class="code">
When /^I click "(.*)" for "(.*)"$/ do |link, desc|
task = Task.find_by_description(desc)
within("table > tr#task"+task.id.to_s) do
click_link link
end
end
```

I run “rake features” and see that 26 steps passed. Woo hoo! Code coverage shows 83.8% of the controller file (everything but those pesky error conditions.)

<a name="refactor"></a>

Refactor to Remove Duplication
==============================

Now that the feature description roughly covers the functionality of our app, I sought to take Matt’s advice and look at the code and see if we need to remove some duplication.  
I looked first at the controller and found something odd:

`in <strong>app/controllers/tasks_controllers.rb</strong>:`

```
<pre class="code">
class TasksController  @tasks }
end
end

# GET /tasks/new
# GET /tasks/new.xml
def new
@task = Task.new

respond_to do |format|
format.html # new.html.erb
format.xml  { render :xml => @task }
end
end

# GET /tasks/1/edit
def edit
@task = Task.find(params[:id])
end
```

The index and new methods repeat code, but the edit method, which I would expect to contain the same repeated 4 lines omits the code. In fact, if I remove those lines in index and new, the app works fine.

```
<pre class="code">
class TasksController < ApplicationController
# GET /tasks
# GET /tasks.xml
def index
@tasks = Task.find(:all)
end

# GET /tasks/new
# GET /tasks/new.xml
def new
@task = Task.new
end

# GET /tasks/1/edit
def edit
@task = Task.find(params[:id])
end
```

When I run ‘rake features’ all the steps pass and poking at the application also yields success. What’s going on? There must be something happening by default. At first I couldn’t figure out where ApplicationController was defined, but an answer to my [question on the Rails list](http://www.ruby-forum.com/topic/174419#764163) pointed out that ApplicationController is one of the classes created by generate scaffold (defined in app/controllers/application.rb). Looking at the code (and comments) we can see that it simply sets some defaults for any controller in the application. ApplicationController is a subclass of ActionController::Base, which we can look up in the [Rails API Doc](http://api.rubyonrails.org/). The doc explains that “Actions, by default, render a template in the app/views directory corresponding to the name of the controller and action after executing code in the action.” I suppose the extra code is in there to facilitate modifying it, in case we wanted the action to do something special.

<a name="review"></a>

What did we learn?
==================

Today we learned about:

- installing and using RCov
- cucumber steps that can be quickly defined using webrat
- dynamic-attribute finders: find\_by
- adding a unique DOM id to more easily test the app

We also learned that you need to understand code in order to refactor it, but, of course, we already knew that :)

There ends day 4, but I still haven’t completed all of the features of the Four Days on Rails tutorial. Topics yet to learn:

- Adding attributes and other models: do I scaffold again or just write code?
- Associated Models
- Pagination
- Updating multiple records