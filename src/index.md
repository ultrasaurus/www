---
layout: base
tags: []
title: the evolving ultrasaurus
pagination:
  data: collections.blog
  size: 3
  reverse: true
  alias: posts
---

*WIP - under construction*

Here are all the posts:

{% for post in pagination.items %}
* *{{ post.date | date: "%Y-%m-%d" }}* [{{post.data.title}}]({{ post.url }})
{% endfor %}
