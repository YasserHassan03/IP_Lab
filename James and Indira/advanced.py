import subprocess
import socket
import sys
import re
import decimal


def send_on_jtag():
    # score=0 #initialize score
    # set TCP connection
    # connection_socket assigned to client on server side
    # assert len(cmd)>=1, "Please make the cmd a single character"    # check if atleast one character is being sent down
    # inputCmd = "nios2-terminal.exe <<< {}".format(cmd);                 # call nios2-terminal and insert characters using <<<
    # with open ('datniga.txt','w',newline='\r') as file:
    # subprocess allows python to run a bash command*
    send = -1  # don't start journey til start is pressed
    while True:  # possibly print a special key from fpga if button is pressed to start/stop loop
        server_name = '54.236.230.179'
        server_port = 12004
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_name, server_port))
        print("hello")
        # score='123456'
        print("connected")
        # change to get score when function works
        score = (client_socket.recv(1024)).decode()
        print(score)
        output = subprocess.run("nios2-terminal.exe <<< {}".format(score),
                                shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
        print('inputted')
        # extract the output from the subprocess call
        vals = output.stdout
        try:
            vals = vals.decode("utf-8")  # turn the byte-chars into a string
            if send==-1:
                send=vals.find('START')
            if (vals.find('END')>-1):
                send=-1
            if send>-1:
                vals = vals.split('\r')       #formatting
                del vals[0:5]    
                vals.pop()
                vals.pop()
                vals.pop()
                vals= ''.join(vals)                                 # split the string according to the defined delimiters <-->
                #file.write(vals.decode("utf-8")  )   
                client_socket.send(vals.encode())                                  # return the data within the delimtiers <-->
                print("your gay")
                client_socket.close()
                print("helo")
                send = 0
        except UnicodeDecodeError:
            print('failed')
            # return the data within the delimtiers <-->
            send_on_jtag()

# try again


def perform_computation():
    # example of how to use send_on_jtag function
    send_on_jtag()


def main():
    # here we would get a score from the server and if we receive a new score call send on jtag with new cmd
    perform_computation()


if __name__ == '__main__':
    main()
