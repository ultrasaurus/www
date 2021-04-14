---
title: 'Laszlo app development'
date: '2003-08-04T19:02:51-07:00'
status: publish
exported_permalink: /2003/08/laszlo-app-development
author: sarah
excerpt: ''
type: post
id: 39
category:
    - Uncategorized
tag: []
post_format: []
---
I recently spent some time with LZX developing a prototype app. I thought it would be interesting to write up how we approached the problem and show some of the results that are now posted on [mylaszlo.com](http://www.mylaszlo.com).  
![](http://www.mylaszlo.com/lps-v1/pablo/store/lz_screenshot.jpg)

The problem:  
– create an e-commerce app  
– 1 week (4 days days for me)  
– 3 people

It was natural to consider developing yet another Pet Store, but we were bored with that concept and perhaps other folks are too. We created a store, but chose to sell three varieties of pots: tea pots, garden pots and cooking pots.

The [Pot Store](http://www.mylaszlo.com/lps-v1/pablo/store/store.lzx) is a work-in-progress. It needs some attention to the design to clarify navigation. The graphical elements are pimitive and it is not a fully functioning store. However, it was a great learning experience and employs some interesting user interface ideas.

\* The subtotal updates as you buy, with a small motion to draw the user’s attention. You can see a summary of what’s in your shopping cart with rollover, without losing the context of the catalog view.

\* The catalog layout is an example of a continuous user experience. You can get product details without losing context. (I consider it a bug that sometimes teapots fly across the screen. They should all move smoothly out of the way to a nearby spot.)

\* Shipping/billing Address in the checkout section conserves real-estate and minimizes screen (and brain) clutter by only showing the fields that you need. (click “ship to a different address” checkbox)

I’ve written up some details on my experience of the development process….

  
Day 1: Plan the project  
We created an [interactive spec](http://www.mylaszlo.com/lps-v1/pablo/store/mockup.lzx) in LZX. There are 3 main sections.  
Catalog (you can click to cycle thru 3 pictures in the mockup)  
– feature product view, one from each category  
– broswe one category  
– product details  
Shopping Cart  
– subtotal displayed when cart is closed, pop-up summary on rollover  
– cart would allow you to change quantity, delete items  
Checkout  
– fill out name &amp; paymeny info  
– ship to different address (checkbox works in mockup)

We split the project into three parts. I would develop a layout for the catalog view; Pablo would create the shopping cart; and Yossie would create a simple database and the checkout process.

Day 2:  
We agreed on what queries we wanted from the database. Yossie created a simple MySQL database and some perl scripts that made the appropriate queries. I found 15 teapot pictures and descriptions. Pablo added the cool rollover subtotal feature to the spec. We each started on our parts.

I had never written a layout before, so I read the docs and looked at the code for simple layout and wrapping layout. I created some simple test files.

Day 3: [layout motion test ](http://www.mylaszlo.com/lps-v1/pablo/store/layout/testlayout.lzx)  
I modified wrappinglayout to create my new layout, which would show the grid of teapot images. When the user clicked on a teapot, details would be displayed. The transition between views was a zoom, where te other images would shrink to make room. This was much easier than I expected and fun to write.

Day 4:  
After the layout was working with colored squares, I integrated the image data from the server. Next I needed to integrate the catalog layout into the store app. Pablo had done a nice job of creating a “basket” object, so I could easily call “basket.addItem” to hook up the “buy” button in the catalog view.

Summary:  
Pablo &amp; Yossie worked on the app for a few more days. Overall I felt we accomplished a lot in a week, especially given that Yossie and Pablo were learning LZX during the development process. It’s a bit scary to post something so raw and unfinished, but we hope that in doing so other folks can learn from our process.

As part of the development team for the [Laszlo Presentation Server](http://www.laszlosystems.com), I believe it is essential that we experiment with using our software as web app developers. In creating a platform for rich internet applications, we need to develop not only the architectural design patterns of how to hook up data and views, client and server, ui to back-end logic, but also the visual and interactive design patterns that could led to a more usable web.

Feedback and questions are welcome, as always.