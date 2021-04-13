---
title: 'preferences are the refuge of the weak'
date: '2008-08-03T10:44:49-07:00'
status: publish
permalink: /2008/08/preferences-are-the-refuge-of-the-weak
author: sarah
excerpt: ''
type: post
id: 397
category:
    - Uncategorized
tag: []
post_format: []
---
While reading [about Yahoo’s move to checkboxes](http://www.webpronews.com/blogtalk/2007/06/07/yahoo-learning-email-innovation-lesson) (“Based on user feedback, they found out that users were confused and unfamiliar with the new system, and just plain didn’t like it.”), I learned that Vista had introduced a preference to show checkboxes for multiple-select in the filesystem.

In the folder options dialog, amongst dozens of other options, you can now choose to turn on checkboxes for selection:  
![](http://www.lytebyte.com/wp-content/uploads/2007/07/folder-options-to-enable-check-boxes.png)

This will make checkboxes appear next to files for selection without shift-click, both in list view…  
![](http://www.lytebyte.com/wp-content/uploads/2007/07/multiple-selection-by-check-box.png)

… and in icon view:  
![](http://www.nirmaltv.com/wp-content/uploads/2008/06/image-thumb4.png)

I’ve always said that preferences are the refuge of the weak. In this case, there seems no strong argument to support adding checkboxes as a preference. If checkboxes are easier for novice users, as some argue, then the preference should be on by default. Only advanced users are going to find this preference.

It is a familiar experience on a software development team where someone has a new idea, but not everyone agrees: after long discussion, someone suggests “let’s make it a preference.” Everyone smiles and agrees that this will provide the best of both. However, I disagree. In most mature products, preferences is a vast sea of checkboxes, radio buttons and menus; there are hierarchical trees with obscure categories. It is in the best interest of the end user for the designers of the software to figure out what options best support an effective workflow, which options to surface prominently and which to hide initially to make the software learnable and reduce confusion. Advanced users can show additional panels with deeper options, but they shouldn’t have to dig thru pages of preference panels to switch the interface into an alternate mode.

So, for the software designers, developers, and product managers out there: be strong and make a decision. You know (or should know) the ins and outs of your software in far more detail than the people using it. Think about how the software capabilities interact. If you must display things two different ways, create a local affordance for changing the display and then save the most recent setting. This way it just feels like application state, and the controls are not tucked away in a preference dialog out of context.