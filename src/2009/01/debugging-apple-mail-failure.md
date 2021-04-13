---
title: 'debugging Apple Mail failure'
date: '2009-01-22T22:28:26-08:00'
status: publish
permalink: /2009/01/debugging-apple-mail-failure
author: sarah
excerpt: ''
type: post
id: 682
category:
    - general
tag: []
post_format: []
---
Just in case anyone was wondering how to tell what really happened when something goes wrong in Apple’s Mail application on Leopard (via [dslreports](http://www.dslreports.com/faq/14522))

1. Quit Mail
2. Open ” /Library/Scripts/Mail Scripts/Turn on Logging.scpt”
3. Click Run
4. It ask you if you want to turn on “secret logging” for Sending, Recieving or Both, then it will launch Mail
5. Do the problematic action
6. Open the Console and type: syslog -C

Interesting, but not helpful this time. Why don’t they log timeouts? Turns out the port was blocked by Comcast. Ugh. Thanks [Doug](http://www.blogarithms.com/index.php/archives/2008/01/17/blocked-by-comcast/).

Amazingly, the operator at Comcast who answered my live chat requesst was able to unblock my port. Here’s an excerpt of the conversation (slightly edited for brevity):

> **Gillema**: Were you able to change the port number on smtp from 25 to port number 587 now?  
> **Sarah**: Well, I would like to use 25. That is what my smtp server listens on  
> **Sarah**: I can use the comcast one with a username/password, but I won’t be able to use that when I’m not at home  
> **Gillema**: Sarah, you may not use tb25 for this is more open to any viruses that may harm on your computer.  
> **Sarah**: I don’t accept incoming connections on 25, so my computer is not vulnerable  
> **Sarah**: Do you have any evidence of infection?  
> **Sarah**: I run two macs and a Windows machine where the anti-virus is typically kept up to date by my work IT department  
> **Gillema**: I see. May I ask what third party email client are you using? Is it outlook express or outlook2003?  
> **Sarah**: Apple Mail on the Macs and Thunderbird on Windows (or web mail)  
> **Gillema**: I see. Thank you for the information.  
> **Gillema**: So, Sarah! In using the TB25, are you able to send a message on both of your third party email clients?  
> **Sarah**: sending…  
> **Sarah**: that worked, you unblocked it?  
> **Gillema**: Yes. So, Sarah, was I able to resolve your issue issue today? Will there be anything else I can help you today?  
> **Sarah**: Yes, issue resolved. Thank you very much

I was so shocked that Comcast was actually willing and able to resove my problem without a prolonged interaction with managerial escalataion that I exclaimed aloud to my family and a funny conversation ensued

> **Mommy**: I can’t believe it. Comcast actually opened the port.  
> **Son**: What’s a port?  
> **Daddy**: It’s a harbor or bay where ships can dock. And the Comcast navy was blocking our ships from getting out of the harbor.
> 
> **Son**: I know \*that\* but really, what’s a port?  
> **Mommy**: you know how a lot of computer words are named after real world things, like the mouse, the web…  
> **Son**: spiders?  
> *\[Intended as a joke, it of course led to a small digression on what a spider is — the computer program not the arachnid*\]
> 
> **Mommy**: a port is a place (not a physical place, but rather a number) that is part of the network connection so multiple programs can communicate on the same time. Like for example, port 80 is for the Web…  
> **Son**: why port 80? the Web is really important. It should be number 1. What’s number 1?  
> **Mommy**: We can look that up. There’s an organization called the [Internet Assigned Numbers Authority](http://www.iana.org/) which gives out numbers, we can look up the [list of ports](http://www.iana.org/assignments/port-numbers) … number 1 is for the TCP Port Service Multiplexer. I’m not sure what that is, but it’s not number 1 because it is most important but instead because it was invented first.
> 
> Son: They should renumber everything and make the Web number 1. *and there ensued a long conversation about how everything would break if we just rearranged all the numbers* **Son**: But number 8 isn’t being used. They could just chop off all the zeros and make the Web number 8. That’s what I think they should do.
> 
> Mommy: did you know Mommy had a number on this list? I wonder if it still assigned to me. Let’s see 1935… Pritham has it registered now. **Son**: why didn’t they let you keep it? **Mommy**: because it didn’t really belong to me. It belongs to the software…  
> *\[another digression about why the software needs it and I don’t. Of course, 1626 is still registered to me. I don’t know if anyone is still running the Shockave Multiuser Server, but the port is still there reserved just in case. Doesn’t it just make you sleep well at night knowing that there is someone out there keeping track of all the numbers and making sure that our netwrok protocols don’t collide?\]*

Geek Mom strikes again.