---
title: 'subjective performance'
date: '2005-07-03T14:50:27-07:00'
status: publish
exported_permalink: /2005/07/subjective-performance
author: sarah
excerpt: ''
type: post
id: 170
category:
    - Uncategorized
tag: []
post_format: []
---
We’ve recently changed bug databases from [Bugzilla](http://www.bugzilla.org/) to [JIRA](http://www.atlassian.com/software/jira/). We made this choice since JIRA allows us to effectively manage multiple projects for multiple customers. I also really like the home portal UI that lets me set up my default view to have custom reports and bug lists. However, I find it hugely frustrating because JRIA feels much, much slower than bugzilla.

It is interesting to note that the perceived slowness is not only due to the speed of fetching each page. (Both systems are pretty standard HTML web applications.) Bugzilla has only one view for bugs, which allows you to view and edit details. When I look at a list of bugs in JIRA, I need to click once to view the bug, then click again to edit it. I didn’t mind this too much when I was using JIRA as an engineer on [OpenLaszlo](www.openlaszlo.org), but when we switched to using it internally for a project I’m managing, it is a different story. As an engineer, I look at bugs more often than I edit them, and I frequently make a only single edit per session. When managing a project, I look at overviews of dozens or hundreds of bugs at a time; I know the details of almost every bug, so I rarely need to view the whole bug report, but I often need to change the priority, milestone, or who the bug is assigned to. I often go thru a list of bugs and need to edit each one.

So… the bugzilla workflow is this:  
1\. find list of bugs that I want to modify  
2\. click on the first one  
3\. make my edit, it automatically shows me the next bug, so I can go immediately repeat this step

In JIRA, the workflow is:  
1\. find list of bugs that I want to modify  
2\. click on the first one  
3\. click edit  
4\. make my edit, OK returns me to the non-editable bug report  
5\. click next, got to step three

That is 3 more clicks for each bug. So, even though each page request may only be 50% slower than bugzilla, my typical operation is 3x slower than that. This could be easily fixed in the UI by adding an edit link to the bug list and an “edit next” option after editing an item in a search list.

At Laszlo we talk a lot about subjective performance vs. quantitative performance. Sometimes something is the same speed by the stopwatch, but can feel faster or slower depending on user feedback (or lack thereof). It is also important to look at use cases, particularly use cases for repetitive actions.

It is also really interesting to notice how everything feels difficult until I’m used to it. I like to know where I am and how to do what I want. I’m used to that in the interface I’m used to. Even though I hated it when I first learned it. It is the devil I know. Using a new application, I am hugely frustrated when I don’t know how to accomplish the task I have in mind. In some cases, I can see that the UI is not actually any worse, only different, and I have to laugh at myself as I grind my teeth and force myself to actually read the screen before knowing what to click.