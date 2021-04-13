---
title: 'openlaszlo simple post code'
date: '2009-06-21T21:43:00-07:00'
status: publish
permalink: /2009/06/openlaszlo-simple-post-code
author: sarah
excerpt: ''
type: post
id: 1584
category:
    - code
tag: []
post_format: []
---
Here’s a little form for sending an XML post in OpenLaszlo. This is a useful little snippet of code, since as if you get one little content header or something wrong, Rails will be unforgiving with its powerful, yet strict implementation of REST.

What the app looks like (enter text in the top, click the button, response is printed in the lower box):

![](http://img.skitch.com/20090622-gts2h4rbw2pq7uwnpdq5e6ea2p.jpg)

blockquote.code {  
 font-style: normal;  
 font-family: Monaco,monospace;  
 font-size: 10px;  
 border: solid 1px #aaa;  
 padding: 6px;  
 background-color: #eee;  
 color: inherit;  
 overflow:auto;  
 margin: 10px 0px;  
}

The code:

> &lt;canvas title="Test Post" proxied="false"&gt;  
>  &lt;dataset src="http:/projects.xml" name="ds"  
>  ondata="response.setAttribute('text'this.childNodes\[0\].serialize())"/&gt;  
>  &lt;simplelayout spacing="4"/&gt;  
>  &lt;edittext id="postdata" multiline="true" width="400" height="200"  
>  text='&amp;lt;project&amp;gt; &amp;lt;title&amp;gt;XXX&amp;lt;/title&amp;gt; &amp;lt;/project&amp;gt;'/&gt;  
>  &lt;button text="post"&gt;  
>  &lt;handler name="onclick"&gt;  
>  ds.setQueryParam("lzpostbody", postdata.text);  
>  ds.setAttribute("querytype", "POST");  
>  ds.setHeader("Content-Type", "application/xml")  
>  ds.doRequest();  
>  &lt;/handler&gt;  
>  &lt;/button&gt;  
>  &lt;edittext id="response" multiline="true" width="400" height="280"/&gt;  
> &lt;/canvas&gt;