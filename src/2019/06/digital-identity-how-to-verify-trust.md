---
title: 'digital identity: how to verify trust?'
date: '2019-06-16T05:56:27-07:00'
status: publish
permalink: /2019/06/digital-identity-how-to-verify-trust
author: sarah
excerpt: ''
type: post
id: 6560
category:
    - general
tag: []
post_format: []
---
How can we communicate with each other on the Internet so that we know each other when we want to be known, yet can have privacy or anonymity when appropriate? My brief notes from April 2018 Internet Identity Workshop (below) still feel relevant a year later.

If we believe that a particular person is trust-worthy, to trust their digital representation, we somehow need to identify that some bits that travel across wires or air actually originate from that person.

In today’s Web, we have a network of trusted authorities, typically my social network or email provider creates a relationship with me and I prove my identity with a password. The challenge is that they also house all of my personal data — could there be a way for me to identify myself without making myself vulnerable to the whims or errors of these companies? New models are emerging.

- Mobile Drivers License: British Columbia and U.S. Commerce Department’s National Institute of Standards and Technology (NIST) have funded development of a new kind of digital ID. Folks are working on ways to validate the identity and “claims” of an individual. This is not just for fraud detection. It also potentially protects the privacy of an individual, in contrast to a traditional drivers license, where I must reveal my home address while proving that I’m over 21.
- Decentralized Identifier (DID): a standard way for individuals and organizations to create permanent, globally unique, cryptographically verifiable identifiers entirely under the identity owner’s control. [Sovrin Foundation Whitepaper](https://sovrin.org/wp-content/uploads/2018/03/Sovrin-Protocol-and-Token-White-Paper.pdf)
- With blockchains, every public key can now have its own address, enabling a decentralized self-service registry for public keys.
- Trust without shared secrets. In cryptography we typically share a secret which allows us to decrypt future messages. But the best way to keep a secret is not to tell anyone. We can actually verify a secret without knowing it. [Zero-knowledge proof](https://www.ultrasaurus.com/2018/04/zero-knowledge-proof-trust-without-shared-secrets/)
- Object capabilities. In the real world we have physical objects that we can transfer for very specific authorization (e.g. a key to your car) whereas digital keys must be kept secret to avoid replication — what if authorization were couple with objects in the digital world. Some basic examples illustrate the framework, discussed further in [false dichotomy of control vs sharing](https://www.ultrasaurus.com/2018/04/false-dichotomy-of-control-vs-sharing/).

Full notes from IIW 26: [PDF Proceedings](https://raw.githubusercontent.com/windley/IIW_homepage/gh-pages/assets/proceedings/IIWXXVI_Book_of_Proceedings.pdf), [wiki](https://iiw.idcommons.net/IIW_26_Session_Notes)

*More about IIW*

The Internet Identity Workshop ([IIW](https://www.internetidentityworkshop.com/)) gathers experts across the industry to solve this particular question. People share their understanding of the problem and potential solutions in this unique unconference twice a year. I always learn unexpected and useful technical solutions, and more importantly gain a deeper understanding of this challenging problem of identity.