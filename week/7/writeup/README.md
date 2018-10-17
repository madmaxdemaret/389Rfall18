Writeup 7 - Forensics I
======

Name: Max Demaret
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 7 writeup

### Part 1 (40 pts)

1. This file is a JPEG file, or a picture.

2. This photo was taken at the John Hancock Center in Chicago, Illinois.

3. This photo was taken on Augest 22, 2018, at 11:30:24 am.

4. This picture was taken by an iPhone 8, using the back camera.

5. This photo was taken 539.5 m above sea level

6. Once flag found in the file is CMSC389R-{look_I_f0ound_a_str1ng}

### Part 2 (55 pts)

First I ran the program and saw the output "Where is your flag?" Then I opened the binary in ida free. The first thing I saw was a directory path, "/tmp/.stego". Then I saw that the binary took input from a variable called challenge and called reverse array on it, then wrote it to the file "/tmp/.stego". Then, taking a hint from the name of the file, I ran steghide extract --stegofile .stego, however that resulted in steghide not supporting the file format of .stego. I then opened up the file in xxD to see the file signature. Looking up the signature in widipedia's list of file signatures showed that the file was a raw JPEG in the JFIF file format, however the file header was messed up somehow. Using binwalk's -e option, I was able to extract the image. I then ran exiftool on the image to see if it would output a flag, but it did not. I then opened the file to see if the flag was visable on the standard picture, but it was a simple picture of a stegosaurus (ha ha). Then I ran strings on the file, but that did not produce any human readable text. 

Based on the assumption that the picture contained data that the instructors expected us to find using steghide, I ran steghide on the extracted picture. Steghide needs a password to search the file for encrpted data, so I put in several passwords that I expected the instructors to use, including "password", "", "CMSC389R", "stego", "steganography", "flag", and "/tmp/.stego". All of these resulted in steghide being unable to extract any data with the pashphrase. However, I was able to get an output when I typed the password "stegosaurus". With that password, steghide outputed the string "Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}".
