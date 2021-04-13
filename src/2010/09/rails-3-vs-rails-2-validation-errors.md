---
title: 'rails 3 vs. rails 2 validation errors'
date: '2010-09-07T02:14:06-07:00'
status: publish
permalink: /2010/09/rails-3-vs-rails-2-validation-errors
author: sarah
excerpt: ''
type: post
id: 2795
category:
    - code
tag: []
post_format: []
---
Not sure if this is a bug or a feature. I’d guess it is here for a reason, and maybe I’m late for noticing, but Rails 3 errors now provides an array for each attribute, whereas in Rails 2.3 it was just a string. Here’s the output from two almost identical applications…

Loading development environment (Rails 2.3.8)  
&gt;&gt; person = Person.new  
=&gt; #&lt;Person id: nil, first\_name: nil, last\_name: nil, present: nil…  
&gt;&gt; person.valid?  
=&gt; false  
&gt;&gt; person.errors  
=&gt; #&lt;ActiveRecord::Errors:0x1034d8f10 @errors=#&lt;OrderedHash …  
&gt;&gt; person.errors\[:first\_name\]  
=&gt; “can’t be blank”

Loading development environment (Rails 3.0.0)  
&gt;&gt; person = Person.new  
=&gt; #&lt;Person id: nil, first\_name: nil, last\_name: nil, present: nil…  
&gt;&gt; person.valid?  
=&gt; false  
&gt;&gt; person.errors  
=&gt; {:first\_name=&gt;\[“can’t be blank”\]}  
&gt;&gt; person.errors.class  
=&gt; ActiveModel::Errors  
&gt;&gt; person.errors\[:first\_name\]  
=&gt; \[“can’t be blank”\]

I didn’t see that in the release notes, but it failed my tests for ActiveRecord class. Someone else must have a list of these details, yes?