---
title: 'bash context'
date: '2009-05-18T08:23:32-07:00'
status: publish
exported_permalink: /2009/05/bash-context
author: sarah
excerpt: ''
type: post
id: 1327
category:
    - code
tag: []
post_format: []
---
Sometimes it takes quite an effort to be a “lazy programmer” (as in Larry Wall’s [virtues of a programmer](http://en.wikipedia.org/wiki/Larry_Wall#Virtues_of_a_programmer)). I’ve been trying to optimize my workflow as I run into things that make for repetitive typing. I find when I can type less, I have more cycles to think. One of my favorite tools in laziness is bash scripting, but I’m still learning its ins and outs.

**The problem**: Lately I’ve been switching between subversion trees in OpenLaszlo. (Someday I want to convince the team to switch to git, but I’m not sure that would even solve the problem completely, since I also like having multiple webapps installed.) So I’ve got trunk checked out in different directories: a clean one for testing, one I keep for code reviews, a sandbox for whatever I’m working on at the moment, etc. Every time I switch OpenLaszlo contexts, I need to redefine $LPS\_HOME environment variable and cd into that directory. Should be simple, huh?

```

BRANCH="trunk"
[ -n "$1" ] && BRANCH="$BRANCH-$1"

echo "BRANCH=$BRANCH"

export LPS_HOME=/Users/sarah/src/svn/openlaszlo/$BRANCH
cd "/Users/sarah/src/svn/openlaszlo/$BRANCH"
pwd
```

Except this didn’t work. It seemed that ‘cd’ had no effect and $LPS\_HOME wasn’t modified. WTF? Lacking someone to look over my shoulder in my new solo work situation, I emailed my friend [Scott Evans](http://www.antisleep.com) from whom I have learned much bash lore. He emailed me the following:

1\) use “.” to run the script, which runs it in your shell process instead  
of in a child one.

2\) use a bash function instead — these run in your current environment.  
try something like this in your bashrc/bash\_profile:

```

trunk() {
 echo "dollar 1: ${1}"
 if [ -n "${1}" ] ; then
   export LPS_HOME=/Users/sarah/src/svn/openlaszlo/trunk-${1}
 else 
   export LPS_HOME=/Users/sarah/src/svn/openlaszlo/trunk
 fi

 cd $LPS_HOME
 pwd
}
```

Note that I didn’t set something like $TRUNK there — since the thing is running in your shell environment, it’s good practice not to potentially step on existing variables, or leave any variables defined after the fact.

Thanks Scott! Posting here so that I will always remember what I learned today and maybe some other folk will find it helpful.