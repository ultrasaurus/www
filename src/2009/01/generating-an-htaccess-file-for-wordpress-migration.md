---
title: 'generating an .htaccess file for wordpress migration'
date: '2009-01-11T07:24:46-08:00'
status: publish
exported_permalink: /2009/01/generating-an-htaccess-file-for-wordpress-migration
author: sarah
excerpt: ''
type: post
id: 574
category:
    - code
tag: []
post_format: []
---
So, I’ve been working to migrate my ultrasaurus weblog from Movable Type to WordPress (this one will come later). Since all the links were changing anyhow, I decided to move from ugly numbered permalinks to pretty links based on the title of the post. I only had a few hundred posts, but enough so I didn’t want to be doing it by hand. Since I’m learning Ruby and infatuated with it at the moment, I wrote a Ruby script to generate the .htaccess directives.

In case this would be helpful to anyone else, here’s the code:

\[sourcecode language=’ruby’\]  
require ‘date’  
require ‘find’

Find.find(‘./archives/’) do |fname|  
\# puts fname  
date\_string = “”  
title = “”  
next if File.directory?(fname)  
File.open(fname, “r”) do |f|  
 f.each\_line do |line|  
 if m = line.match(“(

)(.\*)(
-------

)”) then  
 date\_string = m.captures\[1\]  
 elsif m = line.match(“(

### )(.\*)(&lt;/h3)") then  
 title = m.captures\[1\].downcase  
 end  
 end  
end 

\# for some reason my mt archives include some old drafts with no titles  
next if title == ""

oldfilename = File.basename(fname)

\# 1) remove chars that I think wordpress removes  
\# 2) change spaces to dashes  
\# 3) handle this case to avoid —  
\# Emmy Award for Outstanding Lead Actress – Miniseries or Movie  
\# also avoid — which I saw in my data, but not sure why it was there  
\# 4) remove trailing dash if there is one  
\# Thank you ruby-talk http://www.ruby-forum.com/topic/167299  
title = title.gsub(/\[(,?!'":.+=/)\]/, '').gsub(' ', '-').gsub('–','-').gsub(/-$/, '')

\# get the new path to the entry, like "/2003/03/brand-new-weblog/"  
date = Date.parse(date\_string)  
newpath = sprintf("%d/%02d/%s/", date.year.to\_s, date.month.to\_s, title);

\# we want something like this:  
\# redirect 301 /old/old.htm http://www.you.com/new.htm

output = "redirect 301 /sarahblog/archives/" + oldfilename + " https://www.ultrasaurus.com/sarahblog/" + newpath  
puts output

end # loop thru files in directory  
\[/sourcecode\]