---
title: 'moving from svn to git'
date: '2009-02-12T04:17:26-08:00'
status: publish
exported_permalink: /2009/02/moving-from-svn-to-git
author: sarah
excerpt: ''
type: post
id: 783
category:
    - code
tag: []
post_format: []
---
I’ve been learning git lately and it seems much easier to use than subversion for branching and merging, but I still have yet to become adept at looking at a file history. It seems to be the way that a lot of projects are moving, especially for rails and open source projects; besides, all the kids are doing it, so I figured I would follow the trend. In addition to using it pretty simply for small projects, I’m moving a project from subversion to git, which turn out to be a little bumpy, so I thought I would share.

I started with these awesomely simple instructions [to cleanly migrate your subversion repository](http://www.simplisticcomplexity.com/2008/03/05/cleanly-migrate-your-subversion-repository-to-a-git-repository/) with the addition of a handy script to automatically [create an svn.authors file](http://technicalpickles.com/posts/creating-a-svn-authorsfile-when-migrating-from-subversion-to-git).

This all seemed to go well, until we tried to run the code and learned that svn-git failed to fetch a directory! svn-git really ought to warn you somehow that it doesn’t support fetching externals. This I learned by noticing that the svn log had no checkins of those files and then saw when I did a clean svn checkout that it was fetching externals for the vendor/plugins directory. Of course that makes a lot of sense, but I didn’t set up the svn so I didn’t know. Then I spent some time wandering through the wilderness of blogs and mailing lists learning about svn externals and git submodules, and I found some interesting clues:

- [tracking ffmpeg in svn as a git submodule](http://kerneltrap.org/mailarchive/git/2007/5/1/245002) with fancy instructions on how to make branches of those projects as submodules that can be committed to
- [svn externals to git submodules](http://panthersoftware.com/articles/view/3/svn-s-svn-externals-to-git-s-submodule-for-rails-plugins) which lists 5 options with a follow-up article on [using sub-projects and git-rails-plugins](http://panthersoftware.com/articles/view/4/git-svn-dcommit-workaround-for-git-submodules)

After all of that, I stepped back and thought about what I actually needed for this project. We’re currently at 2.0.2 and planning to upgrade to the the latest, and it turns out that all of the plugins that we’re currently tracking on subversion have moved their latest versions to git. So, I decided to just pull in the vendor/plugins directory verbatim, detaching the external reference, and move to git submodules as we upgrade. What I really wanted to do, but didn’t see how to, was to reference the plugin code as an http URL and keep as a submodule, so that I would have a handy reference to source location and revision.

```

$mkdir project-tmp
$cd project-tmp/
$git-svn init svn://myserver/project/trunk
$git config svn.authorsfile ../svn-users.txt
$git-svn fetch
    :
Checked out HEAD:
  svn://myserver/project/trunk r999

$cd vendor
$svn co svn://whatever.com/myproject/trunk/vendor/plugins
$cd plugins
$rm -rf .svn  
$git add .

$cd ..
$git clone project-tmp project
$rm -rf project-tmp
```