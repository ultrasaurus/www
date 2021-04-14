---
title: 'getting started with drupal'
date: '2013-07-27T02:38:56-07:00'
status: publish
exported_permalink: /2013/07/getting-started-with-drupal
author: sarah
excerpt: ''
type: post
id: 4159
category:
    - code
tag: []
post_format: []
---
Emeline Glynn and Anthony Glynn gave a helpful talk called “[How to teach anyone Drupal in 7 months](http://capitalcamp.org/content/how-teach-anyone-drupal-development-7-months).” The timeline was based on their experience where Anthony, an experience Drupal developer, taught Emeline remotely over a period of 7 months, to the point that she is now working professionally as a Drupal developer. [Slides posted here.](http://anthony-glynn.com/drupal-7-months/)

Emeline notes that you need a passionate &amp; dedicated student. It can be very frustrating, especially as someone new to development, especially learning command line tools, git and debugging, but she was excited about it and found it very rewarding even when she was very new. She usually spent 4-6 hours a day. Anthony noted that if someone has experience with another framework, you can expect the timeline to be 2-3x faster.

I liked this breakdown of stages in learning:

1. Learn the Language
2. Get the Skills
3. Cross the Chasm
4. Leave Footprints

For me, as a developer with 20+ years of experience, I pick this stuff up fairly quickly. I spent a few solid days on getting my dev env setup, understanding the major components and making small changes to a module. As important as the code, is understanding its patterns and jargon. The immersive experience of [CapitalCamp](http://capitalcamp.org/) with its enthusiastic community and these references to key learning resources has significantly accelerated the learning curve.

This learning path focuses on the non-programmer; however, Anthony suggested (and I agree) that the experienced developer would take a similar path.

1. Register at [drupal.org](https://drupal.org/)  
  [ drupal.org/planet](https://drupal.org/planet) should be your home page, with news feeds of all the best blogs online
2. [drupal.org/security](https://drupal.org/security) – the Drupal security team meets once a week and issues security advisories less frequently — they also have a mailing list.
3. Meetups — Anthony learned by reading [Pro Drupal Development](http://www.amazon.com/Pro-Drupal-Development-John-VanDyk/dp/1590597559) &amp; going to meetups. (He noted that the community is a bit less friendly on line.) Meetups provide inspiration and the landscape of what to learn.
4. Setup your dev env  
  Recommended: Linux, git, Drush, PhPMyAdmin, Firebug or Chrome Developer Tools  
  (Linux much easier than Windows)  
  On Mac OSX it is pretty easy too, but finding good setup instructions was hard. I [posted the steps I the I use](https://www.ultrasaurus.com/sarahblog/2013/07/easy-drupal-install-on-mac-osx-lion/) and have since added apache vhost config so I can run multiple drupal sites easily.
5. Embrace the command line! students may be freaked out at first, but it makes you very productive. If the student is non-technical, there are a lot of skills that are not Drupal that you still need to learn (e.g. command line, git)

Consider starting with a distribution profile

- Drupal Commons: if you want to manage communities
- Drupal Commerce: e-commerce
- OpenPublic: government site

Terms &amp; Landmarks

- API [api.drupal.org](https://api.drupal.org/api/drupal)
- node: a piece of content
- module: a Drupal extension written in PHP

Helpful modules

- [administration menu](https://drupal.org/project/admin_menu): allows you to hover on Drupal menu items and shows submenus (drill down)
- [coffee](https://drupal.org/project/coffee): type in the page you want to go to and link pops up (also for the admin UI)
- [module filter](https://drupal.org/project/module_filter): allows your module page to look clearer
- [devel](https://drupal.org/project/devel): key helper module, allows you to access those variables,
- [develthemer](https://drupal.org/project/devel_themer) – helps you develop themes
- [views](https://drupal.org/project/views) – pretty much on every site
- [features](https://drupal.org/project/context) – export your config (config + content is in the database)
- panels &amp; context: each puts you don’t a certain path
- [context](https://drupal.org/project/context) – if you are in this part of the site, show this
- [panels](https://drupal.org/project/panels) – let you pick

Learn about themes – Omega, Adaptive theme and something else. Also, subthemes.

Build

- [BuildAModule](http://buildamodule.com/), [drupalize.me](http://drupalize.me/) – subscription video sites – both are good
- [nodeone library ](http://nodeone.se/sv/learn-drupal)– good for UI stuff
- also there are videos on YouTube YMMV, but some are quite good

Debugging tips

- “Calm down and clear the cache”
- become fmiliar with the apache logs and drupal watchdog logs

Make students feel adventurous! Db backup + git makes it safe

More tips

- [codecademy](http://www.codecademy.com/tracks/php) – good for PHP
- make sure you understand the hook system
- look &amp; use other people’s code
- write patches
- write your own blog
- PHP function: debug\_backtrace

litmus test / goal is to write your own modules