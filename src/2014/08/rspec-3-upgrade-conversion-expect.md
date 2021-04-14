---
title: 'rspec 3 upgrade: conversion of should to expect'
date: '2014-08-09T18:22:38-07:00'
status: publish
exported_permalink: /2014/08/rspec-3-upgrade-conversion-expect
author: sarah
excerpt: ''
type: post
id: 5186
category:
    - code
tag: []
post_format: []
---
**update**: follow the [rspec upgrade guide](https://relishapp.com/rspec/docs/upgrade) and try the [transpec](https://github.com/yujinakayama/transpec) gem

- - - - - -

Upgrading a Rails app to RSpec 3, I appreciated [Jake Boxer’s guide](http://jakeboxer.com/blog/2012/07/09/converting-to-the-new-rspec-2-dot-11-expectation-syntax/). However, his regular expressions didn’t work in the editors I use, so I whipped up some command-line options that use the flexible unix utility sed.

If you want to actually understand the following scripts, I recommend [Bruce Barnett’s sed tutorial](http://www.grymoire.com/unix/Sed.html#TOC) and remember [xargs is your friend](https://www.ultrasaurus.com/2008/06/bash-xargs-is-your-friend/).

Also, there are a few differences with sed on OSX, so these may not work on other platforms.

I didn’t attempt to handle multi-lined expressions, so I searched my spec directory for “lambda” in advance and changed those manually, and, of course, found a few other exceptions by running my tests afterwards.

Change “should ==” to “should eq”
---------------------------------

You’ll need to change other operators also, but this was a pattern that happened to be very common in my code.

```

find . -type f -print0 | xargs -0 sed -i "" -E "s/^([[:space:]]+)(.*)\.should ==[:space]*(.*)[:space]*$/\1\2.should eq(\3)/g"
```

Change “whatever.should” to “expect(whatever).to”
-------------------------------------------------

This also works for should\_not, since it is okay to say .to\_not, even though I usually see people wrote .not\_to

```

find . -type f -print0 | xargs -0 sed -i "" -E "s/^([[:space:]]+)(.*)\.should/\1expect(\2).to/g"
```

Also, check out: [Cyrus Stoller’s upgrade tips](http://www.cyrusstoller.com/2014/07/02/upgrading-to-rspec-3/)