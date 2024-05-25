import socket
import threading
from pymongo import MongoClient

host = "0.0.0.0"
port = 3001

mongoServer = MongoClient("localhost", 27017)
db = mongoServer["info"]
collection = db["chatApp"]

server = socket.socket()
server.bind((host, port))
print("Server connected")
server.listen()
print("Waiting for clients to connect to the server ⌚")

clients = []
clientNames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handleClientMsg(client):
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                index = clients.index(client)
                clientName = clientNames[index]

                user_document = collection.find_one({"clientName": clientName})

                if not user_document:
                    collection.insert_one({"clientName": clientName, "msg": []})
                    print("Added to MongoDB server")

                collection.update_one(
                    {"clientName": clientName}, {"$push": {"msg": msg.decode()}}
                )
                
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            clientName = clientNames[index]
            broadcast("{} left the chat 😑".format(clientName).encode())
            clientNames.remove(clientName)
            break

# This function will receive clients and their names constantly
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected to address {address} & name = {clientNames}")

        # Send msg to client to check if their is a client or not
        client.send("CLIENTNAME".encode())
        clientName = client.recv(1024).decode()
        clientNames.append(clientName)

        # Check if the client is already in the MongoDB database
        user_document = collection.find_one({"clientName": clientName})
        if user_document:
            print("Previous messages:")
            # prev_msgs = user_document.get("msg", [])
            prev_msgs = user_document.get("msg",[])
            for msg in prev_msgs:
                client.send(msg.encode())
            print(prev_msgs)

        if not user_document:
            collection.insert_one({"clientName": clientName, "msg": []})
            print("Added to MongoDB server")
            

        clients.append(client)

        # Tell the server which user joined with what user name
        print("{}".format(clientNames))

        # This broadcast function will tell all users/clients in the server that a new user joined
        broadcast("{} joined!... 👍".format(clientName).encode())
        client.send("Connected to server ".encode())

        thread = threading.Thread(target=handleClientMsg, args=(client,))
        thread.start()

receive()
