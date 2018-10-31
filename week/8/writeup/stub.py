#!/usr/bin/env python2
from __future__ import print_function
import sys
import struct
from datetime import datetime
import array

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_string(s):
    if not is_ascii(s):
        return False

    zero = False

    for i, c in enumerate(s):
        if ord(c) == 0:
            print("index at first 0: %d" % i)
            print("rest of string: %s" % s[i:])
            return all(ord(c) == 0 for c in s[i:])
    return True










# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

time1 = int(struct.unpack("<L", data[8:12])[0])
print("TIME: %s" % datetime.fromtimestamp(float(time1)))


auth_name = data[12:20]
if not is_string(auth_name):
    bork("Author name is not a valid string")
print("AUTHOR: %s" % str(auth_name))


section_count = int(struct.unpack("<L", data[20:24])[0])
if section_count <= 0:
    bork("Section count must be greater than 0, count is %d" % section_count)
print("SECTION_COUNT: %d" % section_count)

print("-------  BODY  -------")

offset = 24
nsects = 0


while offset < len(data):
    
    nsects+=1
    print("At offset %s, currently on section %d" % (hex(offset), nsects))

    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    offset+=8

    if stype == 0x1:
        #png

        print("Section type: png, section length: %d" % slen)

        if offset+slen > len(data):
            bork("Ran out of file data parsing png")


        filename = "png_at_" + str(offset) + ".png"
        f = open(filename, "w+")
        f.write("\211PNG\r\n\032\n")
        f.write(data[offset:offset+slen])
        f.close

        print("File " + filename + " created\n")

        offset+=slen


    elif stype == 0x2:
        #array of dwords

        print("Array of dwords with %d dwords and total length %d" % (slen/8,slen))

        if offset+slen > len(data):
            bork("ran out of file data parsing arrays of dwords")
        if slen%8!=0:
            bork("array of dwords has extra data")

        dwords = []
        for i in range(0, slen/8):
            dwords.append(struct.unpack("<Q", data[offset:offset+8])[0])
            offset += 8

        print("[", end='')
        for i in range(0, slen/8-1):
            print(str(dwords[i]) + ", ", end='')
        print(str(dwords[slen/8-1]) + "]")


    elif stype == 0x3:
        #UTF-8 encoded text

        print("UTF-8 encoded text with length %d" % slen)
        if offset+slen > len(data):
            bork("ran out of file data parsing utf 8 text")
        uni_text = data[offset:offset+slen]
        offset += slen

        print(uni_text.decode("utf-8"))

    elif stype == 0x4:
        #array of doubles

        print("Array of doubles with %d doubles and %d total length" % (slen/8, slen))

        if offset+slen > len(data):
            bork("ran out of file data parsing arrays of doubles")
        if slen%8!=0:
            bork("array of doubles has extra data")

        doubles = []
        for i in range(0, slen/8):
            doubles.append(struct.unpack("<d", data[offset:offset+8]))
            offset+=8

        print("[", end='')
        for i in range(0, slen/8-1):
            print(str(doubles[i]) + ", ", end='')
        print(str(doubles[i]-1) + "]")

    elif stype == 0x5:
        #array of words

        print("Array of words with %d words and %d total length" % (slen/4, slen))

        if offset+slen > len(data):
            bork("ran out of memory parsing arrays of words")
        if slen%4!=0:
            bork("arrays of words has extra data")

        words = array.array('L', [])
        for i in range(0, slen/4):
            words.append(struct.unpack("<L", data[offset:offset+4])[0])
            offset+=4

        print("[", end="")
        for i in range(0, slen/4-1):
            print(str(words[i]) + ", ", end="")
        print(str(words[slen/4-1]) + "]\n")


    elif stype == 0x6:
        #latitude longitude tuple of doubles

        if offset+16 > len(data):
            bork("ran out of file space for latitude longitude")

        if slen != 16:
            bork("Latitude Longitude section has different length than 16, got %d" % slen)

        latitude, longitude = struct.unpack("<dd", data[offset:offset+16])
        offset+=16

        print("Lat: %f\nLong: %f\n" % (latitude, longitude))

    elif stype == 0x7:
        #index of another section

        if offset+4 > len(data):
            bork("ran out of file space for section_reference")

        if slen != 4:
            bork("index of section has length %d, not 4" % slen)

        index = int(struct.unpack("<L", data[offset:offset+4])[0])
        offset+=4

        if index < 0 or index > section_count-1:
            bork("Invalid option for section_reference, got %d but expected between 0 and %d" % index % section_count-1)

        print("Section_Reference, referencing %d\n" % index)

    elif stype == 0x9:
        #ascii

        if offset+slen > len(data):
            bork("ran out of file space for ascii text")

        print("ASCII text, with length %d" % slen)

        print(data[offset:offset+slen] + "\n")
        offset+=slen

    else:
        bork("Section type not matched, expected 0x1-0x7 or 0x9, got: %s" % format(stype, '02x'))


print("Actual number of sections: %d" % nsects)
