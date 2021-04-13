---
title: 'using ruby to fight aids'
date: '2009-04-18T14:29:29-07:00'
status: publish
permalink: /2009/04/using-ruby-to-fight-aids
author: sarah
excerpt: ''
type: post
id: 1124
category:
    - general
tag:
    - gogaruco
    - Ruby
post_format: []
---
We just heard a fantastic talk by Jacqui Maher about her work on the [Boabab project](http://www.baobabhealth.org/), fighting AIDS in Malawi, Africa.

First, she gave us an overview of the AIDS epidemic, especially in Africa:

- Africa has 12% of the world’s population, but 60% of the people with AIDs
- In Malawi 
  - 14% of adults have AIDS
  - 8 people die every hour from aids
  - there are 280 doctors
  - 3500 HIV/AIDS patients per doctor

When she arrived, patients would wait in long lines to see a doctor and patient intake would typically take 15 minutes. It was all paper-based an error-prone. In Malawi, they have a national id program where every ID card has a bar code. This could be used for easy patient intake. After they developed the hardware/software solution, it would take less than 1 minute to register new patients and less than 10 seconds for returning patients to get through the intake process.

The solution was designed to help in a number of areas:

- Patient Registration: entering new patient data, generate national id bar code, or scan an existing one
- Encounters: any patient interaction
- Observations: diagnosis, progression, vitals, patients complaints, drug regimen
- Prescriptions: drugs, ingredients, inventory, etc.

They overcame challenges with spotty internet connections and low bandwidth. They use a wireless mesh network, which is self-healing. The portable computer they used was based on the I-Opener (initially bought from the US on eBay, then 2000 were donated) which was hacked to include a touchscreen, ethernet, PoE (power over ethernet) and a bar code scanner. The software is Ubunto, Ruby on Rails, and MySQL.

More details on the software:

- BART – Baobab Anti-Retroviral Treatment
- OpenMRS Data model
- templating using ERB
- App calls via AJAX
- Rspec tests

Jacqui told a great story about Gem the Janitor (yes, that is his real name) who just picked up the device during a busy time when all of the nurses were busy, figured out the interface quickly and started helping register people. Now he runs the whole intake process.

Why RoR?

- great community
- common consensus on best practices
- active contributions to OSS
- very accessible information on every part of the stack
- supurb interactive tutorials like peepcode
- Ruby is easier to learn offline that other languages, comes with documentation
- ActiveRecord: makes complex data models easier

Now 265 of the 280 doctors are using this app. The data collection enables extensive reporting, enables agencies to use the data to focus research &amp; funding, and influence policy decisions.

You can help!

- <http://github.com/baobab/>
- the developers are on IRC: freenode #baobab
- more info: [www.baobabhealth.org](http://www.baobabhealth.org/)