---
title: 'essential rust tools'
date: '2019-06-03T07:19:23-07:00'
status: publish
exported_permalink: /2019/06/essential-rust-tools
author: sarah
excerpt: ''
type: post
id: 6802
category:
    - code
tag: []
post_format: []
---
Rust has a “community of developers empowered by their tools and each other” (via [Katharina Fey](https://twitter.com/spacekookie) in “[An async story](https://www.youtube.com/watch?v=K_wnB9ibCMg&t=0m1s)“). The Rust community helps each other through effective narrative documentation and attention to error messages, and the robust tooling around Rust drives momentum, overcoming some of the natural hurdles when diving into a new language.

Here’s my list of essential rust tools (so far):

The basics
----------

### rustup

The default tool when you [install rust](https://www.rust-lang.org/tools/install).

Rust has very good offline documentation (perfect for learning on long plane trips!). See `rustup doc help` for full list. Here are some highlights:

```
rustup doc --book              # Rust Programming Language book
rustup doc --rust-by-example   # collection of runnable examples
rustup doc --std               # Standard library API documentation

```

### cargo

Cargo packages Rust code into *crates*. You can find published libraries at [crates.io](https://crates.io/). After getting familiar with `cargo.toml` file which streamlines development and enables reproducible builds, I found command line management easier with [cargo-edit](https://github.com/killercup/cargo-edit):

```
cargo install cargo-edit
cargo add <crate>         # also provides rm, upgrade

```

Rust and Web Assembly
---------------------

The Rust Wasm tooling has improved dramatically over the past year — [wasm-pack](https://rustwasm.github.io/) is the “one-stop shop for building, testing, and publishing Rust-generated WebAssembly.” The [rustwasm book](https://rustwasm.github.io/docs/book/) is very good.

```
cargo install wasm-pack

```

### rust-parcel

I’ve grown to dread building modern web apps with their complex JavaScript build tooling. In learning Rust, I discovered [Parcel](https://parceljs.org/) which lets you [import .rs files from JavaScript](https://parceljs.org/rust.html). Under the hood, it compiles Rust to Web Assembly and hooks it all up into a tidy js src reference for my index.html. Simply breathtaking.

Parcel tool chain is idiomatic for NodeJS folk. `npm run start` will run a local server and watch your files.

```
npm init rust-parcel hello-rust-parcel
cd hello-rust-parcel

```

When you build your web app, it automatically prints out the kinds of things you should want to know. For many uses of Rust, compiled code size doesn’t matter, but for Web apps, it is important to keep an eye on download size:

```
npm run build

> create-rust-parcel@0.0.2 build /Users/sallen/src/rust/hello-rust-parcel
> parcel build index.html

✨  Built in 3.20s.

dist/rust_parcel_bg.d1b79d09.wasm    67.63 KB     13ms
dist/js.caa35af8.js.map              14.65 KB     11ms
dist/js.caa35af8.js                   7.49 KB    2.58s
dist/Cargo.8d29e058.toml              1.17 KB    1.16s
dist/index.html                         228 B    999ms

```

### wasm on the edge?

Interesting to note that Web Assembly isn’t just for client-side browser code. [WebAssembly on Cloudflare Workers](https://blog.cloudflare.com/webassembly-on-cloudflare-workers/) creates potential for new edge capabilities.

TBD
---

I’m just scratching the surface as I learn Rust. My practical applications range from native client and server code, command-line tools along with my early Web app experiments. I don’t expect Rust to be my goto language for everything, but it’s fun to dive in and explore as I climb the steep learning curve of getting my code to reliably compile!

For people ahead of me on your Rust adventures, what essential tools am I missing?