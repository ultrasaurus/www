---
title: 'debugging objective-c in xcode for iOS'
date: '2011-11-02T06:40:59-07:00'
status: publish
permalink: /2011/11/debugging-objective-c-in-xcode-for-ios
author: sarah
excerpt: ''
type: post
id: 3428
category:
    - general
tag: []
post_format: []
---
I’m coding again in native Objective-C coding for iOS with the lovely XCode. It has been a while so I’ve been reading up on debugging tricks. Sadly, it still feels a bit like debugging in Macsbug in 1990…

The graphical display of object values is fairly useless, but in gdb, we can use the **po** command to get a pretty printing of the object if it comes with a built in description (for details see [nice writeup from cocoa with love](http://cocoawithlove.com/2008/10/debugging-tips-for-objective-c.html)).

For our own objects, we can define a debugDescription method. For example, if I have a Thing class which is a subclass of NSObject and just has a title and subtitle:

> ```
> @implementation Thing
> 
> @synthesize title;
> @synthesize subtitle;
> 
> - (NSString *)debugDescription { return [NSString stringWithFormat:@"title: %@n subtitle: %@", title, subtitle]; }
> 
> @end
> ```

Then if I find myself at a breakpoint with an instance of Thing in scope, called “thing”:

> ```
> (gdb) po thing
> title: Another
> subtitle: Another example
> ```

Or if I have an array of Thing instances, called “things”:

> ```
> (gdb) po things
> <__NSArrayM 0x6a157a0>(
> title: Basic
> subtitle: My Thing,
> title: Something
> subtitle: Example of something,
> title: Another
> subtitle: Another example
> )
> ```

[iphonedevelopertips illustrates](http://iphonedevelopertips.com/cocoa/overriding-nsobject-description-method.html) this nicely in more detail with the description method which will do the same thing for any subclass of NSObject.

**Note:** `print-object` actually calls the `debugDescription` method of the specified object. `NSObject` implements this method by calling through to the `description` method. Thus, by default, an object’s debug description is the same as its description. However, you can override `debugDescription` if you want to decouple these; many Cocoa objects do this. (via [Apple Tech Note 2124](http://developer.apple.com/library/mac/#technotes/tn2124/_index.html))

Update: LLVM Debugger sucks less
--------------------------------

If you [choose the LLVM Debugger](http://developer.apple.com/library/mac/#documentation/IDEs/Conceptual/Xcode4TransitionGuide/Debugging/Debugging.html), instead of gdb, you can see properties on an object without defining a description or debugDescription method:

> ```
> 
> (lldb) po thing
> (Thing *) $8 = 0x06a487d0 
> (lldb) po thing.title
> (NSString *) $9 = 0x00005984 Another
> (lldb) po thing.subtitle
> (NSString *) $10 = 0x00005994 Another example
> ```

…but still no love for Arrays:

> ```
> 
> (lldb) po things
> (NSMutableArray *) $11 = 0x06a0b6a0 (
> ,
> ,
> 
> )
> ```

…just for fun, let’s see how to look at a property of the first object in an array:

> ```
> 
> (lldb) po [things objectAtIndex:0]
> (id) $12 = 0x06a44d20 
> (lldb) po [things objectAtIndex:0].title
> error: warning: instance method '-objectAtIndex:' not found (return type defaults to 'id')
> error: property 'title' not found on object of type 'id'
> error: 1 errors parsing expression
> (lldb) po (Thing*)[things objectAtIndex:0].title
> error: warning: instance method '-objectAtIndex:' not found (return type defaults to 'id')
> error: property 'title' not found on object of type 'id'
> error: 1 errors parsing expression
> (lldb) po ((Thing*)[things objectAtIndex:0]).title
> (NSString *) $14 = 0x00005944 Basic
> (lldb) po [[things objectAtIndex:0] valueForKey:@"title"]
> (id) $15 = 0x00005944 Basic
> ```

Whew!