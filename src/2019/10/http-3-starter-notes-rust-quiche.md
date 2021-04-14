---
title: 'http/3 starter notes, rust quiche'
date: '2019-10-28T06:08:24-07:00'
status: publish
exported_permalink: /2019/10/http-3-starter-notes-rust-quiche
author: sarah
excerpt: ''
type: post
id: 6873
category:
    - code
tag: []
post_format: []
---
Learning about HTTP/3… Here are some starter notes

- Talk by Lucas Pardue at Demuxed 2019 — seek to 08:51:02 in [twitch video](https://www.twitch.tv/demuxed/video/498918740)
- Another good overview: https://curl.haxx.se/video/curlup-2019/2019-03-31-Robin-Marx-QUIC-details.pdf

Good to know that they are going through a real IETF process so QUIC is evolving. CloudFlare makes it available, and will track the standard, so could be breaking changes ahead!

**Rust implementation “Quiche”**

uses Rust nightly, here’s a cheat sheet to getting set up..

```
git clone --recursive git@github.com:cloudflare/quiche.git

# git submodule update --init --recursive

cargo +nightly build --examples
cargo +nightly test

```

or if you don’t want to keep writing `+nightly` then:

```
rustup override set nightly

```