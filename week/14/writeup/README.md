Writeup 10 - Crypto II
=====

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 10 Writeup

### Part 1 (70 Pts)

First I clicked on the various items and saw the only change to the website address was adding a /item?id=(item id here). Going back to the slides, I saw that they wanted us to leak /etc/password, so I replaced /item?id=1 with /etc/password. This got me to a page saying Sinatra doesn't know this ditty, with a try this code instead. However, I did not think that would work as we had to do SQL injection and not code injection.

Thus, I tried various inputs to mess up the SQL code. To avoid browser problems, I used wget on my virtual machine. Doing sseveral inputs, I realized that inserting "' or '1=1" would get me the entirely of the table "item". This took over an hour, as I had been doing and instead of or for over 45 minutes before I realized that logically that would not work. 

This works by first escaping the id=0 part of the input, then adding a logical or part, then capturing the 1=1 part. By doing this, I can avoid commenting out the rest of the command, which was leading to a server error. 

By getting the entirety of the table, I was able to find the hidden table item, FLAG, whose text has the flag CMSC389R-{y0U-are_the_5ql_n1nja}. It is priceless.

### Part 2 (30 Pts)

I had already done part of this website before as an in class lecture for cmsc330, but I did not remember what I did so I deleted the cookies to allow me to see the challenges again.

The first challenge read straight html, so by inserting <script> alert() </script> I was able to get the website to alert, which brought me to the second challenge.

In the second challenge, I was unable to delete my cookie for some reason, but the challenge is solved by resourcing the image file of the austronaut and adding an alert on the austronaut's showing.

In the third challenge we needed to escape the <img scr> part of the code. To do this, insert .jpg' /> in the end of the url, then add <script>alert()</script> to have it alert and to progress to the next level.

This level was quite challenging. I realized we had to escape the html in the onload part of the loading.gif image. I was able to get various uncaught syntax errors by inserting ');alert();" />, but that did not run. The main challenge in this was commenting out the remaining part of the function, because no matter what I tried it kept throwing syntax errors. Then I realized I did not have to comment out the rest of the function, I simply had to modify my input to accept the rest of the function. Thus I tried ');alert();var x=(', which worked!

By reading the title and description of this challenge, I knew this challenge would not be about breaking out of html code and inserting a <script>alert()</script> somewhere. By reading the hints, I found the line <a href='javascript:doSomething()'>..</a> in the provided ietf paper. In the signup html, I saw a comment that the email did not do anything, so I looked for other variables, which I found in the next variable in the url. By changing next=confirm to next=javascript:alert(), I was able to advance to the next stage.

Based on the description of this problem I searched the code for location.hash, which lead me to the function uncludeGadget(url). This function runs based on our input in the url after frame#. In this function there is a regex match for external links, specifically looking for the http:// part of the link. 

By looking up how to get urls without the https:// part, I found a stack overflow question saying just using // will automatically include the http: part of the url. This effectively get around our regex check, now all I need to do is load a file that alerts the page. Using the hint, I tried running the page with the input //google.com/jsapi?callback=alert();, but it did not run. After googling google's jsapi callback, the first link I found was solutions to this very problem. Because I thought I was close, I looked it up. All I had to do was delete the (); part from my url and it suddenly worked.

