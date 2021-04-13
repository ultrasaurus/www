---
title: 'building tesseract from source'
date: '2013-07-15T02:39:42-07:00'
status: publish
permalink: /2013/07/building-tesseract-from-source
author: sarah
excerpt: ''
type: post
id: 4081
category:
    - code
tag: []
post_format: []
---
Thanks to the [prior work of Matt Christy](http://emop.tamu.edu/node/45) at [eMOP](http://emop.tamu.edu/), I got started building [Tesseract](https://code.google.com/p/tesseract-ocr/) from source (on Mac OSX 10.8.4).

Here’s my slightly modified workflow:

```

svn checkout http://tesseract-ocr.googlecode.com/svn/trunk/ tesseract-ocr
cd tesseract-ocr
./autogen.sh
mkdir build
cd build
../configure
make
make install
```

recently a makefile changed, and I need to regenerate them, starting at the source code root:

```

autoreconf --force --install
cd build
../configure
make 
make install
```

Making a “build” directory, makes it easier to keep track of source code changes with svn. I set up my global ignores to ignore the interim files and directories.

```

vi ~/.subversion/config
```

then I uncommented this line and added everything after .DS\_Store

```

global-ignores = *.o *.lo *.la *.al .libs *.so *.so.[0-9]* *.a *.pyc *.pyo
   *.rej *~ #*# .#* .*.swp .DS_Store *.in build config configure *.cache
   aclocal.m4 m4
```

So then I only see source code files that are added or modified when I check

```

svn status
```