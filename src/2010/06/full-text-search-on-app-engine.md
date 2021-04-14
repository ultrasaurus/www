---
title: 'full text search on app engine'
date: '2010-06-10T07:03:00-07:00'
status: publish
exported_permalink: /2010/06/full-text-search-on-app-engine
author: sarah
excerpt: ''
type: post
id: 2721
category:
    - general
tag: []
post_format: []
---
I just got back from Google-sponsored hack session at RailsConf. Google App Engine and JRuby combine to create some real awesomeness. I created an small app that uses some classes from Lucene (written in Java) with a Rails app (written in Ruby) to search text stored in the App Engine data store. The idea was to search English text using standard linguistic analysis to distinguish whole words, as well as find variants of the same root word (e.g. find “run” and “running” when searching for run, but don’t find “runt”). It was helpful to read [prior work by Ikai Lan](http://ikaisays.com/2010/04/25/jruby-in-memory-search-example-with-lucene-3-0-1/).

First I [downloaded Solr](//www.motorlogy.com/apachemirror/lucene/solr/1.4.0/), which includes Lucene. I unzipped it into ~/src/sdk, then I [set up Rails for app engine](http://gist.github.com/268192). I experimented first in irb:

```

$ appcfg.rb run -S irb -r config/environment

> require '/Users/sarah/src/sdk/apache-solr-1.4.0/lib/lucene-core-2.9.1.jar'
=> []
> require '/Users/sarah/src/sdk/apache-solr-1.4.0/lib/lucene-snowball-2.9.1.jar'
=> []
> java_import org.apache.lucene.analysis.snowball.SnowballAnalyzer              
=> Java::OrgApacheLuceneAnalysisSnowball::SnowballAnalyzer
> snowball = SnowballAnalyzer.new("English")
=> #<Java::OrgApacheLuceneAnalysisSnowball::SnowballAnalyzer:0x2a134eca>
> s = StringReader.new("Testing Snowball")
=> #<Java::JavaIo::StringReader:0x7deb41d6>
> token_stream = snowball.tokenStream(nil, s2)
=> #<Java::OrgApacheLuceneAnalysisSnowball::SnowballFilter:0x439a8942>
> token_stream.next.term
=> "test"
```

Then I copied the .jar files I needed into WEB-INF/lib

```

$ cp ~/src/sdk/apache-solr-1.4.0/lib/lucene-core-2.9.1.jar  WEB-INF/lib/.
$ cp ~/src/sdk/apache-solr-1.4.0/lib/lucene-snowball-2.9.1.jar WEB-INF/lib/.
```

I ran generators to create my “content” field which is for the free-form text and another column I called index, but was mis-named, perhaps would be better to call it a “vector” or something. In any case, what I called the “index” was for the data that we will search on and I made it a special “List” type which is fast for app engine to search whole words.

```

./script/generate scaffold note content:string index:List -f --skip-migration
./script/generate dd_model note content:string index:List -f 
```

Then I changed the model to use the [Snowball](http://snowball.tartarus.org/texts/introduction.html) analyzer from Lucene. I include all of the model code below, which uses DataMapper instead of ActiveRecord so that it can use the app engine datastore which is not relational. I was quite impressed with how concise the code was and how easy it was to mix Java classes in Ruby — I simply declared the class at the top of the file with a “java\_import” and then I could call SnowballAnalyzer.new as if it were a regular Ruby class. Pretty sweet.

```

java_import org.apache.lucene.analysis.snowball.SnowballAnalyzer
java_import java.io.StringReader

class Note
  include DataMapper::Resource
  
  property :id,      Serial
  property :content, String,        :required => true, :length => 500
  property :index,   List,          :required => true
  timestamps :at 

  before :valid?, :update_index

  def update_index
    analyzer = SnowballAnalyzer.new("English")
    s = StringReader.new(content)
    token_stream = analyzer.tokenStream(nil, s)

    terms = []
    while (token = token_stream.next) do
      terms << token.term 
    end
    self.index = terms
  end
end
```

I then changed the index page to include a search form (joined in late night pairing by Ian McFarland) and in the controller action I could use very familiar Rails code to find the results:

```

    @notes = Note.all(:index => @query)
```

The complete code is on [github.com/ultrasaurus/full-text-search-appengine](http://github.com/ultrasaurus/full-text-search-appengine).

Create an app ID on the [app engine](https://appengine.google.com/) page. Add the app name info the config file and publish the app.

```

vi config.ru 
./script/publish.sh 
```

Note: this is not a complete solution. There are all sorts of features of Lucene that aren’t surfaced in this example, most significantly ranking. Also, the query really should be tokenized and stemmed as well as the “content” field that are being searched.