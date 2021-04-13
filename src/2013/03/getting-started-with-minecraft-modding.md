---
title: 'getting started with minecraft modding'
date: '2013-03-31T17:41:11-07:00'
status: publish
permalink: /2013/03/getting-started-with-minecraft-modding
author: sarah
excerpt: ''
type: post
id: 3824
category:
    - code
tag: []
post_format: []
---
I started learning about creating a Minecraft mod today, using this [excellent tutorial](http://www.minecraftforge.net/wiki/Basic_Modding) (thanks [@0x17h](https://twitter.com/0x17h) and [@adudney](https://twitter.com/adudney)).

Background: [Minecraft](https://minecraft.net/) is a very popular world-building game. They announced last November that they will release an API, but they have a friendly attitude toward users who have reverse-engineered how to create “mods” (extensions to the game and changes to the behavior of objects in the world). [Minecraft Forge](http://www.minecraftforge.net/) is the de-facto standard API toolkit for making mods.

We found that the easiest way to run a server is to run it locally on an old MacBook, allowing external connections to connect to a [noip](http://www.noip.com/) domain and tunnel into our home network.

**Prerequisites:**We’re running Mac OSX SnowLeopard. We need Java and the JDK, 1.6 or better.

Check that java is installed

```

$ java -version
java version "1.6.0_37"
```

Check that the JDK is installed

```

$ javac -version
javac 1.6.0_37
```

We installed 64-bit version of Eclipse.

Other than those platform-specific details that I had to look up, we had no problem following the [basic modding tutorial](http://www.minecraftforge.net/wiki/Basic_Modding). The mod doesn’t do anything yet, but we can run minecraft and see it load:

![](https://www.evernote.com/shard/s6/sh/53988b22-69d4-4697-8b20-30e7f972280c/ea226fa8a84f98a14dd5b31981c4e625/res/98cbe8d2-f482-4d89-9466-ad2c34e476cd/skitch.png?resizeSmall&width=832)