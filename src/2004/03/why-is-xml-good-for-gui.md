---
title: 'why is XML good for GUI?'
date: '2004-03-25T16:55:51-08:00'
status: publish
exported_permalink: /2004/03/why-is-xml-good-for-gui
author: sarah
excerpt: ''
type: post
id: 110
category:
    - Uncategorized
tag: []
post_format: []
---
[Dan Shafer](http://www.eclecticity.com/.3c3f16d4) asks a very good question about Laszlo:

“Instead of direct manipulation of graphical objects to create pleasing interfaces, i get to write XML code (with its extreme overhead burden) to describe how I want the graphical experience to look and feel. And that’s a good thing because…???”

I agree that it is counter-intuitive that XML would be a good format for developing graphical user interfaces. I always felt that XML made a mighty fine interchange format — it’s human-readable, almost self-doumenting, and these days if you are working on a large software development project you probably have at least one or two XML parsers already linked in. So… why use it for developing applications?

There are a few attributes of graphical user interfaces that map well to XML:

**Graphical user interfaces are inherently hierarchical**  
Screen real-estate is naturally divided heirarchically. It is convenient for that heirarchy to be represented by the development environment.

**Graphical user interfaces evolve**  
While a hierarchy could be effectively represented in a visual tool, arguably more effectively than it is in an XML file, it is the managing the evolution of a application where XML really comes in handy. It is natural for a design to change over time. In response to user feedback, bugs, or simply by realization of the author, an application needs new features, gestures, or an altered composition. When your design is caught in a visual tool with an opaque file format, you lose the magic of a diff. What happened between then and now?

**Graphical user interfaces are often built by a team**  
XML files are simple text files. Media files live separately and can be linked in by name. Designers and coders can work together on separate pieces of an application without the need for complex group-ware solutions. Coders use the tools they are used to for editing and archiving files. Designers can use the tools they are used to for creating and editing art assets and media files.

**Graphical user interfaces require structure**  
Graphical user interfaces need to be split into pieces to be manageable. XML provides a structured framework which makes its fairly easy to divide your work into bite-sized chunks. A common problem in a visual tool is that people “lose” things. It may be hard to figure out what object a script is attached to. An object that is invisible can be hard to discover or manipulate. In a system where all objects and code are encapsulated in simple text files, anything can be found. The inherent structure of an XML file helps organize an application. There are lots of visual tools that offer a tree-view of XML files which make this structure more approachable.

As an aside, for Dan who “still doesn’t get Laszlo,” there’s a whole lot more to Laszlo than XML. What makes Laszlo cool is its constraints system, animation geared to UI design, client-server data model, effective class re-factoring, and more.

Someday there’ll be a GUI tool for creating and editing Laszlo applications. Let’s face it: typing in pixel coordinates and RGB values is no fun. Ideally there would be a layout tool that directly created and edited LZX files. Most folks at Laszlo design in Illustrator or whatever and transfer pixel and RGB values to the XML files. By the way, this is often what folks do when building UI for desktop apps.