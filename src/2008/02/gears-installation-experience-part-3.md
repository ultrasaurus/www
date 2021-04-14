---
title: 'gears installation experience (part 3)'
date: '2008-02-24T16:08:14-08:00'
status: publish
exported_permalink: /2008/02/gears-installation-experience-part-3
author: sarah
excerpt: ''
type: post
id: 360
category:
    - Uncategorized
tag: []
post_format: []
---
As it turns out, the typical install avoids popup blocker issues and does return you to your site. With the latest version, you can even append name and icon\_src params to include more context about the web application you are coming from.

The generic install with the custom icon and name looks like this (not a real web application, just some placeholder text and image):

<div id="__ss_280317" style="width:425px;text-align:left"><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px">[![SlideShare](http://static.slideshare.net/swf/logo_embd.png)](http://www.slideshare.net/?src=embed) | [View](http://www.slideshare.net/sarah.allen/generic-gears-install-with-custom-icon?src=embed "View 'Generic Gears Install with Custom Icon' on SlideShare") | [Upload your own](http://www.slideshare.net/upload?src=embed)</div></div>The actual page is [here](https://www.ultrasaurus.com/gears/install/), if you want to check it out yourself, just view source. The code with the extra branding params looks like this:

```

location.href = "http://gears.google.com/?action=install&message=Please install Google Gears to enable offline access to my imaginary ultrasaurus application." +
"&return=" + location.href +
"&name=Ultrasaurus&icon_src=https://www.ultrasaurus.com/dino.gif";
```

While I think the icon and name is a nice addition, the prominence of Google branding vs. the website using Gears seems like it should be inverted. PayPal does a good job of this. When you buy something from a site using PayPal, you end up on the PayPal site for some part of the transaction. However, the website branding is in the top header with the PayPal branding inside the content. For example, here’s a purchase page from ThinkGeek using PayPal:

[![](http://farm3.static.flickr.com/2196/2289968508_fee36de0ed_m.jpg)](http://farm3.static.flickr.com/2196/2289968508_07a7c1a353_o.png)

Of course, what I really want to do is not direct the person using my app to whole different webpage, but just prompt for the download within my site. Maybe someday if they get the whole install working from an ActiveX control, it’ll be more seamless.

Also, I sure hope they do away with that license agreement when they get out of beta. The use of Gears does not imply an account with Google and the people using my software shouldn’t have to worry about the Google privacy policy or service commitments. As a developer, I’m happy to agree to such terms, but I’d rather not give people one more reason to click away from my website.