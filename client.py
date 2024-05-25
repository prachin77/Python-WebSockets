import socket
import threading

clientName = input("Enter name: ")
client = socket.socket()

# host = "0.0.0.0"
host = socket.gethostname()
port = 3001

client.connect((host, port))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg == "CLIENTNAME":
                client.send(clientName.encode())
            else:
                print(msg)
        except:
            print("An error occurred 😡")
            client.close()
            break

def send_msg():
    while True:
        msg = "{}: {}".format(clientName, input(""))
        client.send(msg.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send_msg)
send_thread.start()
