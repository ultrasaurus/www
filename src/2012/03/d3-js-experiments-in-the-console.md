---
title: 'd3.js experiments in the console'
date: '2012-03-30T12:39:44-07:00'
status: publish
exported_permalink: /2012/03/d3-js-experiments-in-the-console
author: sarah
excerpt: ''
type: post
id: 3573
category:
    - code
tag: []
post_format: []
---
d3 (aka Data-Driven Documents) is a great little JavaScript framework for data visualization. It’s got a nice declarative syntax for DOM manipulation that’s quite readable, but takes a bit of effort to understand exactly what it’s doing.

Favorite links:

- UPDATE: [Dashing D3.js](http://www.dashingd3js.com/) is an amazing series of tutorials with great conceptual grounding
- [d3 tutorials](http://mbostock.github.com/d3/api/) provide a great conceptual foundation
- [Thinking with Joins](http://bost.ocks.org/mike/join/) by d3 creator, Mike Bostick, helps explain the syntax for chaining methods
- [Scott Murray’s d3 tutorial](http://alignedleft.com/tutorials/d3/) offers a very nice step-by-step, covering a lot of the same ground as my little tutorial below with excellent discussions of the fundamentals.

I like to understand stuff by playing with it interactively, so I created a skeleton index.html which just includes d3.js and a style a div where I’ll display some data.

UPDATE: blank file below posted [here](http://ultrasaurus.github.com/d3js-examples/simple-div.html)

```

<html><br></br>  <head><br></br>    <title>d3 experiment</title><br></br>    <script type="text/javascript"<br></br>            src="https://raw.github.com/mbostock/d3/master/d3.js"><br></br>    </script><br></br>    <style type="text/css"><br></br>      .box {<br></br>        background-color: skyblue;<br></br>        width: 24px;<br></br>        height: 18px;<br></br>        padding: 4px;<br></br>        margin: 1px;<br></br>      }<br></br>    </style><br></br>  </head><br></br>  <body><br></br>  </body><br></br></html><br></br><br></br><br></br><br></br>
```

Then in the FireBug console, we can interact with d3, the top-level object that allows us to access all of d3’s goodness.

```

>>> d3
Object { version="3.0.1", random={...}, ns={...}, more...}
>>>  body = d3.select("body")
[[body]]
```

Like jQuery, d3 let’s us “select” one or more DOM elements to operate on them. I only have one body tag, so I just get one element in an array — not yet sure why it needs a nested array. Now I can manipulate the DOM:

```

>>>  body.append('p').text('Hello d3!')
[[p]]
```

and “Hello d3!” appears at the top of my page. Yay! Of course that could have been written in a single line like:

```

d3.select("body").append('p').text('Hello d3!')
```

and if I want to change the text, I can use a regular old css selector to grab the paragraph element I just created:

```

d3.select("body p").text("Welcome to d3")
```

or, using the reference to the ‘body’ variable I created above:

```

body.select("p").text("d3 is cool")
```

Data-driven Boxes
-----------------

Ok, now that we understand the basics, let’s put some boxes on the page:

```

body.append('div').attr('class','box')
```

and let’s add a couple with text in them:

```
 
body.append('div').attr('class','box').text('hi')
body.append('div').attr('class','box').text('foo')
```

With my set of boxes, I can select one or all of them:

```

>>> d3.select('.box')
[[div.box]]
>>> d3.selectAll('.box')
[[div.box, div.box, div.box]]
```

Then I can specify data to *bind* to each box and display it. I’ve read that d3 can deal with all sorts of data (like json, csv, etc.) but we’ll start with an array of numbers.

```

>>> my_data = [20, 7, 32]
[20, 7, 32]
>>> d3.selectAll('.box').data(my_data).text( function(d) { return d } )
[[div.box, div.box, div.box]]
```

![](https://img.skitch.com/20120330-jb12cx9qa7p16diptgy6kqjq6c.png)  
![](https://img.skitch.com/20120330-qhkt419gnaqh2d9f5s53xns6nh.png)

We can see that our data is associated with the DOM element and we can get at it via JavaScript in the console. (Of course, we should only do that for debugging. I would guess that \_\_data\_\_ is the private implementation of d3’s data binding.)

```

>>> d3.select('.box')[0][0].__data__
20
```

We can change the data like this:

```

>>> new_data = [10, 50, 25]
[10, 50, 25]
>>> d3.selectAll('.box').data(new_data)
```

You’ll see that the page doesn’t change visually, but in the console, you can see that the data does:  
![](https://img.skitch.com/20120330-kwnsfr1kiuaskauqeruib7in3d.png)

We need to explicitly tell d3 to do something with the data like this:

```

d3.selectAll('.box').text( function(d) { return d } )
```

We can also use this handy shortcut:

```

d3.selectAll('.box').text( String )
```

</body></html>