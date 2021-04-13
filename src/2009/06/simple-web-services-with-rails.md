---
title: 'simple web services with rails'
date: '2009-06-21T10:05:23-07:00'
status: publish
permalink: /2009/06/simple-web-services-with-rails
author: sarah
excerpt: ''
type: post
id: 1533
category:
    - code
tag: []
post_format: []
---
Rails enables web services by default, which is pretty awesome, and I’ve been relying on that for a while. It is pretty nifty how Rails will magically parse XML post parameters, create an in-memory object and then save that object to the database without your having to write one line of code. However, when the magic fails it can be pretty hard to debug. I found it useful to run basic tests on the command line using curl (hearing the voice of [Zach Moazeni](http://simplechatter.com/) in my head saying: “test your assumptions.”)

Below is a writeup of the set of curl commands and sample output for testing the default Rails XML REST APIs. This can serve as a cheat sheet for the experienced or an introduction for folks new to rails who want a basic understanding of the default webservice APIs.

Create an app, by typing the following commands into your terminal:

`<br></br>$ rails basic_app<br></br>$ cd basic_app<br></br>$ ./script/generate scaffold  project title:string description:text<br></br>$ rake db:migrate<br></br>$ ./script/server<br></br>`

In Rails 2.3, you also need to added the following line to the top of app/controllers/projects\_controller.rb (This will allow external access to the APIs.) You can make this change while the server is running, btw.

`<br></br>  skip_before_filter :verify_authenticity_token<br></br>`

Leave that window open where you can see it, since it will output useful stuff from the log. Then in another terminal window, experiment with the following commands to interact with your application APIs.

blockquote.code {  
 font-style: normal;  
 font-family: Monaco,monospace;  
 font-size: 12px;  
 border: solid 1px #aaa;  
 padding: 6px;  
 background-color: #eee;  
 color: inherit;  
 overflow:auto;  
 margin: 10px 0px;  
}

Create
------

POST /projects.xml

Create a project object based on the XML representation given in the post body and save in the projects database table.

> $ curl -X POST -d "&lt;project&gt;&lt;title&gt;Awesome&lt;/title&gt;&lt;description&gt;This is an awesome project.&lt;/description&gt;&lt;/project&gt;" -H "Content-Type: application/xml" http://localhost:3000/projects.xml
> 
> &lt;?xml version="1.0" encoding="UTF-8"?&gt;  
> &lt;project&gt;  
>  &lt;created-at type="datetime"&gt;2009-06-21T10:13:43-07:00&lt;/created-at&gt;  
>  &lt;description&gt;This is an awesome project.&lt;/description&gt;  
>  &lt;id type="integer"&gt;6&lt;/id&gt;  
>  &lt;title&gt;Awesome&lt;/title&gt;  
>  &lt;updated-at type="datetime"&gt;2009-06-21T10:13:43-07:00&lt;/updated-at&gt;  
> &lt;/project&gt;

Index
-----

GET /projects.xml

This returns a list of all of the projects in the database with an automatically generated XML representation.

> $ curl http://localhost:3000/projects.xml&lt;?xml version="1.0" encoding="UTF-8"?&gt;
> 
> &lt;projects type="array"&gt;  
>  &lt;project&gt;  
>  &lt;created-at type="datetime"&gt;2009-06-21T10:13:19-07:00&lt;/created-at&gt;  
>  &lt;description&gt;This is an awesome project.&lt;/description&gt;  
>  &lt;id type="integer"&gt;1&lt;/id&gt;  
>  &lt;title&gt;Awesome&lt;/title&gt;  
>  &lt;updated-at type="datetime"&gt;2009-06-21T10:13:19-07:00&lt;/updated-at&gt;  
>  &lt;/project&gt;  
>  &lt;project&gt;  
>  &lt;created-at type="datetime"&gt;2009-06-21T10:13:43-07:00&lt;/created-at&gt;  
>  &lt;description&gt;New information here&lt;/description&gt;  
>  &lt;id type="integer"&gt;2&lt;/id&gt;  
>  &lt;title&gt;Awesome&lt;/title&gt;  
>  &lt;updated-at type="datetime"&gt;2009-06-21T10:49:21-07:00&lt;/updated-at&gt;  
>  &lt;/project&gt;  
> &lt;/projects&gt;

Show
----

GET /projects/1.xml

This returns an xml representation of the project with id #1

> $ curl http://localhost:3000/projects/1.xml&lt;?xml version="1.0" encoding="UTF-8"?&gt;
> 
> &lt;project&gt;  
>  &lt;created-at type="datetime"&gt;2009-06-21T10:45:19-07:00&lt;/created-at&gt;  
>  &lt;description&gt;This is an awesome project.&lt;/description&gt;  
>  &lt;id type="integer"&gt;8&lt;/id&gt;  
>  &lt;title&gt;Awesome&lt;/title&gt;  
>  &lt;updated-at type="datetime"&gt;2009-06-21T10:45:19-07:00&lt;/updated-at&gt;  
> &lt;/project&gt;

Update
------

PUT /projects/1.xml

This modifies the project with id #1

> curl -X PUT -d "&lt;project&gt;&lt;description&gt;New information here&lt;/description&gt;&lt;/project&gt;" -H "Content-Type: application/xml" http://localhost:3000/projects/1.xml