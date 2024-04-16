#!/usr/bin/python3
import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except Exception as Everything:
            my_index = clients.index(client)
            clients.remove(my_index)
            client.close()
            my_nickname = nicknames[my_index]
            broadcast(f"{my_nickname} left the chat!!! Losers")
            nicknames.remove[my_index]
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected to the server {str(address)}")

        client.send('Nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined!! Losers!".encode('ascii'))
        client.send("You're connected to the server! Dude\n".encode('ascii'))

        my_thread = threading.Thread(target=handle, args=(client, ))
        my_thread.start()

if __name__ == '__main__':
    receive()
