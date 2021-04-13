---
title: 'tesseract html page with text overlay'
date: '2013-07-13T16:52:45-07:00'
status: publish
permalink: /2013/07/tesseract-html-page-with-text-overlay
author: sarah
excerpt: ''
type: post
id: 4050
category:
    - code
tag: []
post_format: []
---
I’m learning a bit about OCR, and wanted to get some hands on experience using the open source Tesseract to get a feel for how it works. I’m a long way from any reasonable visual or interaction design, but the result of today’s exploration is an html page where the original image is overlaid with machine generated text in roughly the right location. This page looks like crap, but it’s a neat first step (click on the image below to see the full html page):

[![](http://monosnap.com/image/gvFJZ4174Y8MQbqWvcewB3BVl.png)  ](http://ultrasaurus.github.io/hocr-javascript/letter.html)

Tesseract
---------

[Tesseract](https://code.google.com/p/tesseract-ocr/) is an open source OCR tool (Apache 2.0 license) that produces fairly accurate output (relative to its open source peers) for scanned, type-written documents in English and many other languages.

On the Mac, we can easily install it with homebrew:

```

brew install tesseract
```

The latest version supports lots of different input image types, via [Leptonica](https://code.google.com/p/leptonica/), an open source C library for efficient image processing and image analysis operations.

If you just want to get text from an image, check the [ReadMe file](https://code.google.com/p/tesseract-ocr/wiki/ReadMe). I wanted to display the generated text over the image, which Tesseract supports via the [HOCR format](https://docs.google.com/document/d/1QQnIQtvdAC_8n92-LhwPcjtAUFwBlzE8EWnKAxlgVf0/preview).

Each word, line, and block of text, is annotated with an HTML tag. I look at just the word element, which is generated as a span tag with the attribute title:

```

<span class="ocrx_word" id="word_14" title="bbox 398 506 471 527" >WHOM</span>
```

I wrote a little javascript to create a style tag from the bbox attribute:

```

Manuscript.bboxToStyle = function(bbox_str) {
  arr = bbox_str.split(" ");
  left_pos = "left:"+arr[1]+"px; ";
  top_pos = "top:"+arr[2]+"px; ";
  right_pos = "right:"+arr[3]+"px; ";
  bottom_pos = "bottom:"+arr[4]+"px; ";
  return left_pos + top_pos + right_pos + bottom_pos;
};
```

Then used jQuery to apply that to every word element:

```

$(document).ready(function() {
    $(".ocrx_word").attr('style', function() {
        return Manuscript.bboxToStyle(this.title);
        });
});
```

Resulting in word elements that are positioned roughly where they appear in the image:

```

<span class="ocrx_word" id="word_14" title="bbox 398 506 471 527" 
style="left:398px; top:506px; right:471px; bottom:527px; ">WHOM</span>
```

I tried to experiment with the background-color of the words, but that’s not working for some reason. [Complete source on GitHub.](https://github.com/ultrasaurus/hocr-javascript)

Would love to hear about anyone else creating HTML UI for OCR results, either with Tesseract or other open source tools.