---
title: 'rails 4 with mongodb on osx'
date: '2013-10-13T11:25:19-07:00'
status: publish
permalink: /2013/10/rails-4-with-mongodb-on-osx
author: sarah
excerpt: ''
type: post
id: 4640
category:
    - code
tag: []
post_format: []
---
This post covers getting started with Rails 4 and Mongodb, using the Mongoid gem. As part of getting up to speed, I enjoyed reading [Rails + Mongo take on the object-relational mismatch](http://blog.mongodb.org/post/53271876885/ruby-rails-mongodb-and-the-object-relational-mismatch) by Emily Stolfo from MongoDB.

For starters, here’s a how to create a super simple toy app. I assume Ruby is installed via rvm, but you are new to Mongo.

Install Mongodb on Mac OSX
--------------------------

```
brew update
brew install mongodb
```

> To have launchd start mongodb at login:  
> ln -sfv /usr/local/opt/mongodb/\*.plist ~/Library/LaunchAgents  
> Then to load mongodb now:  
> launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist  
> Or, if you don’t want/need launchctl, you can just run:  
> mongod

Rails 4 with Mongoid
--------------------

I chose Mongoid over MongoMapper (see [quora](http://www.quora.com/What-are-the-advantages-of-using-MongoMapper-versus-using-Mongoid), [stackoverflow](http://stackoverflow.com/questions/1958365/mongoid-or-mongomapper))  
I used MRI 1.9.3 (at this writing, Mongoid supports HEAD but not 2.0)  
rvmrc:  
`<br></br>rvm use ruby-1.9.3-p429@rails4 --create<br></br>`

added to Gemfile:  
`<br></br>gem "mongoid", git: 'git://github.com/mongoid/mongoid.git'<br></br>`

on the command-line:  
`<br></br>rails new mongo-people --skip-active-record<br></br>rails generate mongoid:config<br></br>rails generate scaffold person name street city state<br></br>rails s<br></br>`

Woo hoo! We’ve got an app — looks like a vanilla Rails app from the outside, but it is different on the inside:

```

class Person
  include Mongoid::Document
  field :name, type: String
  field :street, type: String
  field :city, type: String
  field :state, type: String
end
```

No database migrations needed. If we want a new field, we could just declare one in the model and add it to our views. I assume migrations could be used for data migration, but that would be a subject of another post.

References
----------

[Rails 4 with MongoDB Tutorial](http://moredevideas.wordpress.com/2013/04/26/rails-4-with-mongodb/)