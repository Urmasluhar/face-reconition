import socket
 
host = str(input("Server ip "))
port = int(input("port "))
         
mySocket = socket.socket()
mySocket.connect((host,port))
         
message = input(" -> ")
         
while message != 'q':
    mySocket.send(message.encode())
                 
    message = input(" -> ")
                 
mySocket.close()
 
