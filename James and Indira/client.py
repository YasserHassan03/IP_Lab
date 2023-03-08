import socket
import csv
import keyboard
##print("in client...")
#server name and port
clearfile= open('C:/Users/james/Desktop/Imperial/Informationprocessing/IP_Lab/James and Indira/pythonaccel/accelerometer.csv','w')
clearfile.close()
server_name='3.237.199.213'
server_port=12000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set TCP connection
#connection_socket assigned to client on server side
client_socket.connect((server_name,server_port))

with open ('C:/Users/james/Desktop/Imperial/Informationprocessing/IP_Lab/James and Indira/pythonaccel/accelerometer.csv') as dat:
    next(dat)
    read=csv.reader(dat)  
    while (True):
        for row in read:
            print(((','.join(row)+'\r').encode()).decode())
            client_socket.send(('['+','.join(row)+']''\r').encode())

client_socket.close()