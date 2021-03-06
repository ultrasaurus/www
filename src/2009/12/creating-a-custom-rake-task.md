---
title: 'creating a custom rake task'
date: '2009-12-20T09:30:51-08:00'
status: publish
exported_permalink: /2009/12/creating-a-custom-rake-task
author: sarah
excerpt: ''
type: post
id: 2236
category:
    - code
tag: []
post_format: []
---
There’s a nice [Railscast introduction to rake](http://railscasts.com/episodes/66-custom-rake-tasks) for Rails, which goes into a number of other important details that aren’t covered in this post. Below is a little tutorial of creating a Rails rake task and getting it to run remotely on heroku.

Introduction to Rake
--------------------

In lib/tasks, create a file called greet.rake

```

task :greet do
   puts "Hello world"
end
```

By naming the task .rake and putting it in this special place rails will automatically pick it up and make it available to you. You can see it listed if you type: rake -T on the command line. To run it:

```

rake greet
```

which will print “Hello world”

to run one task before another, specify a dependency like this (multiple tasks may be specified in the same file):

```

task :ask => :greet do
   puts "How are you?"
end
```

Writing a Practical Rake Task
-----------------------------

Now for the task at hand, I’m going to create a rake task which creates a bunch of fake data for me to test with. First I’ll create a little experimental app:

```

rails rake_example
cd rake example
script/generate scaffold person first_name:string last_name:string
rake db:migrate
rails generate admin fake_people
```

Here’s the rake task (lib/tasks/fake\_people.rake):

```

require 'faker'

namespace :admin  do
  desc "create some fake data"
  task :fake_people => :environment do
    print "How many fake people do you want?"
    num_people = $stdin.gets.to_i
    num_people.times do
      Person.create(:first_name => Faker::Name.first_name,
                    :last_name => Faker::Name.last_name)
    end
    print "#{num_people} created.n"
  end
end
```

Note that I’m using the faker gem ([docs here](http://faker.rubyforge.org/rdoc/)) and I created a task dependency on loading the rails environment so I could access my Person model.

Now I can run

```

rake admin:fake_people
```

and it will prompt me to ask how many I want and then it will create them. Cool goodness, yes?

Running Remotely on Heroku
--------------------------

We’re not done yet. I want to deploy this on heroku and be able to run the task remotely. For this, there are two gotchas, first I can’t run an interactive script remotely; also I need to tell heroku that I am using the fake gem and make sure it is installed.

### 1) removing interactivity

Instead of an interactive script, we can set an environment variable or command line argument (thanks to a [tip by Adam Wiggins](http://groups.google.com/group/heroku/browse_thread/thread/775f445e5b11e498/)).

My modified task looks like this:

```

require 'faker'

namespace :admin  do
  desc "create some fake data"
  task :fake_people => :environment do
    num_people = ENV['NUM_RECORDS'].to_i
    num_people.times do
      Person.create(:first_name => Faker::Name.first_name,
                    :last_name => Faker::Name.last_name)
    end
    print "#{num_people} created.n"
  end
end
```

which I can call locally from the command line like this:

```

rake admin:fake_people NUM_RECORDS=1
```

### 2) adding gem to heroku

I need to create a [gems manifest](http://blog.heroku.com/archives/2009/3/10/gem_manifests/), which sounds fancy, but is simply creating a .gems file at the root of my app with contents similar to what I would put in my config environment.rb to specify that my app requires a gem:

```

faker --version ">=0.3.1"
```

### 3) Deploy and Run

So I can deploy my app to heroku with the usual steps

```

git init
git add .
git commit -m "example app for rake script testing"
heroku create
git push heroku master
heroku rake db:migrate
```

and run the task remotely:

```

heroku run rake admin:fake_people NUM_RECORDS=1
```