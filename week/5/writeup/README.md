Writeup 5 - Binaries I
======

Name: Max Demaret
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 5 Writeup

Upon starting this assignment, first I had to look up what registers were used to pass in arguments. I am horrible at remembering the passing registers, and have to look them up almost every time I write or read assembly. Once I looked them up and wrote down which argument was passed in which, I tried to copy the functionality of the c code the instructors provided. 

Both loops start by declaring an incrementor, i, to be 0, so I started by mov'ing 0 into rcx. Then they loop, comparing i to the length value passed in as the third argument, so I cmp'ed rcx to rdx (the third argument) and, if rcx is greater or equal to rdx, we jump to the exit. 

After the comparison, I implamented the moves. Memset was easy, as they passed in the value to set in rsi, so all I had to do was move it from rsi into the memory address given by rdi (the string pointer) + rcx multipled by one (since strings are character arrays and char's are one byte long). Strncpy was a bit more tricky, because you cannot move from memory to memory in assembly, so I had to use r8 as a storage register for the value to move.

After the move all I had to do was increment my counter and jump back to my comparison.

The only problem that I ran into is that the assembler (yasm) did not seem to like any form of specifying length of memory access, whether that is byte ptr, byte,or BYTE. To get around this I changed all of the registers in the mov commands to only be the lower byte of the registers so I would not have to specify the length of memory access, which worked.
