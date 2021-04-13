---
title: 'debugging openssl shared libary'
date: '2019-06-17T21:49:03-07:00'
status: publish
permalink: /2019/06/debugging-openssl-shared-libary
author: sarah
excerpt: ''
type: post
id: 6818
category:
    - code
tag: []
post_format: []
---
I’m debugging an issue where my app uses a library that requires me to dynamically link with an openssl library. What’s more I’m debugging it on an old linux version. Sigh.

`gdb` to the rescue!

After figuring out how to build openssl from source, I stumbled upon a gdb trick… suppose you are using a fairly standard open source library (like openssl) and you want to debug something that uses it (some other library that doesn’t work over ssl), gdb will let you know if there’s an easy way to download the symbols! Just type `gdb` + `library name`.

Here’s an example

```
gdb openssl
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-92.el6)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /usr/bin/openssl...(no debugging symbols found)...done.
Missing separate debuginfos, use: debuginfo-install openssl-1.0.1e-57.el6.x86_64
(gdb) quit

```

Now I can use this command to install the debug symbols for the specific version of openssl that is installed on this system:

```
debuginfo-install openssl-1.0.1e-57.el6.x86_64

```

then I can debug my app looking at how it calls openssl. In the gdb session below, I first set a breakpoint in main, and run to that point…

```
(gdb) b main
(gdb) run
Starting program: /home/builder/src/app 
warning: no loadable sections found in added symbol-file system-supplied DSO at 0x7ffff7ffa000
[Thread debugging using libthread_db enabled]

Breakpoint 1, main (argc=4, argv=0x7fffffffe698) at sample.cpp:226
226         LOG("Here I am in main!")

```

now the openssl library is loaded and I can set a breakpoint in it:

```
(gdb) b SSL_CTX_set_verify
Breakpoint 2 at 0x7ffff7734bb0: file ssl_lib.c, line 2040.
(gdb) c
Continuing.
Creating connection object
[New Thread 0x7ffff4bd6700 (LWP 53)]
Connecting to server/app URL: rtmps://live-api-s.facebook.com/rtmp/

Breakpoint 2, SSL_CTX_set_verify (ctx=0x62efe0, mode=1, cb=0x7ffff7acb6c0 <SecuredConnectionIO::VerifyCallback(int, x509_store_ctx_st*)>)
    at ssl_lib.c:2040
2040        ctx->verify_mode=mode;

```

I can look at variables or all of the function arguments:

```
(gdb) p mode
$1 = 1
(gdb) info args
ctx = 0x62efe0
mode = 1
cb = 0x7ffff7acb6c0 <SecuredConnectionIO::VerifyCallback(int, x509_store_ctx_st*)>

```

How cool is that?