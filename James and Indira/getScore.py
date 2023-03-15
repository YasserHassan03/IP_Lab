import socket
import sys
import re

 # need to add sending code on server side
server_port=12000
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
while True:
    score=connection_socket.recv(1024)
    score=score.decode()
    print(score)

