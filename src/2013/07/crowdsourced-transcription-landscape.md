---
title: 'crowdsourced transcription landscape'
date: '2013-07-23T02:00:05-07:00'
status: publish
exported_permalink: /2013/07/crowdsourced-transcription-landscape
author: sarah
excerpt: ''
type: post
id: 4117
category:
    - general
tag: []
post_format: []
---
The following is based on [an interview with Ben Brumfield](https://www.ultrasaurus.com/sarahblog/2013/07/why-crowdsourced-transcription/), after which I did a bit of research myself, adding links and some additional references.

There are 6 general areas from which people are doing transcription.

1. **Investigative Journalism**: crowdsourcing information for citizen investigation. The idea is to get a whole lot of people to flag and inspect information. People type up the information on scanned documents (e.g. receipts, tax returns), transcribing what they see. Then write a total of receipt on a separate page. Basic transcription + high level purpose-built extraction. Gather the data to use it for something. Volunteers are politically motivated. 
  - [ProPublica](http://www.propublica.org/)
  - [The Guardian and MP expenses scandal](http://www.niemanlab.org/2009/06/four-crowdsourcing-lessons-from-the-guardians-spectacular-expenses-scandal-experiment/)
2. **Bio informatics** The archetypical artifact is a plant specimen with a bunch of labels on them — structured data. They are presenting users with a full image, asking people to extract information. No free form text entry. They tend to be more sophisticated in how they represent documents. “Even if you see an error, type what you see.” or select from a menu. Their volunteers are smaller group more informed group, who want to help science and/or love the subject themselves. Participate even if not active physically. Motivated by the immersive nature of transcription — living in that document, you are really “there.” 
  - Paul Flemons work with [Atlas of Living Australia](http://volunteer.ala.org.au/)
  - [Calbug](http://calbug.berkeley.edu/) working with [Zooniverse](https://www.zooniverse.org/).
3. **Library and Archive world** – scanned letters, papers and diaries. Much more immersive with a narrative flow, which keeps people coming back. Two goals: 1) improve databases (i.e. finding aids) Plain text transcript can be put into Solr DB. 2) improves findability, will be crawled by Google, &amp; people who don’t know about the material or institution. They are also looking at the outreach perspective. Connect with potential patrons/users. Not just labor, but a service – let your users engage more deeply with collections. Tighter connection = advocates. 
  - [National Archives](http://transcribe.archives.gov/) launched a transcription pilot project. All of their materials currently online are completed, but they point people to WikiSource where they have a list of images from the National Archives queued up to work on.
  - University of Nebraska Lincoln – launched campaign to transcribe alumni yearbooks.
  - [DIYHistory](http://diyhistory.lib.uiowa.edu/)
4. **Literature Scholars** – [TextGrid](http://www.textgrid.de/en/), system that was built where all transcription is done off-line in Eclipse, then full transcripts are contributed — this is also a way of giving what scholars already have. Sounds good, but tapping into the scholarly workflow has challenges. For scholars, transcripts are a middle work. They don’t get an incentive for contributing this effort. They typically want everything that has their name on it to be properly cited and looking good. Where that DOES work to some degree is Genealogy (see below). They’ve been doing it for longer and are ok with sharing with a somewhat broader audience. Worry about plagiarism, non commercial use, etc. Not trying to write a book like other scholars.
5. **Geneology** – Generally volunteers will first focus on transcribing material about their own ancestors, then stuff about where their ancestors are from, next they move on to generally useful material like the 1940s census, which leads them to communities of like-minded folks. If you offered them the opportunity to transcribe stuff from their own families, they would leap on it. They are working with tabular records: ship records, shareholder lists. 
  - [Open Source Indexing](http://opensourceindexing.org/)
  - [FamilySearch](https://familysearch.org/)
  - Transcribing ship logs ([Old Weather](http://www.oldweather.org/)) is much like census
6. **Literary and Historical** – A lot of people at the conference seemed to be talking about how to add rich set of markup to indicate things like strikeouts, changes in handwritings, personal names, place names. Taking this approach generally yields small, but quite dedicated, communities of users — their data model is XML, usually TEI XML. They are embedding the information in the document. The majority of the tools that exist are all for that community. [FromThePage](http://beta.fromthepage.com/) is in this camp — you can use a lighter wiki markup for proper names, creating an automatic index and cross-linking between pages. 
  - [Transcribe Bentham](http://blogs.ucl.ac.uk/transcribe-bentham/)
  - [FromThePage](http://beta.fromthepage.com/)