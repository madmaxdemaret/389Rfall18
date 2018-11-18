Writeup 10 - Crypto II
=====

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 10 Writeup

### Part 1 (70 Pts)

The first part of this lab asked us to perform a hash length extension attack on a digital notary using MD5 hashing to check the integrity of messages. This notary would take a message, give you the hash of the secret+message, then retain that hash. When checking data, the notary would add the data to the current state of the md5 hashing algorithm, hash it, and compare with the hash we gave it.

To execute this attack, I needed to take the results of the original hash given as a result of hashing secret+message. I could then instance an md5 hash (here given by the file md5py.py) with the result hash, giving me the same state as the notary. Adding the malicious message and updating the md5 hashing algorithm gives the hash that the notary will get.

Now all that was left was to craft the fake message. I know the begging of the message is secret+original_message. Following that is \x80 and enough \x00 to fill up 56 bytes. Following that is 8 bytes of the size of secret+message in little endian form. We were given that the secret is between 6 and 15 bytes long, so I wrote some code to calculate the necessary number of \x00's required. For some reason, the code I wrote to calculate the correct length of secret+message in hex added a second backslash, which did not work with the notary, so I calculated the size of the message in hex by hand. 

Adding together the message, padding, size, and my malicious messsage gave me the necessary string. All that was left was to send the calculated hash and string to the notary verification to "break" the notary. Upon doing this, I obtained a flag.

My message was "hello", my malicious message was "oh so evil", by brute force I found the length of secret to be 9, the given hash of "hello" was "e9dd3a6532310f8e1381dfdeabf4d47c" and the crafted hash adding my malicious message was "5219c1c1e1a4f906a09c331aa1125d12"

The payload sent was the following:
hello\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00oh so evil

Sending all of that granted me the following flag:
CMSC389R-{i_still_put_the_M_between_the_DV}

### Part 2 (30 Pts)

One can generate pgp keys with the command line tool gpg. To generate a key, one can run the command "gpg --gen-key". It requires a name and email to make an account, then a password to protect your keys.

To import someone elses key, one runs the command "gpg --import (key_name)". This requires you to download your friends key, but then gpg will save the key.

To encrypt a message with your friends key, one would run the command "gpg --output (doc_name) --encrypt -r person@email.com name_of_file_to_encrypt"


