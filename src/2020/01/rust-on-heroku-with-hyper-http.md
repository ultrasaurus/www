---
title: 'rust on heroku with hyper http'
date: '2020-01-05T18:39:54-08:00'
status: publish
exported_permalink: /2020/01/rust-on-heroku-with-hyper-http
author: sarah
excerpt: ''
type: post
id: 6984
category:
    - code
tag: []
post_format: []
---
Running an app on heroku requires at least one entry point responding to http. An easy way to do this is to use [hyper](hyper.rs) to create a simple web service.

Setup
-----

```
cargo new hello_rust --bin
cd hello_rust
git init
git add .
git commit -m "cargo new hello_rust --bin"

```

add to `Cargo.toml`:

```
[dependencies]
hyper = "0.13"

```

Web service code
----------------

The core code to set up a little web service has a few key parts:

1. the service (`async fn hello`) 
  - an async function that takes a `hyper::Request` and returns a `hyper::Response` in the `Result`
  - [Request](https://docs.rs/hyper/0.13.1/hyper/struct.Request.html) is generic over the Body, so it seems nifty to be able to provide our own Rust types for specific content (like JSON) and also for validating API POST params
  - Result is [Infallible](https://doc.rust-lang.org/std/convert/enum.Infallible.html): a Rust error type signifying that the function never returns an error
2. [make\_service\_fn](https://docs.rs/hyper/0.13.1/hyper/service/fn.make_service_fn.html) — docs are a bit sparse on this, but I think all it does it generate an instance of the service with the Request context that so that each request can run concurrently
3. Server::bind(&amp;addr).serve(…) — Hyper uses a builder pattern where Server::bind generates a [Builder](https://docs.rs/hyper/0.13.1/hyper/server/struct.Builder.html), where you can configure http1/2 support and then a running instance of the Server is created by calling the [serve method](https://docs.rs/hyper/0.13.1/hyper/server/struct.Builder.html#method.serve) with the service function.

To see this in action, replace `main.rs` with this code:

```
use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Request, Response, Server};
use std::convert::Infallible;

async fn hello(_req: Request<Body>) -> Result<Response<Body>, Infallible> {
    Ok(Response::new(Body::from(
        "<HTML><H1>Hello World!</H1><HTML>",
    )))
}

#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {

    let make_svc = make_service_fn(|_conn| {
        async { Ok::<_, Infallible>(service_fn(hello)) }
    });

    let addr = ([0, 0, 0, 0], 3000).into();

    let server = Server::bind(&addr).serve(make_svc);

    println!("Listening on {}", addr);

    server.await?;

    Ok(())
}

```

to run the app locally:

```
cargo run

```

then in the browser, go to <http://localhost:3000/>

Heroku setup
------------

### 1. Heroku CLI

Install [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) or if you already have it:

`heroku update`

Then to set up the app on heroku:

```
heroku create --buildpack emk/rust

```

### 2. Procfile

Add a Procfile for heroku to know what to call when it receives a web request:

```
echo "web: ./target/release/hello_rust" >> Procfile

```

### 3. Port configuration

Heroku requires that we listen on the port specified with the `PORT` env var. So, add the following code and replace the hard-coded port number with this variable:

```
    let port = env::var("PORT")
        .unwrap_or_else(|_| "3000".to_string())
        .parse()
        .expect("PORT must be a number");

```

### 4. Deploy!

Deploy the app by pushing code to the Heroku remote repository that was set up by the CLI in step 1.

```
 git push heroku master

```

Full code for the app is on [github.com/ultrasaurus/hello-heroku-rust](https://github.com/ultrasaurus/hello-heroku-rust/tree/hyper)

Background
----------

My environment info (`rustup show`):

```
stable-x86_64-apple-darwin (default)
rustc 1.39.0 (4560ea788 2019-11-04)

```