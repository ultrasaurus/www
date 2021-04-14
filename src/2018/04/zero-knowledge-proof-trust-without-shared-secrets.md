---
title: 'zero-knowledge proof: trust without shared secrets'
date: '2018-04-07T10:52:58-07:00'
status: publish
exported_permalink: /2018/04/zero-knowledge-proof-trust-without-shared-secrets
author: sarah
excerpt: ''
type: post
id: 6569
category:
    - general
tag: []
post_format: []
---
In cryptography we typically share a secret which allows us to decrypt future messages. Commonly this is a password that I make up and submit to a Web site, then later produce to verify I am the same person.

I missed Kazue Sako’s [Zero Knowledge Proofs 101](http://iiw.idcommons.net/Zero_Knowledge_Proofs_101) presentation at [IIW](https://www.internetidentityworkshop.com/) last week, but Rachel Myers shared an impressively simply retelling in the car on the way back to San Francisco, which inspired me to read the notes and review the proof for myself. I’ve attempted to reproduce this simple explanation below, also noting additional sources and related articles.

Zero Knowledge Proofs (ZPKs) are very useful when applied to internet identity — with an interactive exchange you can prove you know a secret without actually revealing the secret.

Understanding Zero Knowledge Proofs with simple math:

### x -&gt; f(x)

Simple one way function. Easy to go one way from `x` to `f(x)` but mathematically hard to go from `f(x)` to `x.`

The most common example is a hash function. [Wired: What is Password Hashing?](https://www.wired.com/2016/06/hacker-lexicon-password-hashing/) provides an accessible introduction to why hash functions are important to cryptographic applications today.

### f(x) = g ^ x mod p

Known(public): `g`, `p`  
\* `g` is a constant  
\* `p` has to be prime

Easy to know `x` and compute `g ^ x mod p` but difficult to do in reverse.

### Interactive Proof

Alice wants to prove Bob that she knows `x` without giving any information about `x`. Bob already knows `f(x)`. Alice can make `f(x)` public and then prove that she knows `x` through an interactive exchange with anyone on the Internet, in this case, Bob.

1. Alice publishes f(x): `g^x mod p`
2. Alice picks random number `r`
3. Alice sends Bob `u` = g^r mod p
4. Now Bob has artifact based on that random number, but can’t actually calculate the random number
5. Bob returns a challenge `e`. Either 0 or 1
6. Alice responds with `v`:  
  If 0, `v = r`  
  If 1, `v = r + x`
7. Bob can now calculate:  
  If e == 0: Bob has the random number `r`, as well as the publicly known variables and can check if `u == g^v mod p`  
  If e == 1: `u*f(x) = g^v (mod p)`

I believe step 6 is true based on [Congruence of Powers](https://proofwiki.org/wiki/Congruence_of_Powers), though I’m not sure that I’ve transcribed e==1 case accurately with my limited ascii representation.

If `r` is true random, equally distributed between zero and `(p-1)`, this does not leak any information about `x`, which is pretty neat, yet not sufficient.

In order to ensure that Alice cannot be impersonated, multiple iterations are required along with the use of large numbers (see [IIW session notes](http://iiw.idcommons.net/Zero_Knowledge_Proofs_101)).

Further Reading
---------------

- [Comparing Information Without Leaking It](https://www.stat.berkeley.edu/users/aldous/157/Papers/fagin.pdf) Ronald Fagin, Moni Naor, Peter Winkler, 1996.
- [The Knowledge Complexity of Interactive Proof-Systems](http://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf): original 1985 paper by Shafi Goldwasser, Silvio Micali, and Charles Rackoff
- [How to Explain Zero-Knowledge Protocols to Your Children](http://pages.cs.wisc.edu/~mkowalcz/628.pdf) Quisquater, Jean-Jacques; Guillou, Louis C.; Berson, Thomas A. (1990). Advances in Cryptology – CRYPTO ’89: Proceedings. 435: 628–631.
- [Applied Kid Cryptography or How To Convince Your Children You Are Not Cheating](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=8ED92C8B3C84F999CADFE20D9012322C?doi=10.1.1.46.9932&rep=rep1&type=pdf) Moni Naor, Yael Naor, Omer Reingold, 1999