---
title: 'rcov and rails'
date: '2009-09-13T14:54:00-07:00'
status: draft
id: 2078
category: general
---
sudo gem uninstall rcov  
sudo gem install relevance-rcov

./script/plugin install http://github.com/ultrasaurus/rcov\_plugin.git

with removed invalid option: –no-validator-links

./script/plugin install git://github.com/commondream/rcov\_plugin.git

rake test:coverage