import subprocess
import socket
import sys
import re
def get_score(): # need to add sending code on server side
    server_port=20000
    #create welcoming socket
    welcome_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #bind server to local host
    welcome_socket.bind(('0.0.0.0',server_port))
    welcome_socket.listen(1)
    #ready message
    print("server running on port: ",server_port)
    #now server side loop
    connection_socket,caddr=welcome_socket.accept()
    print("hello")
    score=connection_socket.recv(1024)
    score=score.decode()
    print(score)
    return score

def send_on_jtag():
    score=0 #initialize score
    server_name='44.214.117.144'
    server_port=12000
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #set TCP connection
    #connection_socket assigned to client on server side
    client_socket.connect((server_name,server_port))
    #assert len(cmd)>=1, "Please make the cmd a single character"    # check if atleast one character is being sent down
    #inputCmd = "nios2-terminal.exe <<< {}".format(cmd);                 # call nios2-terminal and insert characters using <<<
    #with open ('datniga.txt','w',newline='\r') as file: 
    # subprocess allows python to run a bash command*       
    while True: #possibly print a special key from fpga if button is pressed to start/stop loop
        score=10 #change to get score when function works
        print(score)
        output = subprocess.run("nios2-terminal.exe <<< {}".format(score), shell=True, executable='/bin/bash', stdout=subprocess.PIPE)   
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
            client_socket.send(vals.encode())                                  # return the data within the delimtiers <-->
        except UnicodeDecodeError:
            print('failed')
            send_on_jtag(score)                                      # return the data within the delimtiers <-->
#try again
def perform_computation():
    res = send_on_jtag()                                   # example of how to use send_on_jtag function
    #res= get_score()
    print(res)

def main():
    perform_computation()## here we would get a score from the server and if we receive a new score call send on jtag with new cmd
    
if __name__ == '__main__':
    main()
