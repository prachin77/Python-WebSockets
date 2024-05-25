# import socket
# server = socket.socket()
# server.bind(("localhost",1234))
# print("server connected")
# server.listen()
# print("waitin for clients")

# while True:
#     client , add = server.accept()
#     clientName = client.recv(1024).decode
#     print(f"welcome {clientName} connected to port = 1234")
    
#     client.close()
import socket

server = socket.socket()
server.bind(("localhost", 1234))
print("Server connected")
server.listen()
print("Waiting for clients")

while True:
    client, addr = server.accept()
    client_name = client.recv(1024).decode()
    print(f"Welcome {client_name} connected to port = 1234")
    client.send(b"Hello")  # Send hello message to the client
    client.close()

