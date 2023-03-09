import socket
import csv
import keyboard
import pandas
##print("in client...")
#server name and port
def clearfile(path):
    deadfile= open(path,'w')
    deadfile.close()
clearfile('C:/Users/james/Desktop/Imperial/Informationprocessing/IP_Lab/James and Indira/pythonaccel/accelerometer.csv')
server_name='44.214.8.122'
server_port=12000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set TCP connection
#connection_socket assigned to client on server side
client_socket.connect((server_name,server_port))

with open ('C:/Users/james/Desktop/Imperial/Informationprocessing/IP_Lab/James and Indira/pythonaccel/accelerometer.csv') as dat:
    read=csv.reader(dat) 
    n=0 
    while (True):
        n=n+1
        try:
            for row in read:
                print(((','.join(row)+'\r').encode()).decode())
                client_socket.send(('['+','.join(row)+']''\r').encode())
        except:
            print("null")
        if n>100000:
            clearfile('C:/Users/james/Desktop/Imperial/Informationprocessing/IP_Lab/James and Indira/pythonaccel/accelerometer.csv')

client_socket.close()