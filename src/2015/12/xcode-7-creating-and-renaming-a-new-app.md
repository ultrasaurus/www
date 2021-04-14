---
title: 'xcode 7: creating and renaming a new app'
date: '2015-12-22T06:52:40-08:00'
status: publish
exported_permalink: /2015/12/xcode-7-creating-and-renaming-a-new-app
author: sarah
excerpt: ''
type: post
id: 5754
category:
    - code
tag: []
post_format: []
---
Create a new application (File &gt; New &gt; Project)

Create a Single View Application as usual…

<figure class="wp-caption thumbnail aligncenter" id="attachment_5755" style="width: 734px;">[![dialog box with 'Single View Application' selected](../../../uploads/2015/12/Screen-Shot-2015-12-22-at-6.07.37-AM.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/Screen-Shot-2015-12-22-at-6.07.37-AM.png) <figcaption class="wp-caption-text">Create a Single View Application</figcaption></figure>Name your project:

[![XCode New Project Dialog box](../../../uploads/2015/12/Screen-Shot-2015-12-22-at-6.12.22-AM.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/Screen-Shot-2015-12-22-at-6.12.22-AM.png)

Fill in project name, organization name, identifier (like com.yourcompany) and for now, unchecking unit tests. I’m experimenting with a new Mightyverse prototype so I filled in:  
\* PhraseRecorder  
\* Mightyverse  
\* com.mightyverse

which created the app identifier: com.mightyverse.PhraseRecorder

It will also create a folder full of files named with your project name and this will also be the name of the app. I don’t like spaces in file paths, so I use camel case with no spaces.

Run the app now and you should see a blank white screen. I usually use iPhone 5 since the screen is small and easy to preview on my laptop. Let’s go to the home screen and see how the project name is used as the app name. (Choose Hardware &gt; Home or shift-command-H)

[![multiple icons on home screen, new app has truncated name followed by an elipsis](../../../uploads/2015/12/Screen-Shot-2015-12-22-at-7.04.47-AM.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/Screen-Shot-2015-12-22-at-7.04.47-AM.png)

The name I picked was too long so it appears truncated with elipses. This wasn’t the name I wanted the end user to see anyhow. This is easy to fix in XCode 7 (though not very discoverable). Stop the app (using the VCR controls at the top of the XCode window). Then click the little folder icon to see your file listing, then double click on the target name in the middle panel and type a new name.

[![First item selected in first panel, target in second](../../../uploads/2015/12/Screen-Shot-2015-12-22-at-7.07.33-AM.png)](https://www.ultrasaurus.com/wp-content/uploads/2015/12/Screen-Shot-2015-12-22-at-7.07.33-AM.png)

Run the app again and… voila! your app has a new name.