import socket

##print("in client...")
#server name and port
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

while True:
    send_score(10)