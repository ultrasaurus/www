---
title: 'git submodule gotcha'
date: '2009-03-10T02:07:23-07:00'
status: publish
permalink: /2009/03/git-submodule-gotcha
author: sarah
excerpt: ''
type: post
id: 927
category:
    - code
tag: []
post_format: []
---
I anticipate enjoying git submodules for all of the various and sundry dependencies for my project. However there is a bit of a gotcha with my specific use case. It’s seems I’m [not alone](http://blog.buildingwebapps.com/2008/5/20/got-git-submodules-not-a-go-go), but I thought I’d write this up for others who may into the same thing (and for my own future reference).

The issue happens when you have a directory that is checked into git and you decide to delete the directory of checked in files and add a submodule instead. Seems like a common use case to me, but perhaps the creators of git submodules didn’t thinks so. This happened to me in the move from subversion to git. Initially, all of the plugins were accessed as svn externals; however they were not available via git and I wanted to do one migration at a time, so I just checked the source of all of them into vender/plugins. Later, I dug up references to various git repositories where the plugins are now available, and created subrepositories — awesome, right?

The gotcha comes when I switch branches back and forth between the “master” (no submodules, but with checked in source) and “dev” (where my submodule work is). Here’s what happens:

```

$ git checkout master
error: Untracked working tree file 'vendor/plugins/acts_as_list/lib/active_record/acts/list.rb' would be overwritten by merge.
```

Here’s my workaround…  
**To go back to a branch w/o submodules**

```

$ rm -rf vendor/plugins
$ git checkout master
$ git checkout vendor/plugins
```

**To go back to a branch w/ submodules**

```

git checkout dev
git submodule update --init
```

Update: another gotcha, when I tried to merge dev into master I got “fatal: cannot read object… It is a submodule!” found the answer [here](http://n2.nabble.com/git-submodule-merge-madness-td2135496.html) and it worked for me:

```

git merge -s  resolve
```

For the record, I’m working with git version 1.6.1