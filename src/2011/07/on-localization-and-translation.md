---
title: 'on localization and translation'
date: '2011-07-04T09:22:25-07:00'
status: publish
exported_permalink: /2011/07/on-localization-and-translation
author: sarah
excerpt: ''
type: post
id: 3241
category:
    - general
tag: []
post_format: []
---
In thinking about presenting a web site in a different languages, there are a few very different concerns:

- [A localized user interface](#localized).
- [Localized brand](#brand)
- [Unique content](#unique)
- [User-generated content in different languages](#ugen)
- [Translated content](#translation)

In addition, some sites might consider [SEO Translation](http://www.seo-translator.com/the-difference-between-localization-and-seo-translation/) to entice people searching in their native language to find a site even if the site itself isn’t translated (but to me that seems like a cheap hack). If you really want to reach someone, you want to do so in their own language.

I’ve collected examples below of each different kind of translation and at the end I’ve listed [ways to detect and retain language settings](#options) with implications for SEO and user experience.

A <a name="localized">**localized interface**</a> is when we translate the functional parts of an application, but it still may display text or play audio/video from a different language. You Tube is a good example of this. In the image below we can see that the navigational elements, YouTube tagline, and labels are in Japanese, but the videos and user-generated text are in their own language. It seems odd to me that I’ve selected Japanese as a language, but that I’m seeing mostly English language content. Perhaps YouTube is detecting my geo-location and showing me videos that are popular in my country, or perhaps YouTube just shows everyone what is globally popular which would slant the votes towards English-language (or perhaps more specifically American English language) content because of its US origins.

<div class="thumbnail">[![YouTube - Broadcast Yourself](https://img.skitch.com/20110704-ekt432gn3wcwiy33w5pstb78ad.preview.jpg)](https://skitch.com/ultrasaurus/febja/youtube-broadcast-yourself)</div><figure class="wp-caption thumbnail alignright" style="width: 150px;">[![Brand Localization Challenges](http://twitpic.com/show/thumb/5keiag.jpg)](http://blog.mightyverse.com/2011/07/brand-localization-challenges/) <figcaption class="wp-caption-text">Brand Localization Challenges</figcaption></figure>A <a name="brand">**localized Brand**</a> is sometimes necessary when [brands don’t translate well](http://blog.mightyverse.com/2011/07/brand-localization-challenges/). If you need to re-brand for a specific market because of the meaning of some word used in your brand, it is likely that your website content will be so different as to not apply to the rest of this article.  
  
<a name="unique">**Unique content**</a> may be the result a targeted marketing initiatives, where advertisements or introductory material in a language is written to be appropriate to the target culture. For some text-focused products, the product may actually differ in some meaningful way in the target language, such as with [WordReference.com](http://www.wordreference.com/) which has different dictionary features available for some languages, so the introductory text is quite different between Spanish and German pages:

<div class="thumbnail" style="float:left;margin:10px">[![Oxford German-English dictionary - WordReference.com](https://img.skitch.com/20110704-tthy5fm35669xr93722fkhwyic.preview.png)](https://skitch.com/ultrasaurus/f89f2/oxford-german-english-dictionary-wordreference.com)</div><div class="thumbnail" style="margin:10px">[![Diccionarios de Español, Ingles, Francés, Portugues - WordReference.com](https://img.skitch.com/20110704-g9k87jm2xwmcsj1swp7jsktpft.preview.png)](https://skitch.com/ultrasaurus/f89gq/diccionarios-de-espanol-ingles-frances-portugues-wordreference.com)</div>   
<a name="ugen">**User generated content**</a> like we saw in the YouTube example above is a bit different from uniquely targeted or language-specific product text. When people write comments or submit text or video contributions in their own language, that content may be appropriate to a global audience, even if it was submitted in a specific language. Most sites don’t even have a way of detecting or specifying the submission language, so they simply display all user generated content equally. It is technically possible to detect language (or at least make a good guess) based on unicode characters and dictionary lookup. For example, the language website tatoeba does this quite well. You just need to be careful to allow the user to change the language, because it is possible to guess wrong. For example, some Japanese words share Chinese characters and other languages also share sequences of characters that have different meaning. In the example below Tatoeba guessed the language correctly for my three words, but allows me to select a different language just in case:

<div class="thumbnail">[![Firefox](https://img.skitch.com/20110704-c2899un757q7m2rwn95gwe2y96.preview.jpg)](https://skitch.com/ultrasaurus/febs8/firefox)</div>Providing <a name="translation">**translated content**</a> makes sense for a global brand with information that is generally useful to a global audience. For example, Adobe translates product information pages such as with <http://www.adobe.com/aboutadobe/volumelicensing/> and <http://www.adobe.com/la/aboutadobe/volumelicensing/> :

<div class="thumbnail" style="float:left;margin:10px">[![software discounts | Adobe Volume Licensing | home](https://img.skitch.com/20110704-fckkhyn9r1ete66a5xig6wrtsq.preview.png)](https://skitch.com/ultrasaurus/febt4/software-discounts-adobe-volume-licensing-home)</div><div class="thumbnail" style="margin:10px">[![descuentos de software | Programa multilicencia de Adobe | inicio](https://img.skitch.com/20110704-mu1u2s45xr6jn91piqfn8pdt8y.preview.png)](https://skitch.com/ultrasaurus/febtw/descuentos-de-software-programa-multilicencia-de-adobe-inicio)</div><a name="options"></a>

Technical Options
-----------------

There are a few ways to detect and respond to the need to reach people who speak different languages.  
We can display a specific language, based on:

1\) **Accepts header, cookie or query parameter**. For example, [Tatoeba.org](http://tatoeba.org/) respects the accepts header and redirects to <http://tatoeba.org/spa/> when it is set to Spanish (es). Whereas, YouTube requires you to set your language (at the bottom of the page), then uses a query param (<http://www.youtube.com/index?hl=es>) which remains sticky, presumably with a cookie, to retain the language setting.

2\) **Country domain**. (e.g. www.google.fr, de.wikipedia.org) This is most useful when content or functionality is targeted for the culture or adjusted based on geolocation. It makes it easy for users to see content for their country or culture even when they are away from home or for cultural tourists or language learners to easily experience a language and culture without leaving their home country. Google has a nice article about [geotargeting](http://googlewebmastercentral.blogspot.com/2010/03/working-with-multi-regional-websites.html) (via [@avdi](http://googlewebmastercentral.blogspot.com/2010/03/working-with-multi-regional-websites.html)).

3\) **Language encoded in the URL** This can be combined with #1 above for language detection or be based solely on links.

Steve Klabnik wrote an [insightful post](http://blog.steveklabnik.com/2011/07/03/nobody-understands-rest-or-http.html) (mostly focused on Web Services APIs) where he argued for using the accepts header for localized content. However, the implications for SEO are significant. It is appropriate to use an accepts header, query parameter or cookie when the displayed text is not significant to the content. Most localized UI text (such as “Log in” or “Submit”) is not going to be significant to a search engine or ultimately to the person choosing whether the page is the one they want.

However, if the content is translated, then it could be argued that the page is, in fact, a different resource — different content, different audience. The challenge is exacerbated by the fact that the Google indexing bot will always request our pages in English, so without a separate URL that always presents non-English content, people searching with Google based on non-English queries will be unlikely to find a page that is auto-translated based on the Accepts header or a query parameter.

I dove into this exploration while thinking about how to implement the user experience in multiple languages for [Mightyverse](https://www.mightyverse.com). Currently, the site is very English-language-centric and translations of videos are always presented in English. Under the hood, we have a bunch of translations in other languages that I want to figure out how to display to people and to search engines. In some ways the site is like a dictionary site, but in other ways it’s a lot like any media site that would have multi-lingual content and localized UI. Oddly, YouTube was the only media site I could find with content in different languages — I’m sure I know of others, but its not something that is easy to search for!

My conclusion is that the technical solution should be based on the intent. Is the content for a page different enough to be considered a different resource? I personally believe that there is no such thing as a translation which is identical to the source material. Equivalent words in different languages have different connotations. Often the actual substance needs to differ based on a different audience, often in a different country, sometimes with different laws and certainly with a different culture.

Alternately, I suppose I could combine the approaches, and detect that a search bot is asking for the page and generate a document with all of the text for all languages, then display it based on the accepts header and allow the end user to change the language and remember that. I worry, though, that I would need to choose a language for the meta tag description and therefore the page summary presented by the search engine would not match the language of the search query… or maybe I shouldn’t worry and just expect the search results to be smart enough to display relevant text.

\[Update: better to have different pages for different languages see [multicountry/multilingual seo](https://www.ultrasaurus.com/sarahblog/2011/07/multicountrymultilingual-seo/).\]