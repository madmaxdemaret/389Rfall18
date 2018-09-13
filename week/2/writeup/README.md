Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. Lives in Silver Spring, MD. Born in 1990 (Both from twitter)

Accounts:
twitter: (@KRUEGSTER1990), set up August 12, 2018. Only following and being followed by UMD CYBERSEC club. Discovered by google searching "kruegster1990", which popped up the following page on the umdcsec sTwity page.

Reddit: (kruegster1990), set up August 13, 2018, has verified email. Also popped up with google search of "kruegster1990".

Cornerstone Airlines: Owner, email address kruegster1990@tutanota.com. Found via a link he has on his twitter page. You guys put unprecetended security on the homepage, not sure if that is a typo or not.

I noticed using checkusernames.com that there was a linkedin with that username but I couldn't find it.

He also has an instagram account, username kruegster1990, which I found using inteltechniques.com. Here he has three pictures of a first class ticket from cornerstoneairlines.co.


Picture: By doing a reverse image search on the image used for Fred Krueger's twitter picture, I found that the dude is actually Sean Mayday (April Fools though) method.com/blog/article/2018/04/faa-announces-new-atcfad-program/

3. Passive DNS replication in VirusTotal resolved cornerstoneairlines.co to 142.93.118.186

4. One in the source of the home page, CMSC389R-{h1dden_fl4g_in_s0urce}
One in cornerstoneairlines.co/secret/ (found using robots.txt), CMSC389R-{fly_th3_sk1es_w1th_u5}

5. Other associated ip addresses were 142.93.117.193, which was the admin page for cornerstone. Using dnsdumpster, I found the ip addresses of the DNS Servers, 216.87.155.33 and 216.87.152.33. Also on dnsdumpster, I found the IP addresses of the MX Records, 162.255.118.62, and 162.255.118.61.

6. The DNS servers and MX Record servers are all hosted in the US. I got conflicting information as to where the main page server was located, dnsdump put it somewhere in Canada but viewdns.info put it in New York.

7. Putting both the cornerstoneairlines.co and http://142.93.117.193 into mxtoolbox's dns lookup showed the servers were running Apache/2.4.18

8. *(BONUS)*

Using dnsdumpster, I found CMSC389R-{dns-txt-rec0rd-ftw}

Using url fuzzing, I was able to find cornerstoneairlines.co/.git/, and looking through the files I found COMMIT_EDITMSG, which gave the flag CMSC389R-{y0u_found_th3_g1t_repo}

### Part 2 (55 pts)

Using the provided python stub, I guessed the username to be kruegster, based on his email address associated with the website. Based on an nmap of the admin IP address, I saw that port 1337 (leet) was open, which was obviously the port to attack. This was furthur confirmed when I nc into port 1337 and was faced with a login prompt. I completed the stub program and ran it, which then returned the password pokemon. Once inside the server, I navigated to the home directory and saw the folder flight_records, which was what question 2 was asking for. 

In regard to the specific flight flag we needed to submit, I found the correct one on his instagram account. That flight number was AAC27670, and the corresponding flag for that flight record was CMSC389R-{c0rn3rstone-air-27670}.
