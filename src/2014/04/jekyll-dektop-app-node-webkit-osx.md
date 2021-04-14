---
title: 'jekyll dektop app with node-webkit on osx'
date: '2014-04-26T08:24:30-07:00'
status: publish
exported_permalink: /2014/04/jekyll-dektop-app-node-webkit-osx
author: sarah
excerpt: ''
type: post
id: 5087
category:
    - code
tag: []
post_format: []
---
I had an idea this morning that I could make a simple desktop app by combining the lightning-fast website generation capabilities of [jekyll](http://jekyllrb.com/) with the awesome [Node-Webkit](https://github.com/rogerwang/node-webkit) that lets us native wrappers for HTML5 apps. I checked out this [nice intro to Node-Webkit](https://speakerdeck.com/zcbenz/node-webkit-app-runtime-based-on-chromium-and-node-dot-js), and unsurprisingly ran into a few gotchas, documented below for other adventurer and my future self:

Simple Website with Jekyll
--------------------------

```

gem install jekyll
jekyll new experiment
cd experiment
jekyll serve
```

go to <http://localhost:4000>  
you should see the default sample jekyll site

Make a Native OSX App
---------------------

Download and install [Node-Webkit pre-built binary](https://github.com/rogerwang/node-webkit)

At the root of your jekyll site, create a file named “package.json”

```

{
  "name" : "nwk-experiment",
  "window" : {
    "width" : 800,
    "height" : 600,
    "toolbar" : true
  },
  "main" : "app://whatever/index.html"
}
```

The [app root url](https://github.com/rogerwang/node-webkit/wiki/App%20protocol) is a nice feature of node-webkit which makes it pretty easy to transport any website into this system of building a native app.

```

jekyll build  # creates the site
cd _site
zip -r ../app.nw * 
cd ..
```

Most tutorials tell you to zip the directory. The first time I tried, I got an Invalid package error “There is no ‘package.json’ in the package, please make sure the ‘package.json’ is in the root of the package.” On OSX, we need to zip the files from the root of the directory that had the ‘package.json file in it. (via [crashtheuniverse](https://github.com/rogerwang/node-webkit/issues/388))

Run the App
-----------

```

open -n -a node-webkit "./app.nw"
```

When I double-click on the app.nw file, I see the directory, not my index file. I haven’t figured out that part yet. Still a work in progress!