import socket

##print("in client...")
#server name and port
score=10
server_name='192.168.0.9'
server_port=12000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set TCP connection
#connection_socket assigned to client on server side
client_socket.connect((server_name,server_port))
while True:
    try:
        client_socket.send(score.encode())
    except:
        print("null")
    #client_socket.close()