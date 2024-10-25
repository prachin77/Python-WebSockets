import socket

client = socket.socket()
client.connect(("localhost", 1234))
name = input("Enter name: ")

# Send the name encoded as bytes
client.send(name.encode())

# Receive and print the welcome message from the server
server_msg = client.recv(1024).decode()
print(f"Server: {server_msg}")

# Keep the connection open to send and receive messages
while True:
    msg = input("Enter message: ")
    if msg.lower() == 'exit':
        print("Closing connection...")
        client.close()
        break
    
    client.send(msg.encode())

    # Receive the server's response
    server_msg = client.recv(1024).decode()
    print(f"Server: {server_msg}")
