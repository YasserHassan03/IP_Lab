import subprocess
import socket
import sys
import re

def send_on_jtag():
    #score=0 #initialize score
    #server_name='44.214.117.144'
    #server_port=12000
    #client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #set TCP connection
    #connection_socket assigned to client on server side
    #client_socket.connect((server_name,server_port))
    #assert len(cmd)>=1, "Please make the cmd a single character"    # check if atleast one character is being sent down
    #inputCmd = "nios2-terminal.exe <<< {}".format(cmd);                 # call nios2-terminal and insert characters using <<<
    #with open ('datniga.txt','w',newline='\r') as file: 
    # subprocess allows python to run a bash command*       
    while True: #possibly print a special key from fpga if button is pressed to start/stop loop
        #score=(client_socket.recv(1024)).decode() #change to get score when function works
        #print(score)
        print("hello")
        output = subprocess.run("nios2-terminal.exe <<< {}".format('987654'+'~'), shell=True, executable='/bin/bash', stdout=subprocess.PIPE) 
        print('inputted')  
        vals = output.stdout                                            # extract the output from the subprocess call
        try:
            vals = vals.decode("utf-8")  # turn the byte-chars into a string  
            vals = vals.split('\r')       #formatting
            del vals[0:5]    
            vals.pop()
            vals.pop()
            vals.pop()
            vals= ''.join(vals)                                 # split the string according to the defined delimiters <-->
            #file.write(vals.decode("utf-8")  )   
            #client_socket.send(vals.encode())                                  # return the data within the delimtiers <-->
        except UnicodeDecodeError:
            print('failed')
            send_on_jtag()                                      # return the data within the delimtiers <-->
#try again
def perform_computation():
    send_on_jtag()                                   # example of how to use send_on_jtag function

def main():
    perform_computation()## here we would get a score from the server and if we receive a new score call send on jtag with new cmd
    
if __name__ == '__main__':
    main()
