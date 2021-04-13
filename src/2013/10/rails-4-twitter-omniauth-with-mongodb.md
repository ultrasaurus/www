---
title: 'rails 4 twitter omniauth with mongodb'
date: '2013-10-19T19:41:18-07:00'
status: publish
permalink: /2013/10/rails-4-twitter-omniauth-with-mongodb
author: sarah
excerpt: ''
type: post
id: 4686
category:
    - code
tag: []
post_format: []
---
If you are brand new to MongoDB and Rails 4, take a quick look at my very basic [rails 4 mongodb tutorial](https://www.ultrasaurus.com/sarahblog/code/) before diving into this one.

Gems: [mongoid](http://mongoid.org), [omniauth](http://www.omniauth.org/), [figaro](https://github.com/laserlemon/figaro)

Let’s get started
-----------------

Make sure you have Rails 4 (rails -v). We’ll make a Rails app skipping test-unit (-T), since I prefer RSpec, and omitting ActiveRecord (-O) since we’ll be using MongoDB.

```

rails new parakeet -T -O
cd parakeet
```

Add the following to the Gemfile

```

gem "mongoid", git: 'git://github.com/mongoid/mongoid.git'
gem "omniauth-twitter"
gem "figaro"    # key configuration using ENV 
```

Now some auto-code generation for quick setup:

```

rails g mongoid:config
#      create  config/mongoid.yml

rails generate figaro:install
#      create  config/application.yml
#      append  .gitignore
```

I’ve decided to use figaro which allows me to easily configure my API keys without committing them to my source repo, which is very helpful when posting open source code. We need to set up the app for an API key in order to auth with Twitter.

Get Developer Key from Twitter
------------------------------

Sign in using your regular Twitter account at: <https://dev.twitter.com/>

Then in the upper-right, select “my applications”  
![](https://www.monosnap.com/image/GagljLkbhcGSDhZNnegf0246b.png)

Click “Create a new application” and fill in the form. I called my app blue-parakeet for uniqueness — you’ll have to make up your own name.  
![](https://www.monosnap.com/image/CUWsk5qmrLGsoOBZxmqvldb8x.png)  
Make sure you put in a callback URL, even though you won’t use it for development (since omniauth tells twitter the callback URL to override this setting) — if you don’t supply one you will get a 401 unauthorized error.

Read and Accept the Terms, then click “Create Your Twitter Application”

Now you have a “key” and “secret” (called “consumer key” and “consumer secret”) which you will need to configure your rails app.

Using Figaro gem for Configuring API keys
-----------------------------------------

Edit **config/application.yml**

```

# config via Figaro gem, see: https://github.com/laserlemon/figaro
# rake figaro:heroku to push these to Heroku
TWITTER_KEY: ABCLConsumerKeyCopiedFromTwitterDevPortal
TWITTER_SECRET: XYZConsumerSecretCopiedFromTwitterDevPortal
```

Configuring Omniauth
--------------------

Edit **config/initializers/omniauth.rb**

```

Rails.application.config.middleware.use OmniAuth::Builder do
  provider :twitter, ENV['TWITTER_KEY'], ENV['TWITTER_SECRET']
end
```

Now Omniauth is already setup to auth with twitter. Let’s run the server. Install mongo with `brew install mongodb` if you haven’t already. Also, if you don’t have mongo set up to run automatically at startup, then run Mongo:

```

mongod
```

Then run Rails server:

```

rails s
```

Go to <http://localhost:3000/auth/twitter> and you’ll be presented with twitter auth  
![](https://www.monosnap.com/image/OBdV4vFem0tOo4Nzn3lFpEjeB.png)

However, when we authenticate, we get an error, since we have’t configured our routes yet:  
![](https://www.monosnap.com/image/g0cDeKYAWVglRMuFtkcP5PKMU.png)

Create a Sessions Controller, Add Routes
----------------------------------------

Next step is a sessions controller and a route for the OAuth callback. We’ll make a placeholder create action that just reports the auth info we get back from Twitter.

On the command line:

```

rails generate controller sessions
```

Edit the newly created file, **app/controllers/sessions\_controller.rb**

```

require 'json'
class SessionsController  request.env["omniauth.auth"]
  end
end
```

add the following to **config/routes.rb**

```

get '/auth/:provider/callback' => 'sessions#create'
get '/auth/failure' => 'sessions#failure'
get '/signout' => 'sessions#destroy', :as => :signout
root :to => redirect("/auth/twitter")  # for convenience
```

Now go to <http://localhost:3000/auth/twitter> — after authenticating with Twitter, you will see the user info that Twitter sends to the app from the authentication request (see [docs for explanation of each field](https://dev.twitter.com/docs/platform-objects/users)). The general stuff which is more consistent across providers is in the ‘info’ section, and most of the interesting twitter-specific info is in the “extra” section:  
![](https://www.monosnap.com/image/4YQsosoWhSxJgZh8bLG5N0xgc.png)

User Registration
-----------------

For this app, we’ll use a simple user model, just to show that there’s no magic here — we’re only using Twitter auth not storing our own passwords, so we don’t really need the full features of the lovely Devise gem.

```

rails generate scaffold user provider:string uid:string name:string
```

Add to **app/models/user.rb**

```

  def self.create_with_omniauth(auth)
    create! do |user|
      user.provider = auth['provider']
      user.uid = auth['uid']
      if auth['info']
        user.name = auth['info']['name'] || ""
      end
    end
  end
```

With Rails 4 the recommended pattern to lock down model attributes that we don’t want changed from form submits (or malicious attacks) is in the controller. In **app/controllers/users\_controller.rb** change:

```

    def user_params
      params.require(:user).permit(:provider, :uid, :name)
    end
```

to:

```

    def user_params
      params.require(:user).permit(:name)
    end
```

and then remove the corresponding fields from **app/views/users/\_form.html.erb**

Finally, the real create action for the sessions controller, plus a destroy action for the /signout url we defined earlier:

```

  def create
    auth = request.env["omniauth.auth"]
    user = User.where(:provider => auth['provider'],
                      :uid => auth['uid']).first || User.create_with_omniauth(auth)
    session[:user_id] = user.id
    redirect_to user_path(user), :notice => "Signed in!"
  end

  def destroy
    reset_session
    redirect_to root_url
  end
```

With this app, we’ve got a basic understanding to Twitter OAuth using Rails 4 and the OmniAuth gem. We didn’t actually do anything specific to MongoDB and no testing yet. It is important to understand the technology we’re working with before testing or even writing production code.

Special thanks to [Daniel Kehoe](http://twitter.com/railsapps) of RailsApps. His [Rails 3 OmniAuth Mongoid](http://railsapps.github.io/tutorial-rails-mongoid-omniauth.html) tutorial provided a helpful foundation.