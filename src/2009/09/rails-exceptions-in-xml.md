---
title: 'rails exceptions in xml'
date: '2009-09-13T10:13:57-07:00'
status: publish
exported_permalink: /2009/09/rails-exceptions-in-xml
author: sarah
excerpt: ''
type: post
id: 2058
category:
    - code
tag: []
post_format: []
---
We ran into an issue last week where our XML APIs were returning HTML under certain error conditions, rather than the expected XML. Our solution was to add the following code to the ApplicationController:

```

  rescue_from Exception do |exception|
    respond_to do |format|
      format.xml  { render :xml => 
           "<error>Internal Server Error #{exception.message}</error>", 
           :status => 500 }
      format.html { render :html => {:file => 'public/500.html'}, :status => 500 }
      format.json { render :json => 
            {:error => "Internal Server Error #{exception.message}"}.to_json, 
             :status => 500 }
    end
  end
```

We might have also declared a rescue\_action, and I’m not sure of the benefits of one over the other, except that perhaps we needed to implement a general form of rescue\_from since we had another more specific form already declared.

It seemed to me that this should be the default behavior in rails, so I decided to dig into it a little more and see what I could discover. I started by making a little test app to reproduce the exception. The particular case from last week was a database limit that wasn’t being caught in the app with a length validation. When I tried to re-create the error in MySql, I noticed that no exception is thrown since MySql will just truncate the data (although perhaps that is only because I am not running MySql in strict mode). In PostgreSQL, the database layer will throw an exception.

Test app setup:

```

rails -d postgresql test_postgresql
cd test_postgresql/
script/generate scaffold person first:string last:string present:boolean
```

Edit the migration to create a database limit:

```

class CreatePeople < ActiveRecord::Migration
  def self.up
    create_table :people do |t|
      t.string :first, :limit => 40
      t.string :last, :limit => 40
      t.boolean :present

      t.timestamps
    end
  end

  def self.down
    drop_table :people
  end
end
```

Create the postgres user. Note double-quotes around user, single quotes around password. It has to be that way. Go figure.

```

$ sudo su postgres -c psql
postgres=# create user "test_postgresql" with superuser password 'password';
CREATE ROLE
postgres=# q
```

Finally create the database, run migration, and start the server:

```
 
rake db:create:all
rake db:migrate
./script/server
```

If you point your browser at http://localhost:3000/people and try to create a person with more that 40 characters in the first name, you will see the following error:

```

ActiveRecord::StatementInvalid in PeopleController#create
PGError: ERROR:  value too long for type character varying(40)
```

That is all well and good; however, if you do the same in XML, you will get the same error in **HTML**.

```
<pre width="80">
$ curl -X POST -d "<person><first>This is a first name that is too long for the database limit</first></person>" -H "Content-Type: application/xml" http://localhost:3000/people.xml
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Action Controller: Exception caught</title>
  <style>
    body { background-color: #fff; color: #333; }

    body, p, ol, ul, td {
      font-family: verdana, arial, helvetica, sans-serif;
      font-size:   13px;
      line-height: 18px;
    }
```

That seems like a bug to me. Perhaps this should be a lighthouse ticket rather than a blog post.. still not confident in identifying bugs in Rails, so I figured I’d post here first.