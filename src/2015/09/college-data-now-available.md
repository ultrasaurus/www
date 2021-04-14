---
title: 'college data now available'
date: '2015-09-13T20:44:34-07:00'
status: publish
exported_permalink: /2015/09/college-data-now-available
author: sarah
excerpt: ''
type: post
id: 5652
category:
    - general
tag: []
post_format: []
---
The Dept of Education just released its new [College Scorecard](https://collegescorecard.ed.gov/), which includes never-before-released data like earnings 6-10 years after leaving school, combined with previously open data like admissions and completion rates. The data reveals data about the school, not individual student data, with the goal of helping prospective students compare schools based on real data about outcomes.

It was announced yesterday in [President Obama’s weekly video address](https://www.whitehouse.gov/the-press-office/2015/09/12/weekly-address-new-college-scorecard) along with a wonderful behind-the-scenes look at the [human-centered design process](https://www.whitehouse.gov/blog/2015/09/12/under-hood-building-new-college-scorecard-students).

My primary role has been to make the data available in a way that made it possible to build such a lovely website and also for others to create their own tools and analysis. With the help of open source contributors and colleagues at 18F, I created the [Open Data Maker project](https://github.com/18F/open-data-maker) that powers the [College Scorecard API](https://collegescorecard.ed.gov/data/documentation/).

[![filter UI with sliders for cost, graduation rate and salary after attending](../../../uploads/2015/09/Screen-Shot-2015-09-13-at-7.36.42-PM.png)](https://collegescorecard.ed.gov/search/?avg_net_price=..16000&completion_rate=0.44..&median_earnings=35000..&degree=b&major=history&sort=advantage:desc)The really innovative work was done by the Department of Education, bringing together data from Treasury and IRS, combined with their previously open data from the [Office of Postsecondary Education](http://www2.ed.gov/about/offices/list/ope/index.html).

In working on this project, I learned that the average high school graduate earns $25,000 per year. One way to look at the the value of the education offered by a particular school is the percentage of students who later earn more than those without a college education. This was chosen as the default sort order (“% Earning Over HS Grad”).

The site allows some filtering on additional data points: cost, graduation rate, and salary after attending. Looking at 4-year liberal arts schools (by picking those that offer a History degree), that are below average cost, and higher than average graduation rate and salary after attending, I found these results:

[![Harvard, Stanford, Georgia Institute of Technology, Missouri University of Science and Technology, Michigan Technological University, University of Delaware, Texas A&M...](../../../uploads/2015/09/filtered-search-cropped.png)](https://collegescorecard.ed.gov/search/?avg_net_price=..16000&completion_rate=0.44..&median_earnings=35000..&degree=b&major=history&sort=advantage:desc)

I was surprised to see Harvard and Stanford at below average cost — it is great to see these schools putting their large endowments to good use. Looking at details for Harvard, for example, we can see that costs vary widely based on family income and there’s a link with a link to the “net price calculator” which is provided by every school:

[![charge FAMILY INCOME with AVERAGE COST
$0-$30,000 is $3,897, $30,001-$48,000 is $2,977, $48,001-$75,000 is $5,405, $75,001-$110,000 is $13,604, $110,001+ is $36,946](../../../uploads/2015/09/harvard-cost.png)](https://college.harvard.edu/financial-aid/net-price-calculator)

Unsurprisingly, technical schools are high on a list sorted by earnings, though liberal arts school are also prominent. For example, the University of Delaware shows great outcomes for students at below average costs:

[![Screenshot: click to view the page](../../../uploads/2015/09/university-of-delaware1.png)](https://collegescorecard.ed.gov/school/?130943-University-of-Delaware)