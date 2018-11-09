#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re


def get_hash(alg, string):
    if alg == "sha224":
        return hashlib.sha224(string).hexdigest()
    elif alg == "sha1":
        return hashlib.sha1(string).hexdigest()
    elif alg == "md5":
        return hashlib.md5(string).hexdigest()
    elif alg == "sha256":
        return hashlib.sha256(string).hexdigest()
    elif alg == "sha384":
        return hashlib.sha384(string).hexdigest()
    elif alg == "sha512":
        return hashlib.sha512(string).hexdigest()
    else:
        return "failure"




hashing_algorithm = re.compile(r"Find me the ([a-z]{2,3}[0-9]+) hash of ([a-zA-Z0-9]+)")

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:

# receive some data
    data = s.recv(1024)
    print(data)

    m = hashing_algorithm.search(data)

    if m == None:
        break

    hashing_alg = m.group(1)
    stringy = m.group(2)

    s.send(get_hash(hashing_alg, stringy) + '\n')
# close the connection
s.close()
