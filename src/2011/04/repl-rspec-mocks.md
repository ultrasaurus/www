---
title: 'repl rspec mocks'
date: '2011-04-04T17:59:19-07:00'
status: publish
exported_permalink: /2011/04/repl-rspec-mocks
author: sarah
excerpt: ''
type: post
id: 3127
category:
    - code
tag: []
post_format: []
---
[REPL](http://en.wikipedia.org/wiki/Read-eval-print_loop) (Read-Eval-Print-Loop) is a great way to learn. With Ruby, the experience is enabled with irb. Sometimes, to do this we need to peek into the innards of things, which I find to be an extremely effective way to explain mocks and stubs. It’s a regular part of my Ruby curriculum, even though I have needed to figure out the syntax three times in the last couple of years. (Many thanks to Jen-Mei Wu for the most recent iteration.) I still think it is worth it, even though it seems to change with crazy frequency.

Just in case anyone else ever wants to do this with current or previous versions of RSpec, I thought I would write it down before old versions become lost in the mists of time:

RSpec 2.9
---------

\[update for [repl mocks for RSpec 2.9 by Curtis Schofield](http://blog.blazingcloud.net/2012/04/14/repl-mocks-in-rspec-2-9/)\]

```

>> require 'rspec/mocks/standalone'
>>Time.stub(:now).and_return(10,20)
>>Time.now
10
>>Time.now
20
>>Time.now
20
 
```

RSpec 2.5
---------

```

>> require 'rspec/mocks'
>> include RSpec::Mocks::Methods
>>Time.stub(:now).and_return(10,20)
>>Time.now
10
>>Time.now
20
>>Time.now
20
```

RSpec 2.0
---------

```

>> require 'rspec/mocks'
>> require 'rspec/mocks/extensions/object'
>>Time.stub(:now).and_return(10,20)
>>Time.now
10
>>Time.now
20
>>Time.now
20
```

RSpec 1.3
---------

```

>> require 'spec'
>> require 'spec/mocks'
>>Time.stub(:now).and_return(10,20)
>>Time.now
10
>>Time.now
20
>>Time.now
20
```