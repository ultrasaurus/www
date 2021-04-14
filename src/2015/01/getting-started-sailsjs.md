---
title: 'getting started with sailsjs'
date: '2015-01-11T11:24:11-08:00'
status: publish
exported_permalink: /2015/01/getting-started-sailsjs
author: sarah
excerpt: ''
type: post
id: 5442
category:
    - code
tag: []
post_format: []
---
[Sails.js](http://sailsjs.org/) is a [Node.js](http://nodejs.org/) MVC framework. Rails developers will find the components quite similar, but I think Sails has done a really good job of leveraging libraries and frameworks that it integrates. In addition to Node, it sits on top of [Express](http://expressjs.com/), which handles HTTP requests. In fact every request object, is simply an Express request. Sails also nicely integrates [socket.io](http://socket.io/).

Install on OSX
--------------

```

brew install node
npm install sails -g
sails -v
```

 Make a Project 
----------------

```

sails new testProject
cd testProject
sails lift
```

In your browser, go to: <http://localhost:1337/> and there are some pointers to the docs and hints about what to do next.

 Make a REST API 
-----------------

```

sails generate api user
sails lift
```

Now in the browser <http://localhost:1337/user> returns a JSON representation of our list of users, which is an empty array at this point.

By default, your project is configured with a dynamic schema using the default disk databas, which lets us experiment by creating models using the browser:

- <http://localhost:1337/user/create?name=Tim>
- <http://localhost:1337/user/create?name=Judy>
- <http://localhost:1337/user/create?name=Lee>
- <http://localhost:1337/user/create?name=Maggie>

The default routes are configured in config/blueprints.js, so you can turnoff these “shortcut” routes if you want to only have the more standard REST-ful syntax generated for your APIs. If you are fond of it from Rails, you can also tell Sails to pluralize names in the same config file.

Now if you go to: <http://localhost:1337/user>

You can see your users:

```

[
  {
    "name": "Tim",
    "createdAt": "2014-12-21T18:20:19.382Z",
    "updatedAt": "2014-12-21T18:20:19.382Z",
    "id": 1
  },
  {
    "name": "Judy",
    "createdAt": "2014-12-21T18:20:26.269Z",
    "updatedAt": "2014-12-21T18:20:26.269Z",
    "id": 2
  },
  {
    "name": "Lee",
    "createdAt": "2014-12-21T18:20:29.338Z",
    "updatedAt": "2014-12-21T18:20:29.338Z",
    "id": 3
  },
  {
    "name": "Maggie",
    "createdAt": "2014-12-21T18:20:32.879Z",
    "updatedAt": "2014-12-21T18:20:32.879Z",
    "id": 4
  }
]
```

Check Out Sockets
-----------------

Open Javascript console in your browser, and you should see:

```

    |>
  \___/
sails.io.js:200  `io.socket` connected successfully.
```

Try this at the console to see the list of users:

```

io.socket.get('/user', {}, function (users) {console.log(users)})
```

To listen for changes to any user model:

```

  io.socket.on('user', function messageReceived(event) {
    console.log('New comet message received :: ', event);
  });
```

Open another browser window, and create a user:

```

http://localhost:1337/user/create?name=Eva
```

then you’ll see the notification in your first browser window

```

New comet message received ::
Object {model: "user", verb: "create", data: Object, id: 5}
```

The documentation is pretty good, but a lot of has changed for the recent 0.10 update, and their intro video is a couple of revisions behind. To get up to speed on the changes in the new release, I updated what that intro would be in the new syntax on [github ultrasaurus/sails-new](https://github.com/ultrasaurus/sails-new), which includes the above tutorial and a few other details.