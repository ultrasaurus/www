---
title: 'ruby to find latitude/longitude for a list of cities'
date: '2014-01-19T19:08:17-08:00'
status: publish
exported_permalink: /2014/01/ruby-find-latitudelongitude-list-cities
author: sarah
excerpt: ''
type: post
id: 4961
category:
    - code
tag: []
post_format: []
---
I have a relatively short list of cities which I want to plot on a world map. The list is a little too long for a manual lookup, but I don’t know exactly how I’ll use it in an app, so I figured out how to do it with some simple ruby in irb using the lovely [geocoder gem](http://www.rubygeocoder.com/).

I had my cities in a spreadsheet. Selected a few cells, and was able to simply paste into irb and split the string on newlines to get an array of the cities.

```


gem install geocoder
irb
>> require 'geocoder
>> a = "Honolulu, HI
>> Boston, MA
>> New York, NY".split("\n")
 => ["Honolulu, HI", "Boston, MA", "New York, NY"] 

>>a.map do |city| 
    d = Geocoder.search(city)
    ll = d[0].data["geometry"]["location"]
    puts "#{city}\t#{ll['lat']}\t#{ll['lng']}" 
end

Honolulu, HI    21.3069444  -157.8583333
Boston, MA  42.3584308  -71.0597732
New York, NY    40.7143528  -74.00597309999999

```

Then I could copy/paste the irb output back into my spreadsheet. Ta Da!

It appears that the free Google API has some kind of throttling, so this is only good for short lists of &lt;20 cities.