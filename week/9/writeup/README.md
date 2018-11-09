Writeup 9 - Crypto I
=====

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 9 Writeup

### Part 1 (60 Pts)

For the first part, we were given a list of 4 sha512 passwords, salted with a single pre-pended lowercase letter. We were also given the begining of the code in stub1.py. I edited stub1.py to get all of the hashes in the hashes file, and store them in an array. I then wrote a loop to get all basic passwords from the given password list, concatenating it and the character, and sha512 hashing that combination. I then check if the resulting hash is in the list of the given hashes, and if it is I print it out.

This part was particuarly tricky with file input. The first time I tried looping over the base passwords file I did not reset the file pointer, so it was only able to check appending a. Then I had trouble with newlines, I was including newlines in both reading the base passwords and in reading the given hashes. With the newlines, nothing matched up, so I had to get rid of them for my program to work.

The given passwords and salts, in the order of the given hashes, are:

k + neptune
p + pizza
u + loveyou
m + jordan

### Part 2 (40 Pts)

For this part we were instructed to nc onto 142.93.117.193 on port 7331, and we were given the start of part2.py to get us started. Upon nc onto the service, I found that the program asked for a specific hash of a specific string. Going through manually, I saw it always asked in the form of "Find me the [hashing_algorithm] hash of [string]". Thus, I had the idea to encode that into a regex expression and match the input to get the hashing_algorithm and the string. I then wrote the function get_hash that takes the algorithm and string and returns the correct hash in hexdigest. I send that the the server and repeat the process. If something goes wrong, I print out the input and exit. After several runs to find all the algorithms they were asking for, I finally reached the end and got the flag, which is:

CMSC389R-{H4sh-5l!ngInG-h@sH3r}
