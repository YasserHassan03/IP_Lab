import socket
import csv
#import csv
import threading 
import decimal
import numpy as np



print("We're in server now..")
#deadfile= open('data.txt','w')
#deadfile.close()
#clear file for new data
#select port for server
resultscale = '000008' #test score val initial
server_port=12001
#create welcoming socket
welcome_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind server to local host
welcome_socket.bind(('0.0.0.0',server_port))
welcome_socket.listen(1)
#ready message
print("server running on port: ",server_port)
#now server side loop

#print(score())

 #send score to client 
with open ('data.txt','w',newline='\r') as file:
    while True:   
        connection_socket,caddr=welcome_socket.accept()
        connection_socket.send(resultscale.encode())
        cmsg=connection_socket.recv(1024)
        cmsg=cmsg.decode()
        print(cmsg.split('\r'))
        file.write(cmsg)
        

        
        
