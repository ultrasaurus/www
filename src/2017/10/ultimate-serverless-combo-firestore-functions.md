---
title: 'ultimate serverless combo: Firestore + Functions'
date: '2017-10-03T10:07:27-07:00'
status: publish
permalink: /2017/10/ultimate-serverless-combo-firestore-functions
author: sarah
excerpt: ''
type: post
id: 6318
category:
    - code
tag: []
post_format: []
---
Serverless development just got easier — today’s release of [Cloud Firestore](https://firebase.google.com/products/firestore/) with event triggers for [Cloud Functions](https://firebase.google.com/products/functions/) combine to offer significant developer velocity from idea to production to scale.

I’ve worked on dozens of mobile and web apps and have always been dismayed by the amount of boilerplate code needed to shuffle data between client and server and implement small amounts of logic on the server-side. Serverless APIs + serverless compute reduce the amount of code needed to write an app, increasing velocity throughout the development cycle. Less code means fewer bugs.

Cloud Firestore + Cloud Functions with direct-from-mobile access enabled by Firebase Auth and Firebase Rules combine to deliver something very new in this space. Unhosted Web apps are also enabled by Web SDKs.

It is not a coincidence that I’ve worked on all of these technologies since joining Google last year. My first coding project at Google was developing the initial version of the Firestore UI in the Firebase Console. I then stepped into an engineering management role, leading the engineering teams that work on server-side code where Firebase enables access to Google Cloud.

### Cloud Firestore

- **Realtime sync across Web and mobile clients**: This is not just about realtime apps. Building user interfaces is substantially easier: using reactive patterns and progressively filling in details allows apps to be ready for user interaction faster.
- **Scales with the size of the result set**: Simple apps are simple. For complex apps, you still need to be thoughtful about modeling your data, and the reward is that anything that works for you and your co-workers will scale to everyone on the planet using your app. From my perspective, this is the most significant and exciting property of the Cloud Firestore.
- **iOS, Android and Web SDKs**

### Cloud Functions

- **Events** for create, write, update, and delete ([learn how](https://firebase.google.com/docs/firestore/extend-with-functions))
- Write and deploy JavaScript functions that do exactly and only what you need
- You can also use [TypeScript](https://github.com/firebase/functions-samples/tree/master/typescript-getting-started) (JS SDKs include typings)

### All the Firebase things

- **Free tier** and when you exceed that, you only pay for what you use.
- **Zero to planet scale**: no sharding your database, no calculating how many servers you need, focus on how your app works.
- **Secure data access with Firebase Rules**: simple, yet powerful declarative syntax to specify what data can be accessed by client code. For example, some data may be read-only access for social sharing or public parts of an app, user data might be only written by that user, and some other data may be only written by server-code.
- **Firebase Auth**: all the social logins, email/password, phone or you can write code for custom auth
- **Lots more** [Firebase](https://firebase.google.com/products/) things

All this combines to allow developers to focus on building an app, writing new code that offers unique value. It’s been a while since I’ve been actually excited about new technology that has immediate and practical use cases. I’m so excited to be able to use this tech in the open for my side projects, and can’t wait to see the serious new apps…..