import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # establish endpoint connection
server.bind(("127.0.0.1",5000)) # local host
server.listen(1) # waiting for connection
print("Waiting for connection..")
conn,address = server.accept() #make connection
print("Connected by: ", address)
data = conn.recv(1024)
print("Client says", data.decode())
conn.send("Hello client".encode())
server.close()
conn.close()
