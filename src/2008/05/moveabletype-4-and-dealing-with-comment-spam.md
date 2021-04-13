---
title: 'moveabletype 4 and dealing with comment spam'
date: '2008-05-04T18:25:47-07:00'
status: publish
permalink: /2008/05/moveabletype-4-and-dealing-with-comment-spam
author: sarah
excerpt: ''
type: post
id: 370
category:
    - Uncategorized
tag: []
post_format: []
---
I’ve been letting comments build up in my moderation queue, since I have been overwhelmed by the amount of spam. Today, I decided to upgrade to mt4 to see if the new version offered anything better. I got a 500 error at first, but found in my apache logs:

error: “file is writable by others”  
Found via google that I needed to: chmod 755  
I usually just a+x, but that seemed to work.

Other than that, MovableType was a delight to install, as always.

Eek! All of the comments I had marked as junk were simply unpublished after the upgrade. I couldn’t deal with 45,000 comments via the GUI, so I decided to walk on the edge and edit directly via SQL… I had just backed up my database, right?

So… for the record, this is what worked:  
mysql&gt; DELETE FROM mt\_comment WHERE comment\_visible IS NULL;  
Query OK, 45176 rows affected (7.54 sec)

Then, I decide to go after my trackback spam:  
mysql&gt; DELETE FROM mt\_tbping WHERE tbping\_blog\_name LIKE “%Jhony%”;  
Query OK, 46535 rows affected (5.31 sec)

mysql&gt; DELETE FROM mt\_tbping WHERE tbping\_blog\_name LIKE “%sex%”;  
Query OK, 37 rows affected (0.03 sec)

mysql&gt; DELETE FROM mt\_tbping WHERE tbping\_blog\_name LIKE “%loans%”;  
Query OK, 171 rows affected (0.04 sec)

finally, I decided my time was more important than finding the elusive valid trackback, so I deleted them all:

mysql&gt; DELETE FROM mt\_tbping;

Ok, all is good, or so I thought. I’ve got my old blog with the new MT. However, I wanted to try out authentication for comments, but when I turn it on, I get an error when I post a new comment that registration is required. I suppose I need to update my “Entry” template, so I look up the MT4 [default templates](http://www.movabletype.org/documentation/designer/movable-type-40-default-templa.html). However, if I paste in the [entry template](http://www.movabletype.org/default_templates/4.0/entry.mtml), I get an error. Sigh.