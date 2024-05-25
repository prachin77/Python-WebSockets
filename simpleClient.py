# import socket

# client = socket.socket()
# client.connect(("localhost",1234))
# name = input("enter name = ")

# while True:
#     msg = input("enter message = ")
#     client.send(name)
#     server_msg = client.recv(1024).decode()
#     print(server_msg)
#     client.send(msg)
#     client.close()
# import socket

# client = socket.socket()
# client.connect(("localhost", 1234))
# name = input("Enter name: ")

# print("Connected to server")

# while True:
#     msg = input("Enter message: ")
#     client.send(name.encode())
#     server_msg = client.recv(1024).decode()
#     print(server_msg)
#     client.send(msg.encode())
#     client.close()
import socket

client = socket.socket()
client.connect(("localhost", 1234))
name = input("Enter name: ")

print("Connected to server")

# Send the name to the server
client.send(name.encode())

while True:
    msg = input("Enter message: ")
    client.send(msg.encode())
    server_msg = client.recv(1024).decode()
    print(server_msg)
    client.close()
