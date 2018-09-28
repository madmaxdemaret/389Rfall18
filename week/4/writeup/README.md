Writeup 3 - Pentesting I
======

Name: Max Demaret
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Max Demaret

## Assignment 4 Writeup

### Part 1 (45 pts)

The first thing I did was to nmap port 45, to find out it was running service mpm. Upon looking that up I learned that it was a forking service, and it had a keep alive problem. 

Then I realized I was overthinking it, and tried a few tricky inputs. First I tried outside ip addresses such as 8.8.8.8, but that worked. Then I added code after the ip address, such as 127.0.0.1; ls -a. That printed out the directory, so I knew I got something.

Using the trick of putting a ; then commands, I was able to find the script that Fred is running to handle connections. That script is located at /opt/container_startup.sh, and it does not do any input verification. This means any attacker could attach a command to run with &&, or just skip the ping verification entirely by adding ; before they type their commands. However, this exploit only allows for one shot commands. To be able to traverse the directory and run multiple commands, we would need a shell (see part 2).  

After I figured out the exploit, I used it to ls the home directory, which showed a flag.txt file, then I ran "; cat /home/flag.txt" to get this flag:
CMSC389R-{p1ng_as_a_$erv1c3}

I went first to the home directory because that is the most commonly used directory and pervious homeworks flags were there in earlier exercises.

Fred does not do any type of input verification, he simply accepts whatever input the user gives to him and appends it to the command "ping -w 5 -c 2". This means a user could give him ";[COMMAND_HERE]" and run whatever commands they wish. To prevent this, I suggest Fred implament regex checks to the user input. I am not a bash scripter, but I think the following line, put right before the end, would work:

if [[ $input =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
    output=$(eval $cmd) echo $output
fi

This checks the users input against a regex designed to match ip addresses, if the user's input does not match then nothing is run. This will prevent users from running anything, as this regex will ensure Fred's command is not run unless the user only gives an ip address and nothing else.

### Part 2 (55 pts)

Using the vunurability I detailed above, I wrote an interactive shell to simulate a real shell on the machine. My program keeps track of the current directory, and when a user cd's it changes the variable storing the current directory. When a user runs a command my program connects to cornerstoneairlies.co through port 45 and sends the following input: "; cd current_directory && user_input". This allows the user to traverse through the directories and run commands in them. If the commands result in an error then no data is returned, as the server redirects standard error to log commands run on the server. The directory traversal becomes a problem when the user goes into a sub-sub directory of the root, as the way it is set up the user would have to cd /sub-directory/sub-directory2, instead of cd sub-directory then cd sub-directory2. When a user does this it results in an error, and nothing is returned. 

Additionally my program allows pulling. This is essentially catting the requested file and outputing it into a file on the users computer, but it still allows downloading ASCII files.

This shell is located in stub.py, and can be run by typing python stub.py in the terminal.
