---
title: 'upgrading pie from rails 3.0 to 3.1'
date: '2011-09-13T08:23:59-07:00'
status: publish
permalink: /2011/09/upgrading-pie-from-rails-3-0-to-3-1
author: sarah
excerpt: ''
type: post
id: 3406
category:
    - general
tag: []
post_format: []
---
Whenever I upgrade Rails, I always start with “rails new” so that I get all the new config file goodness — I want to start fresh with whatever the new defaults are and then only make the modifications that I really want in my app. Here’s the process I went through upgrading the pie “bakery” (a relative simple Rails 3.0 app) to Rails 3.1.

First I moved my old app to a new name (since I want my new Rails app to have the same name internally as the old Rails app):

```

mv bakery bakery30
```

Now I set up a new gemset, so I’m starting fresh. (My first attempt was to use my old gemset, but that showed me an old warning that I’d like to not bring forward, or at least isolate in the process of upgrading):

```

rvm use 1.9.2-p290
rvm gemset create rails31
rvm use 1.9.2-p290@rails31
```

Create the new app (specifying -T to create the app without test-unit, since I’m an [RSpec](https://www.relishapp.com/rspec) fan)

```

rails new bakery -T
mv bakery bakery 31
```

Now I edit my Gemfile to include the gems I want to bring over from my old app…

```

cd bakery
vi Gemfile   
bundle install
```

Then I want to re-generate rspec and cucumber config files and boilerplate

```

rails g rspec:install
rails g cucumber:install
```

ok, now I have vanilla Rails 3.1 app  
I fetch my old app from github:

```

git clone git@github.com:blazingcloud/pie-bakery.git bakery
cd bakery
```

and using the power of git, I’m going to remove all the old 3.0 code, add in my 3.1 app

```

git rm -r *
cp -r ../bakery31/* .
git add .
```

Then I use gitx (a modern version like [brotherbard](https://github.com/brotherbard/gitx/downloads)) to look at the changes and revert any deletes that are actually app code that I want to keep, review every diff, and hope that I’m paying close enough attention to everything (really wish I could be pairing on this).

Now I set up my database and run my tests… I don’t know why “rake test” doesn’t automatically run cucumber and rspec tests like it used to. hmmm

```

rake db:schema:load
rake cucumber
rake spec
```

I realize that I missed a couple of diffs, rinse, repeat… when all is green I’m done. Whew.

I copy in my old .git/config so I pull in my remote heroku repo config (which I’ve updated to [cedar stack](http://devcenter.heroku.com/articles/cedar))

```

cp ../bakery30/.git/config .git/config
```

and run rails