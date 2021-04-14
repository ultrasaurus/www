---
title: 'xcode playground for parse in swift'
date: '2016-01-02T23:46:40-08:00'
status: publish
exported_permalink: /2016/01/xcode-playground-for-parse-in-swift
author: sarah
excerpt: ''
type: post
id: 5797
category:
    - code
tag: []
post_format: []
---
Xcode playgrounds are a delightful way to explore the Swift language — once you get them set up. I admit that I’ve grown to love environments where I can code with simple text files, however, I also love to develop iOS apps and so I find myself digging once again thru the byzantine Xcode GUI. It seems I always forget the magic incantations!

Here are the notes for my future self and other intrepid explorers:

Experimenting with [Parse.com](https://www.parse.com/) in Swift 2, Xcode 7.2, OSX 10.10.5 (Yosemite)

note: cocoapods 0.39.0 has issue with Ruby 2.3 (https://github.com/CocoaPods/CocoaPods/issues/4345) — likely fixed in the 1.0 beta, but I stuck with older ruby and released cocoapod for this exercise.

`rvm use ruby-2.2.4<br></br>gem install cocoapods<br></br>`

Make a new Xcode project, and add a new Empty file to your project called Podfile (New &gt; File… &gt; Other &gt; Empty), with the following contents:

`platform :ios, '8.1'<br></br>xcodeproj 'ParsePlayground'<br></br> <br></br>use_frameworks!<br></br>target :ParsePlayground, :exclusive => true do<br></br>  pod 'Parse'<br></br>end<br></br>`

back on the command-line:

`pod install`

This creates a new Xcode workspace, so we need to close the project in Xcode, then re-open Xcode with the file named something ending in .xcworkspace.

This new workspace should have both the original project and a new one called Pods. Now we can create the Playground, by selecting the menu: File &gt; New &gt; Playground… Then we save it in the root of our project directory, then add it to the project with the menu: File &gt; Add Files To “ParsePlayground”

Now this code should compile:

`import Parse<br></br>import XCPlayground<br></br>XCPlaygroundPage.currentPage.needsIndefiniteExecution = true<br></br>`

We want to set needsIndefiniteExecution so that the async commands will work.

I made a new Parse app to experiment, then in the parse docs, in the [QuickStart Guide](https://parse.com/apps/quickstart#parse_data/mobile/ios/swift/new), they set up some sample code already customized with the app ID and client key, it should be something like:

`Parse.setApplicationId("abunchofnumbersandletters",<br></br>      clientKey: "morelettersandnumbers")<br></br>`

Then we can start coding! I made an item class in Parse with a string property “info.” Here some code that worked for me:

`let testObject = PFObject(className: "TestObject")<br></br> <br></br>testObject["foo"] = "bar"<br></br>testObject.saveInBackgroundWithBlock { (success: Bool, error: NSError?) -> Void in<br></br>  print("Object has been saved: (success)")<br></br>}<br></br> <br></br>var query = PFQuery(className: "item")<br></br>var items = try query.findObjects()<br></br>print("got some items")<br></br>for item in items {<br></br>  var info = item["info"]<br></br>  print("   item #(item.objectId!) info:(info)")<br></br>}<br></br> <br></br>print("not the end... wait for the sync call to finish")<br></br>`

When I run the above code it works fine, but I do get some of the following errors. Not sure why…

`Failed to obtain sandbox extension for path=/var/folders/hz/vnvkxt7x4236fp6nqt5zy2wr0000gn/T/com.apple.dt.Xcode.pg/containers/com.apple.dt.playground.stub.iOS_Simulator.experiment-3C8D4B75-8EA0-4BE8-8467-1B06C9B1F881/Library/Caches`

I’ve posted the full [ParsePlayground project ](https://github.com/ultrasaurus/ParsePlayground)on Github with some notes on how to set up the Parse app if you want to jump right in!