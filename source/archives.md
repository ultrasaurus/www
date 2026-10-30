---
layout: base
tags: []
title: Archives
---
# Archives

Links to all of the posts:

{% for post in collections.blog reversed %}
* *{{ post.date | date: "%Y-%m-%d" }}* [{{post.data.title}}]({{ post.url }})
{% endfor %}
