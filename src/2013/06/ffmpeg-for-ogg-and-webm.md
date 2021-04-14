---
title: 'ffmpeg for ogg and webm'
date: '2013-06-06T23:05:13-07:00'
status: publish
exported_permalink: /2013/06/ffmpeg-for-ogg-and-webm
author: sarah
excerpt: ''
type: post
id: 3893
category:
    - code
tag: []
post_format: []
---
I wanted to experiment with Ogg and WebM and the &lt;video&gt; tag, and I thought the easiest way would be with my favorite command-line transcoder, ffmpeg. It’s fabulous support for just about every audio and video file format makes it fabulous for hacking.

Sadly “brew install ffmpeg” doesn’t support the new file formats and codecs, so I had to compile it myself, as well as the codec libraries. Here’s what worked (on MacOSX Mountain Lion):

0\. **Clone from git and use a stable branch**  
Check the bottom of the [download page](http://www.ffmpeg.org/download.html) for descriptions of latest stable versons.

```
git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg
```

Look for the version tag you want with: `git tag -l`  
I picked 1.2.1 “Magic”

```
git checkout -b n1.2.1
```

1\. **Install Xcode, Homebrew, then and Remaining Dependendencies**  
following [MacOSXCompilationGuide](http://ffmpeg.org/trac/ffmpeg/wiki/MacOSXCompilationGuide) instructions.

2\. Compile libvpx (needed for WebM)  
I took these instructions from the [UbuntuCompilationGuide](http://ffmpeg.org/trac/ffmpeg/wiki/UbuntuCompilationGuide), and swapped out the prefix to be what the Mac instructions told me to do:  
`<br></br> git clone --depth 1 http://git.chromium.org/webm/libvpx.git<br></br>cd libvpx<br></br>./configure --prefix=/usr/local --disable-examples<br></br>make<br></br>sudo make install<br></br>make clean<br></br>cd ..<br></br>`

3\. Configure &amp; build ffmpeg  
I picked just the libraries I needed plus whatever didn’t require extra dependencies:

```

./configure --enable-gpl --enable-version3 --enable-nonfree --enable-postproc --enable-libaacplus --enable-libcelt --enable-libfaac --enable-libfdk-aac --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-openssl --enable-libopus --enable-libschroedinger --enable-libspeex --enable-libtheora --enable-libvo-aacenc --en
make && make install
```

Ready to Make Movies!
---------------------

### Ogg Theora/Vorbis

I just followed the instructions on the [ffmpeg wiki](http://ffmpeg.org/trac/ffmpeg/wiki/TheoraVorbisEncodingGuide) I used lower video and audio quality since the wiki recommendations ended up creating a huge file.

```
ffmpeg -i mymovie.mov -codec:v libtheora -qscale:v 3 -codec:a libvorbis -qscale:a 3 mymovie.ogv
```

### WebM

```
ffmpeg -i mymovie.mov -vcodec libvpx -acodec libvorbis mymovie.webm
```

size chart

```

 2788953  pool-480p.mov
19459157  pool.mov
 2870873  pool.mp4
  833597  pool.webm
 3022359  pool3v3a.ogv
 4398308  pool4v3a.ogv
 5755066  pool5v5a.ogv
 7767888  pool6v5a.ogv
11424378  pool7v5a.ogv
```