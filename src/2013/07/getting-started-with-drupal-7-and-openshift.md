---
title: 'getting started with drupal 7 and openshift'
date: '2013-07-04T10:07:03-07:00'
status: publish
permalink: /2013/07/getting-started-with-drupal-7-and-openshift
author: sarah
excerpt: ''
type: post
id: 3942
category:
    - code
tag: []
post_format: []
---
When learning a new web technology, I believe it is important to have hands-on experience from development to deployment. I chose [Open Shift](https://openshift.redhat.com), one of the [recommended cloud deployment options for Drupal 7](https://drupal.org/node/1860868). It’s free for 3 small instances, which seems perfect for experimentation.

I used the very simple web UI to create a Drupal 7 instance:  
[![](http://monosnap.com/image/I2Mf4bHlPrhNUWMKcnaudyjiU.png)](http://monosnap.com/image/I2Mf4bHlPrhNUWMKcnaudyjiU.png)  
Note: Just like Heroku, you can’t write to the file system with open shift, so by default the Drupal install is “not scalable.” However, there’s documentation about how to configure it so that it would be scalable if you don’t need file upload — not sure why they wouldn’t just do that by default.

[![](http://monosnap.com/image/eE7LvM8oTHb7D2N4Oqnazw7kt.png)](http://monosnap.com/image/eE7LvM8oTHb7D2N4Oqnazw7kt.png)

Next there’s a screen that provide credentials for the app, and a link to my new instance:  
[![](http://monosnap.com/image/0ceVNMU9XgdB0YJNrbzXamOuE.png)](http://monosnap.com/image/0ceVNMU9XgdB0YJNrbzXamOuE.png)

Woo hoo! I can log in with the default credentials (admin / openshift\_changeme ) and see the default Drupal admin UI:  
[![](http://monosnap.com/image/aqSYRkRIr3KHbTJYgH7gyrQ0S.png)](http://monosnap.com/image/aqSYRkRIr3KHbTJYgH7gyrQ0S.png)

If you go to “People,” you can find your admin user and change the password. Of course, I’ve done this on my instance, so you can’t log in — you should go make your own!

Dev Setup?
----------

I already had an account that I had experimented with for Ruby, but it was some time ago, so I needed to [reinstall the local tools and setup](https://www.openshift.com/developers/rhc-client-tools-install):

1\. requires git and ruby (since its “rhc” tool is a gem) — I’m using rvm with ruby 1.9.2  
2\. to setup client tools, as well as ssh key and a token locally for automagic auth:

```

rhc setup 
```

3\. clone the repo

```

git clone ssh://51d..183@drupal7-ultrasaurus.rhcloud.com/~/git/drupal7.git/ openshift-drupal7
cd openshift-drupal7 
```

Not clear what to do from here. The [OpenShift forums](https://www.openshift.com/forums/openshift/git-clone-repo-success-what-next#comment-32050) provides the hint that I can take a snapshot of files with

```
rhc snapshot save -a {appname}
```

 but that doesn’t hint at a dev workflow.

I do want to figure out a nice workflow to develop locally and deploy on a free cloud. I’ve played with Acquia Desktop. [MAMP](http://www.mamp.info/en/index.html) has been recommended. I’d be more comfortable with “brew install …”

I will post this for now, in case any of you readers can clue me in or point me to some good install docs. I’ll update this post once I figure out something I like. Thanks in advance.