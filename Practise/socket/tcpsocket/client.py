import socket
clinet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet.connect(("127.0.0.1",5000))
clinet.send("Hello server".encode())
data = clinet.recv(1024)
print("Server says:", data.decode())
clinet.close()