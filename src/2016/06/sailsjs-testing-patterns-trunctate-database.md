---
title: 'sailsjs testing: how to truncate the database'
date: '2016-06-11T19:10:00-07:00'
status: publish
exported_permalink: /2016/06/sailsjs-testing-patterns-trunctate-database
author: sarah
excerpt: ''
type: post
id: 5990
category:
    - code
tag: []
post_format: []
---
SailsJS is a NodeJS MVC framework that we use for the [OpenOpps Platform](https://github.com/openopps/openopps-platform). Sails has some basic [testing docs](http://sailsjs.org/documentation/concepts/testing), but it doesn’t explain how to set up the framework nicely where the database is dropped in between tests. I find myself always re-figuring out these patterns when I write experimental apps.

With an in-memory database, this bootstrap.test.js will drop the database between tests:

```

var sails = require('sails');

before(function(done) {
  sails.lift({
    // test config
    environment: 'test',
    port: 9999,   // so we can run the app and tests at the same time
    hostName: 'localhost:9999',
    connections: {
      testDB: {
        adapter: 'sails-memory'
      }
    },
    models: {
      connection: 'testDB'
    },
  }, function(err, server) {
    if (err) return done(err);
    done(err, sails);
  });
});

after(function(done) {
  sails.lower(done);
});

beforeEach(function(done) {
  // Drops database between each test.  This works because we use
  // the memory database
  sails.once('hook:orm:reloaded', done);
  sails.emit('hook:orm:reload');
});
```

When I need to use postgres, Waterline doesn’t expose SQL truncate which would be much faster, instead this bootstrap.test.js will destroy all the models:

```

var async = require('async');
var sails = require('sails');

before(function(done) {
  sails.lift({
    // test config
    environment: 'test',
    port: 9999,   // so we can run the app and tests at the same time
    hostName: 'localhost:9999',
    models: {
      connection: 'postgresql'
    },
  }, function(err, server) {
    if (err) return done(err);
    done(err, sails);
  });
});

afterEach(function(done) {
  destroyFuncs = [];
  for (modelName in sails.models) {
    destroyFuncs.push(function(callback) {
      sails.models[modelName].destroy({})
      .exec(function(err) {
        callback(null, err)
      });
    })
  }
  async.parallel(destroyFuncs, function(err, results) {
    done(err);
  })
});

after(function(done) {
  sails.lower(done);
})

```