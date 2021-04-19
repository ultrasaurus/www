---
layout: base
tags: []
title: the evolving ultrasaurus
---

{% assign posts = collections.blog | reversed %}
{% assign post = posts | last %}
{% assign prev = posts | getPreviousCollectionItem: post %}


{% include _post_highlight %}

---

read previous post: [{{prev.data.title}}]({{ prev.url }})
