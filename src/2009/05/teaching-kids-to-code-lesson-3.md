---
title: 'teaching kids to code: lesson #3'
date: '2009-05-31T00:10:10-07:00'
status: publish
exported_permalink: /2009/05/teaching-kids-to-code-lesson-3
author: sarah
excerpt: ''
type: post
id: 1425
category:
    - general
tag: []
post_format: []
---
On the third (and final) class in my series of teaching Shoes and Ruby to 4th/5th graders, I decided to teach them to create a game. I met with my two fifth grade helpers the afternoon before the day of the class. I taught them how to create text and buttons and add a click method and showed them the Shoes manual, then let them experiment. This was a good experience for them, but we ended the day with a more complicated program than I felt we could do with the class and it incorporated internet images which wouldn’t work in the classroom since Internet connectivity isn’t working right now. I also ended up getting beyond my Shoes experience and had to ask help of the Shoes list. After some help from some kind souls, this was the app the kids wrote:

```
class OurApp < Shoes
 url '/',  :index

 def index
   clear
   para "Which is correct?"
   stack {
     @correct = button "A bed of clams"
     @wrong1 =button "A coalition of cheetahs"
     @wrong2 =button "A gulp of swallows"
   }

   @correct.click {
     clear
     para "Correct"
     image "http://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Balloons-aj.svg/550px-Balloons-aj.svg.png"
     button "Go Back" do
       visit "/"
     end

   }
   @wrong1.click {
     clear
     para "Wrong!"
     image "http://icanhascheezburger.files.wordpress.com/2007/05/cheez_doing_it_wrong.jpg"
     button "Go Back" do
       visit "/"
     end
   }
   @wrong2.click {
     clear
     para "Wrong, your consolation prize is..."
     image "http://farm2.static.flickr.com/1166/1230713908_083d7f6c53_o.jpg",
     :width => 500
     button "Go Back" do
       visit "/"
     end
   }

 end  # this is the end of the index method, which lays out the "/" page

end # this is the end of the subclass, which contains all the pages (well, one page)

Shoes.app
```

I ended up teaching the class a much more simplified version. I think the initial session with two students worked well as a great approach to developing a lesson plan. I improved it even more in my live coding session where I built up the app in stages (with compile and demo between each of the steps below):

1. Shoes app with para “Which is correct?”
2. Add three buttons
3. Add stack around the buttons
4. Move the app into Game subclass, show that it has the same behavior
5. Add ‘/correct’ url, button click action, and show\_correct method
6. Add ‘/wrong’ url, button click action, and show\_correct method

Then a student asked how to ask another question if after someone got the right answer. I just made another url and added a button with a visit action to the show\_correct method.

After the demonstration, I gave them a copy of the program for reference and told them *not* to copy it — they had to come up with their own questions and answers. Of course, then they typed in the whole program verbatim only substituting different editorial and ended up with dozens of syntax errors. I wish I had instructed them to do it just like I had and build up their app in several steps, and I did tell them to do that, after they started, but at first they were somehow convinced that all they needed to do was type it in to complete the assignment. Another approach would be to get them to follow along with me and get the whole class to complete each step before moving on the the next; however, once they have their hands on the keyboard it is really hard to get their attention. I also forgot to accidentally on-purpose type things wrong and demonstrate debugging. In any case, the students were engaged and reported having fun, even if most did not finish the game.

Here’s my revised version of the app (improvements were to name the url and the method differently to make it clear that they were different things and to create just one “wrong” url and method to show reusing a method).

```

class Game < Shoes
  url '/',  :index
  url '/correct',  :show_correct
  url '/wrong',  :show_wrong

  def index
    clear
    para "Which is correct?"
    stack { 
      @correct = button "A bed of clams" do
        visit "/correct" 
      end 

      @wrong1 =button "A coalition of cheetahs" do
        visit "/wrong" 
      end

      @wrong2 =button "A gulp of swallows"  do
        visit "/wrong" 
      end
    }
  end  # this is the end of the index method, which lays out the "/" page
   
  def show_correct
    para "Correct"
  end  # of the "correct" method, which lays out the "/correct" page
    
  def show_wrong
    para "Sorry, try again."
  end  # of the "wrong" method, which lays out the "/wrong2" page

end # this is the end of the "Game" subclass, which contains all pages

Shoes.app 

```