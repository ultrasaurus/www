---
title: 'markdown to textile with vim regex'
date: '2009-12-30T00:36:20-08:00'
status: publish
exported_permalink: /2009/12/markdown-to-textile-with-vim-regex
author: sarah
excerpt: ''
type: post
id: 2331
category:
    - code
tag: []
post_format: []
---
So, I needed to change markdown to textile and google didn’t yield any handy scripts, so I sharpened my vim fu with [Rubular](http://www.rubular.com/), my favorite regular expression tester and came up with a few substitutions that took care of everything but lists and code blocks.

In vi, type ESC to go into command mode, then :%s/one/two/g will find every instance of “one” and replace it with “two”

First the easy stuff, headers. ^ finds the beginning of the line.

```

:%s/^# /h1. /g
:%s/^## /h2. /g
:%s/^### /h3. /g
```

To replace images, I needed to replace !\[alt-text\](link) with !link! so I needed to capture text. I suppose I didn’t really need the first capture, but I was working on the replace expression for a regular link when I realized it would be easier to do the images first. To understand the expression below, you need to know that (stuff) captures some text which can be inserted in the replacement text with 1 and 2, etc. So to get everything between square brackets, I use \[(.\*)\]

```

:%s/![(.*)]((.*))/!2!/g
```

All of my images appeared on a single line, so I didn’t catch a potential issue in the above expression until I got to replacing text links. I needed to use a non “greedy” capture so that I wouldn’t pull in text after the link that happened to include a parenthetical comment. Normally, in reg ex I would use (.\*?) but in vim I needed to write (.{-}) …wtf?

```

:%s/[(.*)]((.{-}))/"1":2/g
```

Special thanks to Adam Wolf’s tip via [ShareGrove](http://www.sharegrove.com) which helped me document these steps.

> you can put VIM in a mode where the [command history](http://vimdoc.sourceforge.net/htmldoc/cmdline.html#Command-line) is just like another buffer. Not in insert mode, try q:

> You should get a new buffer that you can edit with the command history in it, so “\*yy would yank the current line into the system clipboard, etc.