---
title: 'mobile payments hidden costs'
date: '2011-08-25T15:10:59-07:00'
status: publish
permalink: /2011/08/mobile-payments-hidden-costs
author: sarah
excerpt: ''
type: post
id: 3366
category:
    - general
tag: []
post_format: []
---
In the so-called 3rd world, mobile payments are stimulating economic growth and individual entrepreneurship. While in the United States, we struggle to overcome the legacy of an earlier trend in mobile payments facilitated by a plastic card. New players such as [Square](https://squareup.com/), [Verifone](http://www.verifone.com/), and [Erply](http://www.erply.com/) are bringing us, belatedly, into the modern world.

TechCrunch [reported yesterday](http://techcrunch.com/2011/08/24/intuit-partners-with-verizon-wireless-to-sell-square-competitor-at-retail-stores/) on Square-competitor, [GoPayment](http://gopayment.com/), a mobile credit card reader from the well-established Intuit. Perhaps the Verizon partnership to offer them in retail stores and piles of marketing with the well-known Intuit name will spur adoption. However, to understand the real value to the small business owner, we need to look past the nifty device that plugs into your mobile phone or tablet. What matters most to the small business owner is the effect on the business — what is the setup time and expense, switching costs, transaction fees, and cash flow.

As a small business owner with some recent real-world experience in getting set up to accept AmEx, I applaud this disruptive change. This spring I spent a few weeks of my life disentangling tens of thousands of dollars from a maze of holding centers and risk management departments. All the trouble came from the intermediary MerchantOne with whom we set up a merchant account. In turn MerchantOne accepted payment through FirstData, which initially held the payment. (Despite having been assured of 24 hour approval and 5 day settlement.) MerchantOne offered several types of accounts and allowed us to switch to another one but require a reversal of payment which was WITHDRAWN from OUR bank account, instead of FirstData’s and then, subsequently, held the second payment. It’s a long and sorry tale that leads me to know more about credit card processing than one would expect for a software consulting company.

Many thanks to Bill Devine, biz dev guy extraordinaire, who researched much of the info below. I thought it important to share my perspective and shed light on some of the hidden corners in the payments world for those who are new to it.

Setting up
----------

The biggest difference between Square and its competitors is that Square doesn’t require that you set up a Merchant account. If you already accept payments, you already have a merchant account and with GoPayment you’ll need another from Intuit. For the uninitiated, a Merchant account is offered by 3rd parties as a way to accept credit card payments from multiple card companies. In reality, even if you just want to process a single payment from a single credit card company, you pretty much have to deal with these intermediaries. Typically, setting up a merchant account takes weeks, involves credit checks and verifications that you are who you say you are. When I can get an online credit card by filling out a web form, it does seem a little incongruous that allowing someone to give me money should take more than 24 hours. In adding to the setup time, there are additional costs — Merchant accounts typically have multiyear terms with setup and/or early termination fee (from Intuit, it’ll be $60 signup and $19.95/month).

Note: Square doesn’t require merchant accounts because it acts as a Internet Payment Service Provider (possible through a partnership w/ Visa) which essentially means it manages a single merchant account, and assumes all risk for all merchants. This may give Square more collective bargaining power since they are moving a lot of money under a single account (via [Quora](http://www.quora.com/What-are-the-differences-between-Squares-and-Intuits-GoPayment-merchant-services-on-boarding-processes))

Aside from the merchant account nonsense, GoPayment offers a “free” reader which is only free via rebate, whereas if you buy a Square reader in the Apple Store they credit your account. If you sign up using the iPhone app, they will physically mail you one for free.

Fees
----

Merchant accounts also typically have their own transaction fees, but aside from that GoPayment’s rate (2.7%) is seemingly less than Square’s (2.75%). Until you take a look at the asterisks:

- Any business, rewards, or foreign card automatically bumps that up to 3.7% + $.07 per transaction
- If you want to accept American Express the you’ll have to apply and be placed in some bracket that can go up to 3.5%

Note: Everyone has a higher fee for manual entry of credit card numbers, which is based on credit card company policies.

Cash Flow
---------

Merchant accounts are evil. In this day of instantaneous wire transfers, companies like MerchantOne, FirstData and even alternate payment services like PayPal, routinely hold money for 5-10 business days. I assume they make piles of money off the interest, while still charging fees on every transaction, and sometimes sign-up and termination fees as well.

Square settles payments every evening. Money is in your bank account the next day.