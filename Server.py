import socket
 

host = str(input("Server ip (my) "))
port = int(input("port "))
     
mySocket = socket.socket()
mySocket.bind((host,port))
     
mySocket.listen(1)
conn, addr = mySocket.accept()
print ("Connection from: " + str(addr))
while True:
    data = conn.recv(1024).decode()
    if not data:
                    break
    print (int(data))           

conn.close()

