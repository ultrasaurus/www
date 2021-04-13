---
title: 'command line happiness'
date: '2009-02-28T12:53:20-08:00'
status: publish
permalink: /2009/02/command-line-happiness
author: sarah
excerpt: ''
type: post
id: 884
category:
    - code
tag:
    - bash
    - vi
post_format: []
---
How could I have lived for so long without knowing that I could set up my command line with vi key bindings? Well, for anyone else who uses vi and bash, here’s the secret…

Create ~/.inputrc

```

set meta-flag on
set input-meta on
set output-meta on
set convert-meta off
```

add this to your .bashrc

```

set -o vi
```

Thanks [Adam](http://elasticprocess.com/blogs/adam)!