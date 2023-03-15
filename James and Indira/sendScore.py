import socket

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
        cmsg='10'
        connection_socket.send(cmsg.encode())