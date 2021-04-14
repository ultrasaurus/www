---
title: 'easy drupal install on mac osx lion'
date: '2013-07-08T13:18:20-07:00'
status: publish
exported_permalink: /2013/07/easy-drupal-install-on-mac-osx-lion
author: sarah
excerpt: ''
type: post
id: 4000
category:
    - code
tag: []
post_format: []
---
Lion comes with Apache and PHP installed. We just need to enable PHP, install MySql and create a database, then download drupal.

Enable PHP
----------

My new laptop which came with Lion has PHP 5.3.15, using the test page we’ll build below you can verify you’ve got a [good version of PHP](https://drupal.org/requirements) to go with the Drupal you need:

- Drupal 6: PHP 4.4.0 or higher (5.2 recommended).
- Drupal 7: PHP 5.2.5 or higher (5.3 recommended).
- Drupal 8: PHP 5.3.10 or higher.

 Commands below use vi (of course, you should use your editor of choice). (thank you [stackoverflow](http://stackoverflow.com/questions/6790568/how-do-you-get-php-working-on-mac-os-x-lion-10-7))

You’ll need `sudo` to edit the Apache config file:

```
 
sudo vi /etc/apache2/httpd.conf
```

uncomment the following line:

```

LoadModule php5_module libexec/apache2/libphp5.so
```

On the following line change `_www` to the username you log in with:

```

User _www
```

By default, Apache only loads index.html, so update that line to:

```

DirectoryIndex index.html index.php index.htm
```

Restart apache on the command line

```

sudo apachectl restart
```

Now, let’s make a test file:

```

cd ~/Sites
mkdir php-test
cd php-test/
vi index.php
```

Then paste in this [test file](https://gist.github.com/ultrasaurus/5943921) and browse to `http://localhost/~yourusername/php-test/`

Install MySql
-------------

I like to install everything with [homebrew](http://mxcl.github.io/homebrew/) which is my favorite package manager for osx. It keeps everything in `/usr/local/` by default, and then I don’t have to remember where GUI installers put everything.

```
 
brew install mysql
```

I like to have MySql always start up, so I use a Launch Agent, which homebrew describes how to do after the install:

```

To have launchd start mysql at login:
    ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
Then to load mysql now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
Or, if you don't want/need launchctl, you can just run:
    mysql.server start
```

Now make a database:

```

mysqladmin -uroot create drupal_dev
```

The default way this is set up is for a dev environment, so there’s no password and root has full access. You can see this in the mysql console:

```

mysql -uroot
show databases;
show grants;
```

Now we need to fix the PHP configuration to refer to mysql correctly so we don’t get PDO errors (thanks [Hiraash](http://blog.hiraash.org/2012/09/17/pdo-for-the-default-installation-of-php-on-mac-osx/)):

```

sudo cp /etc/php.ini.default /etc/php.ini
vi /etc/php.ini
```

replace all instances of `/var/mysql/mysql.sock` with `/tmp/mysql.sock`  
and restart apache

```

sudo apachectl restart
```

Download Drupal
---------------

I followed the [drupal.org instructions](https://drupal.org/documentation/install/download), but you need to go find the [right version](https://drupal.org/project/Drupal). As of this writing, 7.22 is the recommended v7 release, which is what I’ll be working with.

```

cd ~/Sites
wget http://ftp.drupal.org/files/projects/drupal-7.22.tar.gz
tar -xzvf drupal-7.22.tar.gz
rm drupal-7.22.tar.gz
```

Now, I’ll just rename it to be the same name as the database we set up:

```

mv drupal-7.22 drupal_dev
```

browse to `http://localhost/~yourusername/drupal-dev` and proceed with the install wizard

![](http://monosnap.com/image/ocxB8VYvpm1SC0HafuKPcSXfp.png)

step through the wizard and drupal sets itself up.