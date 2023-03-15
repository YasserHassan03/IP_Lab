import socket
import csv
import keyboard
import pandas
##print("in client...")
#server name and port

server_name='44.214.117.144'
server_port=12000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set TCP connection
#connection_socket assigned to client on server side
client_socket.connect((server_name,server_port))
while True:
    msg=client_socket.recv(1024)
    print(msg.decode())


client_socket.close()