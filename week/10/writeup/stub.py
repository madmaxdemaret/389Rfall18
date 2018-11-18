#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import re
import time

hash_re = re.compile(r"Your hash: ([a-z0-9]+)")
message = 'hello' # original message here
m = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("142.93.118.186", 1234))

data = s.recv(1024)
print(data)

s.send("1\n")

data = s.recv(1024)
print(data)

s.send(message + '\n')

data = s.recv(1024)
print(data)

m = hash_re.search(data)
legit = m.group(1)                # the legit hash of secret + message
print(legit)
# we need the legit hash to perform our attack

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'oh so evil'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long, 64 bytes
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

#(6-15) + ('hello' length = 6) = 12-21 length of secret+hello 
#12-21 bytes long

# so we have 64-length of secret+hello padding
# which is 52 - 43 bytes left

#8 of those bytes at the end are for the message length, which will be:
# \x60 + 7*\x00 to \xA8 + 7*\x00

#so minus length, we have 44-35 bytes left, which would be \x10 followed by 43-34 bytes of \x00 padding

secret_size=9
size_of_secrethello = '\x78'

secrethello_len = secret_size+6

padding_left = 64-secrethello_len-8-1

padding = '\x80' + (padding_left*'\x00') + size_of_secrethello  + (7*'\x00')

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
payload = message + padding + malicious

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

print(repr(payload))


data = s.recv(1024)
print(data)

s.send("2\n")
data = s.recv(1024)
print(data)


s.send(fake_hash + '\n')
data = s.recv(1024)
print(data)


s.send(payload + '\n')
data = s.recv(1024)
print(data)

data = s.recv(1024)
print(data)
