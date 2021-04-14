---
title: 'visualization of word frequency'
date: '2007-07-29T23:38:16-07:00'
status: publish
exported_permalink: /2007/07/visualization-of-word-frequency
author: sarah
excerpt: ''
type: post
id: 303
category:
    - Uncategorized
tag: []
post_format: []
---
The Human-Computer Interaction Lab, University of Maryland, [presents](http://www.futureofthebook.org/mckenziewark/gamertheory30/featurelens/) an interesting OpenLaszlo application for analyzing word frequency in a document (via David Temkin).

[![](https://www.ultrasaurus.com/images/blog/featurelens/ui-small.gif)](http://monk.lis.uiuc.edu:6060/openlaszlo-3.3.3-servlet/my-apps/featurelens/src/featurelens.lzx?debug=false&lzt=html)  
[click to interact with FeatureLens](http://monk.lis.uiuc.edu:6060/openlaszlo-3.3.3-servlet/my-apps/featurelens/src/featurelens.lzx?debug=false&lzt=html)

It took a bit of poking around to figure out where to start and what to do with this app. (You want to click the “load” button in the upper right.) I explored the “State of the Union” a bit…

Initially, we can see the frequency of words in the speech:  
![](https://www.ultrasaurus.com/images/blog/featurelens/frequency.png)

I also looked at words which decrease in frequency throughout the document. By selecting “budget” you can see a graph of how often that word is used through the course of the speech:  
![](https://www.ultrasaurus.com/images/blog/featurelens/budget-37-decreasing.png)![](https://www.ultrasaurus.com/images/blog/featurelens/budget.png)

In looking at words that increase in frequency, we can see that “Iraq” is discussed more toward the end of the speech:  
![](https://www.ultrasaurus.com/images/blog/featurelens/iraq-44-increasing.png)![](https://www.ultrasaurus.com/images/blog/featurelens/iraq.png)

The selection of trends in the distribution of pattern frequencies allows collecting meaningful pieces of information about the text. FeatureLens is a “provocational” tool as it gives rise to new questions and hypotheses, as well as insights about the text.