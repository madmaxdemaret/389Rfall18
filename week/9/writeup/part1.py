#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

hashes = []
with open("../hashes") as f:
    for line in f:
        hashes.append(line.rstrip('\n'))

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    with open("../probable-v2-top1575.txt", 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            temp = hashlib.sha512(salt+line).hexdigest()
            if temp in hashes:
                print("Hash %s given by salt %s and password %s" % (temp, salt, line))
