Writeup 3 - OSINT II, OpSec and RE
======

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 3 Writeup

### Part 1 (100 pts)

Dear Fred Krueger,

Per your request I have looked at your companies web server and have found at least three areas where you could greatly improve.

First I reccomend you look at your credentials, specifically your username and password. The fact that your username is the same as your email address left it extreamly vunurable for attackers to guess. I would recomend changing it to something harder to guess, such as fred_krueger_admin. Additionally, your password is horrible. "pokemon" is one of the most common passwords people use, and can easaly be bruteforced. It is so common that it comes standard in kali, which is one of the most used tools in hacking. I would recomend changing it to something still recognizable but much harder to bruteforce, such as "Level100pokemonarethebest!". When comparing these passwords using howsecureismypassword.net, "pokemon" would be cracked instantly whereas "Level100pokemonarethebest!" would be cracked in 9 nonillion years.

Secondly, I would look at removing your admin account from your website. The ethical hackers had easy knowladge on where to attack because the IP address of your admin site was a click away from the main page of your website. Customers viewing your website do not need to see an unfinished admin page, and attackers definatly should not get easy access to know where your admin server is. If you removed the link between your website and your server then attackers would not have been able to connect the two and you would have been safe. This would be easy to do, just delete the link to the admin page on the home page and the about page.

Third, I would look into getting a host based intrusion detection system. They can monitor if attackers are scanning your server and block furthur scans from taking place. This would prevent attackers from noticing that you have a log-in on port 1337, and can possibly prevent attackers from trying to bruteforce your password. A free host based intrusion detection system I can recommend for you would be OSSEC. 

By combining these three measures your system will be much more secure against all kind of hackers, ethical or otherwise.
