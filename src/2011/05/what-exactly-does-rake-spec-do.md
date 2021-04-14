---
title: 'what exactly does rake spec do?'
date: '2011-05-08T13:41:35-07:00'
status: publish
exported_permalink: /2011/05/what-exactly-does-rake-spec-do
author: sarah
excerpt: ''
type: post
id: 3164
category:
    - code
tag: []
post_format: []
---
$ rake spec  
(in /Users/sarah/src/../my\_app)  
You have 1 pending migrations:  
 20110416135407 CreateCourses

The rake spec command reminds us that we need to run our migration before running  
our tests. In fact, it does a whole lot more than that. There are a whole bunch of best practices rolled in that one  
command. To see exactly what is going on, we can run rake spec with the –trace  
option:

`<br></br>$ rake spec --trace<br></br>(in /Users/sarah/src/tfr/svn/Book/code/class_app_new_source)<br></br>** Invoke spec (first_time)<br></br>** Invoke db:test:prepare (first_time)<br></br>** Invoke db:abort_if_pending_migrations (first_time)<br></br>** Invoke environment (first_time)<br></br>** Execute environment<br></br>** Execute db:abort_if_pending_migrations<br></br>** Execute db:test:prepare<br></br>** Invoke db:test:load (first_time)<br></br>** Invoke db:test:purge (first_time)<br></br>** Invoke environment<br></br>** Execute db:test:purge<br></br>** Execute db:test:load<br></br>** Invoke db:schema:load (first_time)<br></br>** Invoke environment<br></br>** Execute db:schema:load<br></br>** Execute spec<br></br>`

When it says invoke it is calling a particular rake task, but then it will call its dependencies. To really see what is happening in what order, check out the execute commands. The commands db:test:prepare and db:test:load don’t do much themselves, aside from setting up the environment and executing another task or two. We can see from the output that rake is actually executing the following steps:

1. Don’t run the specs if there are pending migrations in the development database. (db:abort\_if\_pending\_migrations)
2. Drop the test database (db:test:purge)
3. Load the schema into the test database (db:schema:load in environment “test”)

These steps make sure that we are always testing in a clean environment, so we know exactly what we’re testing when we run our specs.

The code that makes this happen in Rails 3, can now be found in [railties](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/railties/databases.rake#L455). (Thanks to [@pixeltrix](http://twitter.com/pixeltrix) for pointing me to it.)/62206174505873408