---
title: 'setting up ec2 minecraft server'
date: '2011-11-24T19:08:54-08:00'
status: publish
permalink: /2011/11/setting-up-ec2-minecraft-server
author: sarah
excerpt: ''
type: post
id: 3464
category:
    - general
tag: []
post_format: []
---
Goal: set up a minecraft server using free EC2 account from OSX  
\[update: FAIL — game play doesn’t work on a micro instance, if we want to use EC2 it looks like we need to use at least a small one. so be careful to adjust the steps below to pick a small instance if you want to play.\]

I learned that there are a lot of minecraft server implementations. I decided to use Craftbukkit server largely because I saw it referenced from a [RubyConf talk](http://confreaks.net/videos/696-rubyconf2011-be-a-minecraft-modman-with-purugin) by [Tom Enebo](http://blog.enebo.com/) — might be fun to mod it someday :)

I pieced together information from some helpful tutorials from [Ubuntu](https://help.ubuntu.com/community/EC2StartersGuide) and [Robert Sosinski](http://www.robertsosinski.com/2008/01/26/starting-amazon-ec2-with-mac-os-x/).

1. Sign-up for an AWS account (1 year free for new AWS accounts, but you need a credit card)
2. Go to [AWS Management Console](https://console.aws.amazon.com/ec2/home)
3. Create a Private Key 
  - Select EC2 tab, click on “0 Key Pairs” on the right side
  - name it ec2.pem (or anything you want, but I’ll use ec2 in the rest of this tutorial)
  - save it to ~/.ec2/ec2.pem
4. Create a Certificate 
  - Under your name in the top right corner, select “Security Credentials”
  - Download the private key and certificate and save them in ~/.ec2
5. Make your credential files private. In your local terminal, type: 
  - cd ~/.ec2
  - chmod go-rwx ~/.ec2/\*.pem
6. Download [EC2 API Tools](http://aws.amazon.com/developertools/351)
  - Unzip the Amazon EC2 Command-Line Tools
  - Move both the bin and lib directory into your ~/.ec2 directory
7. Your ~/.ec2 directory should have: 
  - The cert-xxxxxxx.pem file
  - The pk-xxxxxxx.pem file
  - The bin directory
  - The lib directory
  - ec2.pem
8. Set up EC2 Command-line Tools 
  - Put the following into your ~/.bash\_profile:  
      `# Setup Amazon EC2 Command-Line Tools<br></br>export EC2_HOME=~/.ec2<br></br>export PATH=$PATH:$EC2_HOME/bin<br></br>export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`<br></br>export EC2_CERT=`ls $EC2_HOME/cert-*.pem`<br></br>export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Home/`
  - On the command-line, type:  
      `source ~/.bash_profile`
9. Startup a server 
  - \[Update\] We want to be careful to choose an AMI that works with the micro instance, which is what we get for free. Ubuntu takes up too much disk space by default to fit into a micro instance, so you need to use one of the [micro Ubuntu AMIs](http://cloud.ubuntu.com/2010/11/using-ubuntu-images-on-aws-free-tier/) they created for this purpose. I’m going to use Maverick 10-10 — it’s the most recent version that has a micro version.
  - \[Update\] I picked one in us-east, since that’s where Amazon started my account by default and it seems that it needs to be in the same region matching the one set for my key:  
      ec2-run-instances ami-cf33fea6 –instance-type t1.micro –region us-east-1 –key ec2
  - check to see if it is running, by typing:  
      `ec2-describe-instances`
  - make a note of your hostname! It should look something like:
  
  ```
  ec2-###-##-##-##.compute-1.amazonaws.com
  ```
10. Open relevant ports (22 for ssh, 80 for http, 25565 for minecraft):`<br></br>ec2-authorize default -p 22<br></br>ec2-authorize default -p 80<br></br>ec2-authorize default -p 25565<br></br>`
11. ssh into your new instance  
  `ssh -i ec2.pem ubuntu@ec2-###-##-##-##.compute-1.amazonaws.com`
12. Install Java ([nice Ubuntu instructions](http://ubuntu-for-humans.blogspot.com/2011/04/installing-java-on-ubuntu-server-1010.html))  
  Note: to accept the license, use tab to get to the OK “button” then hit return, then arrow to get to “Yes” and hit return again.  
  To verify installation:  
  $ java -version  
  java version “1.6.0\_26”  
  Java(TM) SE Runtime Environment (build 1.6.0\_26-b03)  
  Java HotSpot(TM) Client VM (build 20.1-b02, mixed mode, sharing)
13. See [this tutorial for setting up minecraft](http://wiki.bukkit.org/Setting_up_a_remote_Linux_server), but if you are playing with the Minecraft 1.0 client (at least of today) you’ll need to install a dev build which you can find on the [ci server](http://ci.bukkit.org/job/dev-CraftBukkit/). I found that I needed to run the server, stop it and run it again to get it to start without errors. 
  - get the latest dev build (I’m running 1502): ```
      
      wget http://ci.bukkit.org/job/dev-CraftBukkit/lastSuccessfulBuild/artifact/target/craftbukkit-1.0.0-SNAPSHOT.jar
      ```
  - create a file called “start.sh” with the following contents: ```
      
      #!/bin/sh
      java -Xmx613M -Xincgc -jar craftbukkit-1.0.0-SNAPSHOT.jar
      ```
  - run the server in screen: ```
      
      screen
      ./start.sh
      ```

\[Update\] By tweaking the memory allocation, we can get it to work (most of the time) with a single player. I found that I can raise the memory allocation for java and use virtual memory, but that it sometimes maxes out the CPU.

Here’s the setting where the game couldn’t be failed (couldn’t fight monsters or build things):

```
#!/bin/sh
java -Xmx613M -Xincgc -jar craftbukkit-1.0.0-SNAPSHOT.jar

$top
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                                                 
 1642 ubuntu    20   0  978m 300m  10m S 12.3 50.7 100:44.96 java                                                                     
```

Note:  
VIRT – 978M of virtual memory  
RES – 300m resident (physical) memory

- - - - - -

With this it sometimes works:

```

#!/bin/sh
java -Xmx1024M -Xincgc -jar craftbukkit-1.0.0-SNAPSHOT.jar

 2829 ubuntu    20   0 1336m 271m  10m S 14.0 45.8   0:18.76 java                                                                     
```

- - - - - -

With this works almost all the time (but we’ve only tested one player):

```

#!/bin/sh
java -Xmx2048M -Xincgc -jar craftbukkit-1.0.0-SNAPSHOT.jar

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                                                 
 2893 ubuntu    20   0 2499m 341m  10m S 99.8 57.6   0:27.68 java                                                                     

 2893 ubuntu    20   0 2499m 341m  10m S 18.2 57.7   1:27.30 java                     
```

when the CPU maxes out, I see this in the game console:  
`22:39:19 [WARNING] Can't keep up! Did the system time change, or is the server overloaded?`