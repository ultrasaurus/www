---
title: 'animated sorting algorithms'
date: '2008-11-16T10:57:32-08:00'
status: publish
exported_permalink: /2008/11/animated-sorting-algorithms
author: sarah
excerpt: ''
type: post
id: 438
category:
    - Uncategorized
tag:
    - visualization
post_format: []
---
[David Martin](http://vision.bc.edu/~dmartin/), an assistant professor at Boston College, has published a fabulous [sorting visualization](http://vision.bc.edu/~dmartin/teaching/sorting/anim-html/all.html) (via [HMK](http://www.extragroup.de/weblog/hmk/archives/004857.html)).

These should be a must-see for every computer science student. He includes some good notes about what we should be looking for and why we might care (excerpted below). Often people publish marvelous visualizations, but people who are new to the subject matter can miss key aspects of what they might learn from the detailed visual cues. It is great to see the combination here.

> These visualizations are intended to:
> 
> \* Show how each algorithm operates.  
> \* Show that there is no best sorting algorithm.  
> \* Show the advantages and disadvantages of each algorithm.  
> \* Show that worse-case asymptotic behavior is not the deciding factor in choosing an algorithm.  
> \* Show that the initial condition (input order and key distribution) affects performance as much as the algorithm choice.
> 
> The ideal sorting algorithm would have the following properties:
> 
> \* Stable: Equal keys aren’t reordered.  
> \* Operates in place, requiring O(1) extra space.  
> \* Worst-case O(n·lg(n)) key comparisons.  
> \* Worst-case O(n) swaps.  
> \* Adaptive: Speeds up to O(n) when data is nearly sorted or when there are few unique keys.
> 
> There is no algorithm that has all of these properties, and so the choice of sorting algorithm depends on the application.