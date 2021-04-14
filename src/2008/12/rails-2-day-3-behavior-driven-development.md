---
title: 'rails 2 day 3: behavior-driven development'
date: '2008-12-22T00:42:19-08:00'
status: publish
exported_permalink: /2008/12/rails-2-day-3-behavior-driven-development
author: sarah
excerpt: ''
type: post
id: 599
category:
    - code
tag: []
post_format: []
---
Now that we have learned some basic Ruby syntax and gained some understanding about what the Rails generate scaffold script does, it is high time we started using a more modern approach to coding. In fact, if you recall at the end of [day 2](https://www.ultrasaurus.com/code/2008/12/rails-day2.html), I realized with horror that we had actually modified code and added features without developing the tests first. This defied everything I had ever heard about good coding practices from the Ruby crowd and I set off to mend my ways.

[Rick Denatale](http://www.ruby-forum.com/topic/94721#264483) describes the process of test-driven/behavior-driven development as:

1. Write the test/spec
2. Ensure that it FAILS
3. Write the code to make it pass
4. Goto step 1

After [reading a bit](https://www.ultrasaurus.com/sarahblog/archives/000543.html) about test- and behavior-driven development, I decided to use a relatively new framework called [cucumber](http://github.com/aslakhellesoy/cucumber/wikis) which uses natural language to describe features.

Today we will:

1. [Install cucumber](#install)
2. [Set up the application](#setup)
3. [Describe a feature](#spec)
4. [Execute the feature and Watch it fail](#fail)
5. [Write the code to make it pass](#code)
6. [Review what we learned](#review)

- - - - - -

h1 {font-size: 150%}  
h1,h2 {font-style: bold}  
img  
{  
border:2px solid silver;  
margin:0px 0px 15px 20px;  
}  
blockquote, pre.code {  
border: solid 1px #aaa;  
padding: 6px;  
background-color: #eee;  
color: inherit;  
overflow:auto;  
margin: 10px 0px;  
}

<a name="install"></a>

Install Cucumber
================

Based on these [install instructions](http://github.com/aslakhellesoy/cucumber/wikis/ruby-on-rails)

```
<pre class="code">sudo gem install rspec rspec-rails cucumber webrat
```

**important**: Cucumber 0.1.12 and up depends on Webrat 0.3.2.1 or higher, which as of this writing is not yet officially released to Rubyforge’s gem repository. In the meanwhile, install Bryan Helkamp’s snapshot gem:

```
<pre class="code">
gem sources -a http://gems.github.com
sudo gem install brynary-webrat
```

The plugins’ dependencies must be installed separately:

```
<pre class="code">
gem install term-ansicolor treetop diff-lcs nokogiri
```

<a name="setup"></a>

Setup the Application
=====================

First we’ll create the Rails “to do list” application:

```
<pre class="code">
cd $webroot
rails -d mysql todolist
cd todolist
rake db:create:all
rake db:migrate
```

Now we’ll set up cucumber for the project

```
<pre class="code">
ruby script/generate cucumber
create  features/step_definitions
create  features/step_definitions/webrat_steps.rb
create  features/support
create  features/support/env.rb
exists  lib/tasks
create  lib/tasks/cucumber.rake
create  script/cucumber
```

Just to make sure that everything is installed correctly:

```
<pre class="code">rake features
```

If that runs without errors you are ready to rock.

<a name="spec"></a>

Describe a Feature
==================

In the features directory that was auto-created for us with the cucumber script, we create a .feature file which starts with a description of the feature. The first section that describes the feature appears to be purely documentation; however the “scenario” sections will each become part of the executable feature definition. For starters we’ll do something simple.

`<strong>features/tasklist.feature</strong>`

```
<pre class="code">
Feature: Tasks
In order to keep track of tasks
People should be able to
Create a list of tasks

Scenario: List Tasks
Given that I have created a task "task 1"
When I go to the tasks page
Then I should see "task 1"
```

We know we haven’t written any executable steps, but we’ll execute it anyhow:

![](http://farm4.static.flickr.com/3243/3126961149_b267e27c02_o.png)

Note that one of the steps is already defined in webrat. Isn’t that cool? When we set up cucumber for the project, it automatically includes step\_definitions/webrat\_steps.rb which defines some common steps. As you get the hang of this, you reuse certain word patterns which map to specific tests. But we’re getting ahead of ourselves. We need to dive into the creation of “steps” which make up our executable spec. Cucumber gives a some handy snippets to get us started (in the output of “rake features” above). We’ll paste these into a new file that we’ll create in the “features/step\_definitions” directory:

`<strong>features/step_definitions/tasklist_steps.rb</strong>`

```
<pre class="code">
Given /^that I have created a task "(.*)"$/ do |desc|
Task.create!(:description => desc)
end

When /^I go to the tasks page$/ do
visit "/tasks"
end
```

Note that I touched up the first step to include a regular expression. This means I could add `Given that I have created a task "foo"` to another scenario and it would match this step.

> <a name="syntax"></a>
> 
> ## Short aside on task creation syntax
> 
> To create the task, I’m calling my Task model directly (since I’m new to Rails, I looked up the ActiveRecord::Base syntax in the[ Rails Framework API docs](http://api.rubyonrails.org/)). In my first pass I wrote:
> 
> ```
> 
> task = Task.new(:description => desc);
> task.save
> ```
> 
> However, Aslak Hellesøy [kindly pointed out](http://www.ruby-forum.com/topic/174015#762400) that it would fail silently with that syntax, and instead I should call `task.save!` or the even simpler `Task.create!(:description => desc)`. I had missed create! in the documentation, since it is part of [ActiveRecord::Validations](http://api.rubyonrails.org/classes/ActiveRecord/Validations/ClassMethods.html#M001902). The API doc is a little confusing on this point, but looking at the source shows that [ActiveRecord::Validations is included as a module](http://www.ruby-forum.com/topic/174015#762531). [Pat Maddox notes](http://www.ruby-forum.com/topic/174015#762550) that he uses the bang version (.save!) in tests, and the non-bang version (.save) in production code since validation errors aren’t exceptional.

<a name="step3"></a>

Back to Step 3
--------------

Looking in `features/step_definitions/webrat_steps.rb`, you can see the definition of our third step:

```
<pre class="code">
Then /^I should see "(.*)"$/ do |text|
response.body.should =~ /#{text}/m
end
```

Ok, now we have a simple spec. Is it time to write the code? No!

<a name="fail"></a>

Execute the Feature and Watch it Fail
=====================================

  
![](http://farm4.static.flickr.com/3131/3127004017_c31be47724_o.png)

As expected, we see errors on our first step, since we have not yet written any code for the application.

<a name="code"></a>

Write the code to make it pass
==============================

Now, at last it is time to write code

```
<pre class="code">
$ ./script/generate scaffold Task description:string
$ rake db:migrate
```

Run the spec again..

![](http://farm4.static.flickr.com/3131/3127010689_8d6948843c_o.png)

It passes, yay!

<a name="review"></a>

What did we learn?
==================

When we first set up our app, to setup cucumber:

```
<pre class="code">
ruby script/generate cucumber
```

To describe our feature, we create two files:

- features/xxx.feature
- features/step\_definitions/xxx\_steps.rb

To run the feature description:

```
<pre class="code">
rake features
```