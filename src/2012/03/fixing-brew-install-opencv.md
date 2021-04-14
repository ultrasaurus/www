---
title: 'fixing brew install opencv on osx'
date: '2012-03-30T03:46:27-07:00'
status: publish
exported_permalink: /2012/03/fixing-brew-install-opencv
author: sarah
excerpt: ''
type: post
id: 3583
category:
    - code
tag: []
post_format: []
---
This is more about fixing my brew install, than about opencv. As with many install issues the root cause was actually pretty simple, but finding it was challenging. Along the way, I fixed a number of issues which took a bit of digging to find, so I’m leaving a little trail on the web in case other people run into the same things — or in case some inspired open source citizen has time to add better solution messages to brew. The first step of any solution, is, of course, understanding the problem.

$ brew install opencv  
==&gt; Installing opencv dependency: cmake  
==&gt; Downloading https://downloads.sf.net/project/machomebrew/Bottles/cmake-2.8.7-bottle.tar.gz  
\######################################################################## 100.0%  
Error: SHA1 mismatch  
Expected: f218ed64ce6e7a5d3670acdd6a18e5ed95421d1f  
Got: 3a57f6f44186e0dba34ef8b8fb4a9047e9e5d8a3

solution:  
$ brew update  
 :  
 :  
Error: Failed executing: make install (libtiff.rb:18)  
If `brew doctor’ does not help diagnose the issue, please report the bug:  
 https://github.com/mxcl/homebrew/wiki/reporting-bugs

tl;dr;  
install command-line tools from developer.apple.com
------------------------------------------------------------

before I figured that out I fixed all of the issues found with ‘brew doctor’

$ brew doctor

Warning: Some directories in /usr/local/share/man aren’t writable.  
This can happen if you “sudo make install” software that isn’t managed  
by Homebrew. If a brew tries to add locale information to one of these  
directories, then the install will fail during the link step.  
You should probably `chown` them:

 /usr/local/share/man/de  
 /usr/local/share/man/de/man1

solution:  
$ sudo chown sarah /usr/local/share/man/de/\*  
$ sudo chown sarah /usr/local/share/man/\*

Warning: “config” scripts exist outside your system or Homebrew directories.  
`./configure` scripts often look for \*-config scripts to determine if  
software packages are installed, and what additional flags to use when  
compiling and linking.

Having additional scripts in your path can confuse software installed via  
Homebrew if the config script overrides a system or Homebrew provided  
script of the same name. We found the following “config” scripts:

 /Library/Frameworks/Python.framework/Versions/2.7/bin/python-config  
 /Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7-config

solution:  
Uninstalled python, which I don’t use much — I figure I can install later with brew  
$ sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7  
$ sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7  
$ sudo rm -rf “/Applications/Python 2.7”  
$ sudo rm /usr/local/bin/py\*

Warning: You have unlinked kegs in your Cellar  
Leaving kegs unlinked can lead to build-trouble and cause brews that depend on  
those kegs to fail to run properly once built.

 coreutils  
 geoip

solution:  
$ brew link coreutils  
Linking /usr/local/Cellar/coreutils/8.12… 0 symlinks created  
$ brew link geoip  
Linking /usr/local/Cellar/geoip/1.4.6… 2 symlinks created

Warning: You have uncommitted modifications to Homebrew’s core.  
Unless you know what you are doing, you should run:  
 cd /usr/local &amp;&amp; git reset –hard

tried this:  
$ cd /usr/local &amp;&amp; git reset –hard  
HEAD is now at ffb9aa5 Remove “\_\_brew\_ps1” function from completion  
–&gt; didn’t work

solution:  
$ pushd /usr/local  
$ git status  
–&gt; lots of untracked files, no idea how I got into that state  
$ git add .  
$ git reset HEAD –hard  
$ popd

Warning: Your Xcode is configured with an invalid path.  
You should change it to the correct path. Please note that there is no correct  
path at this time if you have \*only\* installed the Command Line Tools for Xcode.  
If your Xcode is pre-4.3 or you installed the whole of Xcode 4.3 then one of  
these is (probably) what you want:

 sudo xcode-select -switch /Developer  
 sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer

DO NOT SET / OR EVERYTHING BREAKS!

I don’t have anything at /Developer, so I did this:  
$ sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer

$ brew doctor  
Your system is raring to brew.

Of course, it wasn’t, the key clue for me was finding this in the long stream of installation output:  
tiffgt.c:35:11: fatal error: ‘OpenGL/gl.h’ file not found

which convinced me that I was missing some fundamentals. Searching on the text of the error led me to:  
<https://github.com/mxcl/homebrew/issues/11088>

Ideally ‘brew doctor’ would have caught that I was missing the command-line tools that don’t get installed automatically with XCode 4.3. I installed those and all was well.