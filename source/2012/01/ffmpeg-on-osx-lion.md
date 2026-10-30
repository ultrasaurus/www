---
title: 'ffmpeg on osx lion'
date: '2012-01-07T21:40:37-08:00'
exported_permalink: /2012/01/ffmpeg-on-osx-lion
id: 3537
category: code
---
Update: [more links and ogg and webm details](https://www.ultrasaurus.com/sarahblog/2013/06/ffmpeg-for-ogg-and-webm/)

I found that I needed to convert an m4a audio file (which is what QuickTime saves when I record audio) to a wav file, so I decided to use my favorite “can opener.” The versatile open source [ffmpeg](http://ffmpeg.org) tool has always seemed to be able to convert anything to anything in audio-video formats.

I decided to pull the source from git:  
```
$ git clone git://source.ffmpeg.org/ffmpeg.git
$ cd ffmpeg/
```

Stable versions are tagged (which I could see with “git tag -l”). I don’t need to live on the edge right now, so I switched to the tag “n0.9.1” which I assume is for the latest stable build “harmony” 0.9.1 and made a local branch based on that.  
```
$ git co n0.9.1
$ git checkout -b n0.9.1
```

Instructions for building ffmpeg are in the “INSTALL” file. I discovered I needed yasm, which I could install with brew. Here’s what I did:  
```
$  brew install yasm
$  ./configure
$ make
CC	libavdevice/alldevices.o
CC	libavdevice/avdevice.o
CC	libavdevice/lavfi.o
AR	libavdevice/libavdevice.a
CC	libavfilter/af_aconvert.o
libavfilter/af_aconvert.c:53: warning: function declaration isn’t a prototype
libavfilter/af_aconvert.c:105: warning: function declaration isn’t a prototype
CC	libavfilter/af_aformat.o
CC	libavfilter/af_anull.o
CC	libavfilter/af_aresample.o
    :
   :
ffserver.c: In function ‘parse_ffconfig’:
ffserver.c:4236: warning: ‘avcodec_get_context_defaults2’ is deprecated (declared at ./libavcodec/avcodec.h:3948)
ffserver.c:4237: warning: ‘avcodec_get_context_defaults2’ is deprecated (declared at ./libavcodec/avcodec.h:3948)
LD	ffserver_g
CP	ffserver
STRIP	ffserver
```
I saw a lot of warnings, but they didn’t seem to negatively affect what I was trying to do. I found a [nice blog post from catswhocode](http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs) to remind me of the usage, and was able to use this simple command:

```
$ ./ffmpeg -i frog.m4a frog.wav
ffmpeg version 0.9.1, Copyright (c) 2000-2012 the FFmpeg developers
  built on Jan  7 2012 21:19:08 with llvm_gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)
  configuration:
  libavutil    51. 32. 0 / 51. 32. 0
  libavcodec   53. 42. 4 / 53. 42. 4
  libavformat  53. 24. 2 / 53. 24. 2
  libavdevice  53.  4. 0 / 53.  4. 0
  libavfilter   2. 53. 0 /  2. 53. 0
  libswscale    2.  1. 0 /  2.  1. 0
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'frog.m4a':
  Metadata:
    major_brand     : M4A
    minor_version   : 0
    compatible_brands: M4V M4A mp42isom
    creation_time   : 2012-01-08 05:09:05
  Duration: 00:00:07.22, start: 0.000000, bitrate: 206 kb/s
    Stream #0:0(und): Audio: aac (mp4a / 0x6134706D), 44100 Hz, stereo, s16, 201 kb/s
    Metadata:
      creation_time   : 2012-01-08 05:09:05
      handler_name    :
Output #0, wav, to 'frog.wav':
  Metadata:
    major_brand     : M4A
    minor_version   : 0
    compatible_brands: M4V M4A mp42isom
    creation_time   : 2012-01-08 05:09:05
    encoder         : Lavf53.24.2
    Stream #0:0(und): Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, stereo, s16, 1411 kb/s
    Metadata:
      creation_time   : 2012-01-08 05:09:05
      handler_name    :
Stream mapping:
  Stream #0:0 -> #0:0 (aac -> pcm_s16le)
Press [q] to stop, [?] for help
size=    1244kB time=00:00:07.22 bitrate=1411.3kbits/s
video:0kB audio:1244kB global headers:0kB muxing overhead 0.003611%

$ ls
frog.m4a  frog.wav
```

Success!!