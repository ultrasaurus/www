---
layout: base
title: Code
date: '2009-01-09T05:51:52-08:00'
status: publish
exported_permalink: /category-code
author: sarah
excerpt: ''
type: page
id: 584
---

{% assign code_collection = collections.blog | category: "code" %}

# {{ title }}

{% for post in code_collection reversed %}

* *{{ post.date | date: "%Y-%m-%d" }}* [{{post.data.title}}]({{ post.url }})

{% endfor %}
