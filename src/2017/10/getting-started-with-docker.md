---
title: 'getting started with docker'
date: '2017-10-09T07:17:24-07:00'
status: publish
exported_permalink: /2017/10/getting-started-with-docker
author: sarah
excerpt: ''
type: post
id: 6328
category:
    - code
tag: []
post_format: []
---
Learning about docker this weekend… it always is hard to find resources for people who understand the concepts of VMs and containers and need to dive into something just a little bit complicated. I had been through lots of intro tutorials, when docker first arrived on the scene, and was seeking to set up a hosted dev instance for existing open source project which already had a docker set up.

Here’s an outline of the key concepts:

- **docker-machine**: commands to create and manage VMs, whether locally or on a remote server
- **docker**: commands to talk to your active VM that is already set up with docker-machine
- **docker-compose**: a way to create and manage multiple containers on a docker-machine

As happens, I see parallels between human spoken language and new technical terms, which makes sense since these are things made by and for humans. The folks who made Docker invented a kind of language for us to talk to their software.

I felt like I was learning to read in a new language, like pig-latin, where words have a prefix of docker, like some kind of honorific

They use docker- to speak to VMs locally or remotely, and docker (without a dash) is an intimate form of communication with your active VM

Writing notes here, so I remember when I pick this up again. If there are Docker experts reading this, I’d be interested to know if I got this right and if there are other patterns or naming conventions that might help fast-track my learning of this new dialect for deploying apps in this land of containers and virtual machines.

Also, if a kind and generous soul wants to help an open source project, I’ve written up my work-in-progress steps for setting up [OpenOpps-platform dev instance](https://github.com/openopps/openopps-platform/issues/1560) and would appreciate any advice, and of course, would welcome a pull request.