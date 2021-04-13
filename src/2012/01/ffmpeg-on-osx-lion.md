---
title: 'ffmpeg on osx lion'
date: '2012-01-07T21:40:37-08:00'
status: publish
permalink: /2012/01/ffmpeg-on-osx-lion
author: sarah
excerpt: ''
type: post
id: 3537
category:
    - code
tag: []
post_format: []
---
Update: [more links and ogg and webm details](https://www.ultrasaurus.com/sarahblog/2013/06/ffmpeg-for-ogg-and-webm/)

I found that I needed to convert an m4a audio file (which is what QuickTime saves when I record audio) to a wav file, so I decided to use my favorite “can opener.” The versatile open source [ffmpeg](http://ffmpeg.org) tool has always seemed to be able to convert anything to anything in audio-video formats.

I decided to pull the source from git:  
`<br></br>$ git clone git://source.ffmpeg.org/ffmpeg.git<br></br>$ cd ffmpeg/<br></br>`

Stable versions are tagged (which I could see with “git tag -l”). I don’t need to live on the edge right now, so I switched to the tag “n0.9.1” which I assume is for the latest stable build “harmony” 0.9.1 and made a local branch based on that.  
`<br></br>$ git co n0.9.1<br></br>$ git checkout -b n0.9.1<br></br>`

Instructions for building ffmpeg are in the “INSTALL” file. I discovered I needed yasm, which I could install with brew. Here’s what I did:  
`<br></br>$  brew install yasm<br></br>$  ./configure<br></br>$ make<br></br>CC	libavdevice/alldevices.o<br></br>CC	libavdevice/avdevice.o<br></br>CC	libavdevice/lavfi.o<br></br>AR	libavdevice/libavdevice.a<br></br>CC	libavfilter/af_aconvert.o<br></br>libavfilter/af_aconvert.c:53: warning: function declaration isn’t a prototype<br></br>libavfilter/af_aconvert.c:105: warning: function declaration isn’t a prototype<br></br>CC	libavfilter/af_aformat.o<br></br>CC	libavfilter/af_anull.o<br></br>CC	libavfilter/af_aresample.o<br></br>    :<br></br>   :<br></br>ffserver.c: In function ‘parse_ffconfig’:<br></br>ffserver.c:4236: warning: ‘avcodec_get_context_defaults2’ is deprecated (declared at ./libavcodec/avcodec.h:3948)<br></br>ffserver.c:4237: warning: ‘avcodec_get_context_defaults2’ is deprecated (declared at ./libavcodec/avcodec.h:3948)<br></br>LD	ffserver_g<br></br>CP	ffserver<br></br>STRIP	ffserver<br></br>`  
I saw a lot of warnings, but they didn’t seem to negatively affect what I was trying to do. I found a [nice blog post from catswhocode](http://www.catswhocode.com/blog/19-ffmpeg-commands-for-all-needs) to remind me of the usage, and was able to use this simple command:

`<br></br>$ ./ffmpeg -i frog.m4a frog.wav<br></br>ffmpeg version 0.9.1, Copyright (c) 2000-2012 the FFmpeg developers<br></br>  built on Jan  7 2012 21:19:08 with llvm_gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)<br></br>  configuration:<br></br>  libavutil    51. 32. 0 / 51. 32. 0<br></br>  libavcodec   53. 42. 4 / 53. 42. 4<br></br>  libavformat  53. 24. 2 / 53. 24. 2<br></br>  libavdevice  53.  4. 0 / 53.  4. 0<br></br>  libavfilter   2. 53. 0 /  2. 53. 0<br></br>  libswscale    2.  1. 0 /  2.  1. 0<br></br>Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'frog.m4a':<br></br>  Metadata:<br></br>    major_brand     : M4A<br></br>    minor_version   : 0<br></br>    compatible_brands: M4V M4A mp42isom<br></br>    creation_time   : 2012-01-08 05:09:05<br></br>  Duration: 00:00:07.22, start: 0.000000, bitrate: 206 kb/s<br></br>    Stream #0:0(und): Audio: aac (mp4a / 0x6134706D), 44100 Hz, stereo, s16, 201 kb/s<br></br>    Metadata:<br></br>      creation_time   : 2012-01-08 05:09:05<br></br>      handler_name    :<br></br>Output #0, wav, to 'frog.wav':<br></br>  Metadata:<br></br>    major_brand     : M4A<br></br>    minor_version   : 0<br></br>    compatible_brands: M4V M4A mp42isom<br></br>    creation_time   : 2012-01-08 05:09:05<br></br>    encoder         : Lavf53.24.2<br></br>    Stream #0:0(und): Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, stereo, s16, 1411 kb/s<br></br>    Metadata:<br></br>      creation_time   : 2012-01-08 05:09:05<br></br>      handler_name    :<br></br>Stream mapping:<br></br>  Stream #0:0 -> #0:0 (aac -> pcm_s16le)<br></br>Press [q] to stop, [?] for help<br></br>size=    1244kB time=00:00:07.22 bitrate=1411.3kbits/s<br></br>video:0kB audio:1244kB global headers:0kB muxing overhead 0.003611%`

$ ls  
frog.m4a frog.wav

Success!!