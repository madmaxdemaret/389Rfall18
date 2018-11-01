Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The hackers did use traceroute on websites, going to cornerstoneairlines.co, which has the ip address 142.93.118.186.

2. The hacker's names are laz0rh4x and c0uchpot4doz.

3. c0uchpot4doz's ip address is 206.189.113.189, and laz0rh4x's ip is 104.248.224.85. Geolocating these gives c0uchpot4doz is in london and laz0rh4x is in North Bergen, NJ, USA.

4. They are using port 2749.

5. Their plans are happening tommorow (October 25, 2018) at 1500, or 3 pm.

6. The hackers sent a google drive link: https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

They did mention they needed a parser to read it.

7. They expect to see each other tommorow (October 25, 2018).

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. update.fpff was generated October 24, 2018 at 20:40:07.

2. laz0rh4x authored update.fpff.

3. update.fpff says it has 9 sections, but it really has 11 sections. 

4. At offset 0x18, currently on section 1
ASCII text, with length 51
Call this number to get your flag: (422) 537 - 7946

At offset 0x53, currently on section 2
Array of words with 15 words and 60 total length
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

At offset 0x97, currently on section 3
Lat: 38.991610
Long: -77.027540

At offset 0xaf, currently on section 4
Section_Reference, referencing 1

At offset 0xbb, currently on section 5
ASCII text, with length 60
The imfamous security pr0s at CMSC389R will never find this!

At offset 0xff, currently on section 6
ASCII text, with length 991
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

At offset 0x4e6, currently on section 7
Lat: 38.991094
Long: -76.932802

At offset 0x4fe, currently on section 8
Section type: png, section length: 245614
File png_at_1286.png created

At offset 0x3c474, currently on section 9
ASCII text, with length 22
AF(saSAdf1AD)Snz**asd1

At offset 0x3c492, currently on section 10
ASCII text, with length 45
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


At offset 0x3c4c7, currently on section 11
Array of dwords with 6 dwords and total length 48
[4, 8, 15, 16, 23, 42]
Actual number of sections: 11

5. I was able to find three flags in this excercise, one is hidden in the paragraph about stegonography and is "CMSC389R-{PIN_IF_FLAG}".
Another is in the png file and is "CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}"
The last one was decoded base64 for section 10: "CMSC389-{h1dd3n-s3ct10n-1n-fil3}"
