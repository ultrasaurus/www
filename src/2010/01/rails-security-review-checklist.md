---
title: 'rails security review checklist'
date: '2010-01-27T00:00:12-08:00'
status: publish
permalink: /2010/01/rails-security-review-checklist
author: sarah
excerpt: ''
type: post
id: 2378
category:
    - code
tag: []
post_format: []
---
I’m reviewing the security of a web app built with Ruby on Rails, so I put together a checklist for a security audit. This isn’t a bank or high security situation, but there were a number of engineers and quite a bit of open source code, so I thought a few checks were in order.

Here’s the list I came up with that I thought other folks might appreciate as a starting point (special thanks to the sfruby list, [Mike Gunderloy](http://afreshcup.com/), and Scott Bronson for feedback):

0\) Make sure your Rails and gems are up to date for latest security patches (see [rails security mailing list](http://groups.google.com/group/rubyonrails-security) for recent advisory notes)

1\) Active Record audit:  
 A) SQL injection:  
 (i) whole word search for “find”, “first”, and “all” then visually inspect all instances of ActiveRecord find calls for potential SQL injection vulnerability (also search for “sql” not whole work search to find find\_by\_sql and “execute” to find cases where raw sql is executed.  
 (ii) search your models for “named\_scope” and check :conditions  
 B) check for [mass assignment](http://railspikes.com/2008/9/22/is-your-rails-application-safe-from-mass-assignment) Either disable mass assignment as Eric suggests in his article, or audit its use. If doing an audit, check every model to make sure it declares which attributes are settable with attr\_accessible. (While attr\_protected may technically work, a white list approach is recommended by security experts and the [rails security advisory](http://groups.google.com/group/rubyonrails-security/browse_thread/thread/42c4d5d3b7354735) on this topic)

2\) Scripting attack: search all eRB files for &lt;%= and ensure that if dynamically generated text was originally entered by the user, it is HTML escaped. Consider [rails\_xss](http://github.com/nzkoz/rails_xss)

3\) Secure Access: If some of the site does not have public access, check controllers and ensure that public actions are specifically allowed and that protected access is the default

4\) search for “eval” (whole word) and verify that usages are safe

5\) search for “forgery” (not whole word), make sure that  
config.action\_controller.allow\_forgery\_protection = false  
is only disabled in test config  
 protect\_from\_forgery should be in the ApplicationController, unless there is a good reason for it not to be

6\) check user auth and review that controller actions are limited to expected use

7\) passwords: not saved as clear-text in the db, not logged

8\) check that private data is not stored in cookies