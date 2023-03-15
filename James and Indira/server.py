import socket
import csv
def send_score(score):
    server_name='192.168.0.9'
    server_port=20000
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #set TCP connection
    #connection_socket assigned to client on server side
    client_socket.connect((server_name,server_port))
    try:
        client_socket.send(score.encode())
    except:
        print("null")
    #client_socket.close()

print("We're in server now..")
deadfile= open('data.txt','w')
deadfile.close()
#clear file for new data
#select port for server
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
with open ('data.txt','w+',newline='\r') as file:
    while True:   
       # send_score(10)
        cmsg=connection_socket.recv(1024)
        cmsg=cmsg.decode()
        print(cmsg.split('\r'))
        file.write(cmsg)
