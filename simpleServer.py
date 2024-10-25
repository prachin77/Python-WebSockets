import socket
from datetime import datetime as dt

server = socket.socket()
server.bind(("localhost", 1234))
print("Server connected")
server.listen()
print("Waiting for clients...")

now = dt.now()

while True:
    client, addr = server.accept()
    client_name = client.recv(1024).decode()
    welcome_msg = f"Hello {client_name}, you're connected to the server!"
    client.send(welcome_msg.encode())  
    while True:
        try:
            msg = client.recv(1024).decode()  
            if not msg or msg.lower() == 'exit': 
                print(f"{client_name} has disconnected.")
                client.close()
                break
            print(f"{client_name}: {msg}")
            response = f"Message received at {now.strftime("%H:%M:%S")}: {msg}"
            client.send(response.encode())  
        except ConnectionResetError:
            print(f"{client_name} connection was reset.")
            client.close()
            break
