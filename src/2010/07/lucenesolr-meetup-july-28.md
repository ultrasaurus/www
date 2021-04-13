---
title: 'lucene/solr meetup, july 28'
date: '2010-07-30T20:34:43-07:00'
status: publish
permalink: /2010/07/lucenesolr-meetup-july-28
author: sarah
excerpt: ''
type: post
id: 2753
category:
    - general
tag: []
post_format: []
---
I attended the [Lucene/Solr meetup](http://www.meetup.com/SFBay-Lucene-Solr-Meetup/calendar/14124466/) this week — quite a swank event sponsored by [Salesforce](http://www.salesforce.com/) with tasty appetizers, beers and an incredible view of the bay. The three speakers were very knowledgeable and well spoken and I enjoyed hearing about the different applications of Lucene and Solr. Below are my rough notes. For folks who want to learn more about Lucene and Solr, check out the upcoming conference [Lucene Revolution](http://lucenerevolution.org/), Oct 5-8, 2010 in Boston.

Search@salesforce.com, Bill Press, Salesforce
---------------------------------------------

Salesforce uses Lucene 2.2 (not Solr) and shared some stats about their seriously large scale operation:

- millions of searches per day, hundreds of thousands of users
- hundreds of millions of doc updates per day
- force.com platform, 72,500+ customers, 150,000+ apps
- almost half a billion indexing events per day (batches can include &gt; 1000 documents)
- Over 8 TB of searchable data
- incremental indexing (90% &lt; 3 mins, 70% &lt; 1 min )
- 6M queries per day, mean search time 250ms (76% &lt; 250 ms, 89% &lt; 500 ms)

It’s a multi-tenant architecture, each org has 1-100,000s users and had a single codebase, which means there is just 1 version to support at one time.

- consistent hashing for node affinity
- throttling for fairness
- record type bucketing, as well as by org

They use post-filtering for:

- authorization
- reranking in the DB, last update

They query db to bridge the gap with indexing lag.

They are faced with new search challenges driven by what Salesforce CEO calls “the facebook imperative.” When he started Salesforce, he used to ask “why donesn’t every enterprise app look like amazon?” Now he asks: “why doesn’t every enterprise app look like Facebook?” (side note: this is an echo of what many folks have been saying for a while, that social networking makes sense as a feature of an app, rather than just destinations like Facebook and LinkedIn.)

Salesforce allows you to have a feed on a record, follow accounts, status updates for accounts. They index tracked changed. They need to search this rich set of data which is people articulating their interests. Bill noted that the needs of structured data are really different from unstructured data.

Practical Relevance, Grant Ingersoll, Lucid Imagination
-------------------------------------------------------

Grant Ingersoll spoke of “two tales of relevance”

- The case of the missing data: you know you have poor relevance when the most important search result is on page 10. For example, the accessories for an item are often listed higher on search results than the item itself.
- The power of suggestion. Grant cited a specific case where just adding auto-suggest added 100s of millions to the bottom line.

Better search results = less time searching, more time acting

Other cases to consider:

- Only the first result matters, such as Google’s “I’m feeling lucky”
- Known item searches, for example: NetFlix has a high frequency of people searching for specific movies
- Are you finding all the documents that are relevant? In the case where you want to analyze all the results returned/
- Is zero results the right answer? Where people want to definitely know that something is not present
- Is it important that you don’t have a result that doesn’t match (e.g. Yelp doesn’t want to find a plumber talking about unclogging what you just ate when you are looking for a restaurant)

Befre undertaking any relevance tuning, you need to define what “better search” means to you. There are many ways to test and measure:

- a/b testing
- log analysis
- empirical (top x queries, plus random sample) — read and evaluate queries, top 10, top 50, have your top biz people rate what is important –&gt; leads to actionable data
- ask your users, thumbs up/down around your search results
- Ad Hoc evaluation
- TREC — fixed data set, fixed queries, see open relevance project (open source TREC)

Capturing user feedback:

- log analisys (click analyss)
- rating/reviws
- filters and facets

Grant notes that Lucene searches default to “or” out of the box, when “and” is typically better today. He had a list of links that he suggested we check out (sadly I couldn’t type fast enough, but here are some I wrote down):

- [code.google.com/p/luke](http://code.google.com/p/luke/)
- solar analysis tool
- [sigir.org](http://sigir.org/)
- [Debugging Relevance Issues in Search](http://www.lucidimagination.com/Community/Hear-from-the-Experts/Articles/Debugging-Relevance-Issues-Search?utm_medium=lucene.li-copypaste&utm_source=direct-lucene.li&utm_content=awesm-site)

auto-add phrases to your questies — surround with quotes — automtric win  
auto-add a “sloppy phrase” — large slop factor, like an AND, boost when words are close

Logs, Search, Cloud, Jon Gifford, Loggly
----------------------------------------

Logfile managemetn in the cloud (no Hadoop). Logs are painful — distributed, large, ephemeral. Most log search is hightly skewed. “We’re just implementing grep across terabytes of data.” This was a compelling talk, but it took most of my attention to follow, so my notes are weak and may make sense to no one except me:

syslog + 0MQ + SolrCloud  
0MQ – not traditional queing, it fails, when it fails we lose data, but it is very fast  
Solr give s us facets which gives us graphs

run many indexers, “hot shards” — the indexers update small shards

0MQ gives us node-specific input queues for Solr

nrt + solrCloud = Our Nirvana

Hot shards re chilled when we stop writing to them

Solr is awesome at what it does, but not so good for data mining  
— plan to plug in Hadoop for large-volume analytics  
Syslog is the only way in for now, adding others, http, scribe, flume,