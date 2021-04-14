---
title: 'cucumber and custom rspec matchers with rails 3.1'
date: '2012-01-22T08:40:52-08:00'
status: publish
exported_permalink: /2012/01/cucumber-and-custom-rspec-matchers-with-rails-3-1
author: sarah
excerpt: ''
type: post
id: 3548
category:
    - code
tag: []
post_format: []
---
I’m working my way through an epic Rails 3.1 upgrade and some of my cucumber features were failing because I was using a custom RSpec matcher and the method wasn’t found.

My custom matcher looks something like this:

```

module CustomMatchers

  class XmlSubsetMatcher
      :
  end

  def be_xml_subset_of(expected)
    XmlSubsetMatcher.new(expected)
  end
```

and when I ran my feature I was getting this failure:  
`<br></br>      undefined method `xml_subset_of?' for # (NoMethodError)<br></br>`

As it turns out, in my zeal to make sure everything was using the latest and great new stuff, I had forgotten to move over this critical configuration line in cucumbers env.rb:

`<br></br>World(CustomMatchers)<br></br>`

Now, my cucumber feature is happily failing cuz my code doesn’t work. Whew. I couldn’t find this documented anywhere and I’m not even sure where this documentation would belong. I found a hint on the [cucumber wiki rspec expectations page](https://github.com/cucumber/cucumber/wiki/RSpec-Expectations), but none of the code on that page is actually needed when using cucumber with Rails, so I decided not to touch it and just write this blog post.