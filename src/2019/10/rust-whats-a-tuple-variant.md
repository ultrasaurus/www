---
title: '[rust] what&#8217;s a tuple variant?'
date: '2019-10-13T08:17:17-07:00'
status: publish
exported_permalink: /2019/10/rust-whats-a-tuple-variant
author: sarah
excerpt: ''
type: post
id: 6859
category:
    - code
tag: []
post_format: []
---
Learning Rust, like with any new programming language, requires learning the language of compiler error messages, which is partly about the Rust language itself and partly how Rust programmers talk about the language. One of the first error messages that tripped me up was when I was attempting to return a `Result`.

I wrote a function that had a syntax error like this one:

```
fn get_num() -> Result<i32, &'static str> {
  let result = 4;
  OK(result);
}

```

Which generates this error:

```
   |
11 | fn get_num() -> Result<i32, &'static str> {
   |    -------      ^^^^^^^^^^^^^^^^^^^^^^^^^ expected enum `std::result::Result`, found ()
   |    |
   |    implicitly returns `()` as its body has no tail or `return` expression
12 |   let result = 4;
13 |   OK(result);
   |             - help: consider removing this semicolon
   |
   = note: expected type `std::result::Result<i32, &'static str>`
              found type `()`

```

So, of course, I remove the semicolon, which leads to this error:

```
error[E0425]: cannot find function `OK` in this scope
  --> examples/tuple.rs:13:3
   |
13 |   OK(result)
   |   ^^ help: a tuple variant with a similar name exists: `Ok`

```

The compiler doesn’t know what I’m attempting to do, so it gives me two possibilities:  
 1. cannot find function `OK`  
 2. a tuple variant with a similar name exists: `Ok`

When I first saw this error, I thought the second part was simply pointing out the location of the error and giving me more detail. I spent a few hours trying to figure out where I had created a conflicting tuple variant… and what the heck was a tuple variant? I copy/pasted seemingly identical code and somehow the problem went away but I didn’t know what I had fixed. When I hit this error a second time, I isolated a small test case, wrote a [StackOverflow post](https://stackoverflow.com/questions/55800693/whats-a-a-tuple-variant-understanding-compiler-error-message/55802994#55802994) and some helpful person pointed out that `Ok` in Rust has a lower-case `k`.

For some reason my fingers really want to type `OK` and my eyes really want to see that as a correct formation of the syntax, so I get this error now and then. “Hello, tuple variant my old friend!” says the voice in my head that anthropomorphizes my code. Then as my fingers automatically fix the typo and recompile, I reflect on Rust tuples and wonder about tuple variants.

So, what’s a tuple?
-------------------

A tuple is a “finite heterogeneous sequence,” and one of Rust’s primitive type (see [doc](https://doc.rust-lang.org/std/primitive.tuple.html)).

The [enum keyword](https://doc.rust-lang.org/std/keyword.enum.html) allows us to express a type which has multiple *variants* which from context must be *tuple variants*, though I was never able to find a reference to this in the docs.

**Update**:  
– [discussion on twitter](https://twitter.com/ultrasaurus/status/1183402662340907008)  
– bug filed with suggestions from twitter thread: https://github.com/rust-lang/rust/issues/65386  
– there are some very awesome people developing the Rust language (and surrounding ecosystem of tools and docs)