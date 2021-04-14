---
title: 'empowering content creators with drupal'
date: '2013-07-27T05:59:16-07:00'
status: publish
exported_permalink: /2013/07/empowering-content-creators-with-drupal
author: sarah
excerpt: ''
type: post
id: 4163
category:
    - code
tag: []
post_format: []
---
[Bryan Braun](http://bryanbraun.com) ([@bryanebraun](https://twitter.com/bryanebraun)) gave a refreshingly opinionated talk [Empowering Content Creators with Drupal](http://capitalcamp.org/content/empowering-content-creators-drupal). Coming directly from the Ruby and Rails communities where a core value is to articulate best practices, it is great to see this kind of guidance from a member of the Drupal community. ([slides here](http://bryanbraun.com/slides))

Bryan referred to a blog post by Dilbert creator Scott Adams on the [Botched Interface Market](http://dilbert.com/blog/entry/botched_interface_market/), where sites like Orbit and Travelocity had such poor user experiences that they inadvertently created a market opportunity for new sites like Hipmunk. Bryan’s goal is that Drupal should not become a botched interface market.

He organized his advice into two categories:

1. **[More Control](#control)**: Power Tools, Reducing Risk
2. **[Less Confusion](#clarity)**: Better Interface, Streamline Workflow

Bryan highlights borrowed techniqes from other platforms (mostly WordPress), and points out lots of “low-hanging fruit” techniques.

Example: the default layout for a node has a lot of labels and whitespace which doesn’t contribute to understanding the page. The default UI for a file attachment is not concise. Compare Gmail’s message compose interface vs. what it would be in Drupal (~1/3 of your screen vs. a page that is two screens high!) Having a very long page can contribute to confusion, since you have to scroll to get to some of the functionality.

Larry Garfiled’s blog post [Drupal is not a CMS](http://www.palantir.net/blog/drupal-not-cms) points out that Drupal is something you use to build a CMS. Perhaps we should think of it as a CMF, a Content Management Framework. In this case, we are designing the workflow and user experience of a new custom CMS that we build with Drupal.

**Myth: I am not a designer**  
 **Fact: um.. you actually are.** Whether you identify as a designer or not. The decision you make when you are building a site has an effect on the end user — these are design decisions!

Myth: it will take a long time and effort  
Fact: it could but it doesn’t have to  
<a name="control"></a>

More Control
------------

We can make our content creators more productive by giving them “power tools” while at the same time, reducing risk that they will make mistakes will give them confidence to move faster.

### WYSIWYG

It’s not really an option anymore to tell people to edit HTML. \[My personal perspective is that even though I am perfectly capable of HTML markup, why should you make me type extra characters? why should I have to learn the markup that works with your stylesheet? Though I do like the option of editing HTML when the rich text editors fail me.\]

The following modules are good for WYSIWYG and File Upload:

- [wysiwyg](https://drupal.org/project/wysiwyg) or [ckeditor](https://drupal.org/project/ckeditor) which both appear to be rich text, WYSIWYG editors
- [media](https://drupal.org/project/media) or [imce](https://drupal.org/project/wysiwyg) for uploading and managing file (also seems to be an either/or choice

### Node Editing Power

Always check “Add to Menu” on the Node Edit page — for most content creators, if a menu isn’t there, the feature doesn’t exist.

With context, use a module with [Context Node](https://drupal.org/project/context_node) which can pull out just a few context options and put it on the Node Edit page.

As a themer, you can make a bunch of templates and the content creator can pick with [template -picker](https://drupal.org/project/template-picker) module.

### Use Short Codes

Short code are a best practice from WordPress and can accelerate content creation:

```
[video:url]
[[nid:123]]
```

Drupal Modules:

- [Caption Filter](https://drupal.org/project/caption_filter)
- [Video Filter](https://drupal.org/project/video_filter) works with the wysiwyg module or with TinyMCE or CKEditor (not sure why those are in a different category).
- [Insert View](https://drupal.org/project/insert_view) lets content editors add views without editing PHP
- Make your own

In Drupal we tend to expose this kind of functionality as a block, but that gives the power to the site builder, rather than the content creator. In Drupal, the modules that do this tend to be called filters.

### Reduce Risk

Always put description text when you are creating new fields (you probably won’t come back later). If you are going to come back later, you can improve it then — at least put something in.

- [Autosave](drupal.org/project/autosave)
- Revisions: just enable it by default
- Preview — poor experiences with the preview button, not always what you expext
- Turn off preview button on content types page, use use [view\_unpublished](https://drupal.org/project/view_unpublished) module instead

Granting **Appropriate Access** is not an easy fix. You need to understand how your organization works, know the users, watch them work, etc. Once you do know those things, you can set up good workflows for them with clear options for the different roles in the organization.

- Use the “shortcut menu” that comes with Drupal7
- [Admin Menu Source](https://drupal.org/project/admin_menu_source) lets different roles have different menus
- [Menu Item Visibility](https://drupal.org/project/menu_item_visibility) module — remember the menus are their interface

<a name="clarity"></a>

Less Confusion
--------------

Admin Themes can help

- [Rubik](https://drupal.org/project/rubik) is less cluttered: 2-column node-edit page, description text on
- [Ember](https://drupal.org/project/ember) is responsive

### Logical Grouping

Group things according to how your content creators think about them, not how you built them. Consider grouping admin menu items into safe vs. risky like WordPress does. Bury advanced and less-frequently used functionality.

- Fields into fieldsets &amp; field collections
- Admin Menus for content creators
- Permissions into Roles
- WYSIWYG Icons

Default to expanded for highly recommended options, collapse for optional, and hide anything that is unnecessary.

- Use [conditional fields](https://drupal.org/project/Conditional_Fields) (never show someone an option that does nothing
- [Simplify](https://drupal.org/project/simplify) hides fields
- [Jammer](https://drupal.org/project/jammer) hide many other things)
- [Hide Submit Button](https://drupal.org/project/hide_submit) avoids double submissions and just an importantly communicates to the creator or editor that the site is actually doing something
- Preview Button (see above)

### Streamline Workflows

- Use [Chosen](https://drupal.org/project/chosen) instead of the default multi-select
- [Add Another](https://drupal.org/project/addanother) is great for repetitive node creation.

### Dashboard

There are lots of great dashboard modules. Consider what your creator or editor wants to see the most — make that their default homepage.

**“the best tool of them all… …is the one that works best for your users”**   
It looks like I’ll still have to do quite a bit of experimentation, since Bryan often points to multiple modules to solve the same challenge — still a great reference to address common concerns and highlight best practices.