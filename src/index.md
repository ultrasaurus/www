---
layout: base
tags: []
title: Welcome to my blog
---

Here are all the posts:

{% for post in collections.blog %}
* *{{ post.date | date: "%Y-%m-%d" }}* [{{post.data.title}}]({{ post.url }})
{% endfor %}