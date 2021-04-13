---
title: 'computer security primer'
date: '2015-12-31T15:17:47-08:00'
status: publish
permalink: /2015/12/computer-security-primer
author: sarah
excerpt: ''
type: post
id: 5783
category:
    - general
tag: []
post_format: []
---
Ivan Krstić provided a computer security primer with some interesting historical context when he introduced the Mac App Sandbox in 2011. I learned these important concepts when I started writing web software in 1995 with the Shockwave player, but I’ve never seen as clear an overview as in the [first 20 minutes of this talk](https://developer.apple.com/videos/play/wwdc2011-203/).

Here are some highlights:

[![unfortunate-assumption](../../../uploads/2015/12/unfortunate-assumption.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/unfortunate-assumption.png)

[![history-of-assumptions](../../../uploads/2015/12/history-of-assumptions.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/history-of-assumptions.png)

We are conditioning our users to ignore our security messages…

[![if-you-are-explaining-you-are-losing](../../../uploads/2015/12/if-you-are-explaining-you-are-losing.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/if-you-are-explaining-you-are-losing.png)

What if we took this approach with car airbags?

[![security-ui-airbag-analogy](../../../uploads/2015/12/security-ui-airbag-analogy.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/security-ui-airbag-analogy.png)

The root problem is one of “ambient privilege.” Just because of the person who happened to run a program, we give that program all of the privileges we would give to the person. However, no human can understand and review all of the lines of code that we execute every day.

We are building complex systems, which *always* have vulnerabilities.

Complexity is growing, and there is no limit on the kind of damage an exploit can do. From cars to fighter planes, the amount of code we are putting into our vehicles has increased dramatically over time.

[![vehicle-loc](../../../uploads/2015/12/vehicle-loc.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/vehicle-loc.png)

100M lines of code in a car today….

[![car-loc](../../../uploads/2015/12/car-loc.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/car-loc.png)

[![what-works](../../../uploads/2015/12/what-works.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/what-works.png)

Mostly, the Mac App Sandbox introduces ideas that the Web Browser introduced in 1993, Shockwave in 1995 with a full program language, then with JavaScript running in its own sandbox a couple of years later. There are some new ideas, of course. One that I particularly like is the notion of leveraging the File Open dialog to capture a user’s intent and seamless allow selective file access only to those files that the user chooses to open.

We need more creative and thoughtful user experience design that allows humans to safely interact with a complex world.