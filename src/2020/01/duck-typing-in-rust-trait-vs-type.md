---
title: 'duck typing in rust: trait vs type'
date: '2020-01-25T14:33:23-08:00'
status: publish
exported_permalink: /2020/01/duck-typing-in-rust-trait-vs-type
author: sarah
excerpt: ''
type: post
id: 7004
category:
    - code
tag: []
post_format: []
---
A `Trait` in the Rust programming language enables what today’s coders commonly call “duck-typing” (walks like a duck and quacks like a duck).

In Rust, `type` refers to concrete types — the type of a value; whereas, a `Trait` refers to an abstract or generic type. Here the English word *type* lacks the specificity we need to describe these concepts, so we need adjectives to differentiate.

TLDR: traits vs types
---------------------

The `type` keyword lets us define a type alias, like:

```
type Population = i32;

```

This is useful if I’m often passing around specific variables for a Population, and I have function that takes multiple numbers, then the compiler will be able to catch certain classes of errors:

```
fn report(p: Population, num: i32)

```

A Trait is a collection of functions that can be applied to a type (a built-in type, like `i32` or a type that we have defined with a struct, enum or type alias). A good example of a Trait is [ToString](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string) which is part of the Rust standard library:

```
pub trait ToString {
    fn to_string(&self) -> String;
}

```

Here’s a naive approach to implementing ToString on a custom struct:

```
struct Monster {
  eyeball_count: i32,
}

impl ToString for Monster {
  fn to_string(&self) -> String {
    format!("{}-eyed {}", self.eyeball_count, "monster")
  }
}

fn main() {
  let m = Monster { eyeball_count: 3 };
  println!("We just created a {}!", m.to_string())
}

```

Experienced Rustaceans would rarely implement the above code, instead they might implement [std::fmt::Display](https://doc.rust-lang.org/std/fmt/trait.Display.html) which provides additional functionality we probably want, so if I write this instead of `impl ToString for Monster`:

```
impl fmt::Display for Monster {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    write!(f, "{}-eyed {}", self.eyeball_count, "monster")
  }
}

```

Then our code that calls `to_string` will still work, but we can also provide the variable directly to println! (or format!) and it will also work:

```
  println!("We just created a {}!", m);

```

This is because Rust allows for implementing functions on Traits in terms of a generic type.

Traits in context
-----------------

Traits help break down what’s needed and make our code reusable and easier to maintain. Most libraries will use many Traits from the std libary, as well as their own Traits, which can make the learning curve a bit steep, but very flexible once you understand what they do.

So, as I’m learning, it helps me to spell everything out, but then I end up with code that was a bit hard to read. Check out this beauty that I wrote yesterday:

```
async fn read_some<R: AsyncRead + Send + Unpin>(mut reader: R) -> Result<(), std::io::Error>

```

I’m using Rust 1.39 with built-in `async fn` which means that the compiler will build me a future and I can declare as the return value to be whatever type that Future will ultimately produce (or simply what my function returns). In this case, I want to be able to pass in a [tokio::net::TcpStream](https://docs.rs/tokio/0.2.10/tokio/net/struct.TcpStream.html) and also a “ReadHalf” that is returned from [split](https://docs.rs/tokio/0.2.10/tokio/io/fn.split.html).

My first attempt at refactoring was to do this:

```
type Reader = AsyncRead + Send + Unpin;

```

The above code doesn’t do what I wanted. I’ve explained above that `type` creates an alias for a concrete type; however, when we provide Traits, it (unexpected for me) creates a “Trait object” which is not the abstract type I was looking for. What I wanted to do was to define a new Trait that composes the other traits, but has no implementation of its own. Here’s the syntax I was looking for:

```
trait Reader: AsyncRead + Send + Unpin { } 
impl<T: AsyncRead + Send + Unpin> Reader for T {}

```

which I can then use like this:

```
async fn read_some<R: Reader>(mut reader: R) -> Result<(), std::io::Error>

```

or in a slightly more readable form with `where`:

```
async fn read_some<R>(mut reader: R) -> Result<(), std::io::Error>
where R: AsyncReader  

```

If you want to see the working code, I have a few examples here: https://github.com/ultrasaurus/rust-tokio-proxy where each can be executed like this: `cargo run --example reader-type`

- - - - - -

Many thanks to the Alice, David, Lucio and Jeb on Tokio discord who helped me understand types, traits and how they are used in tokio!