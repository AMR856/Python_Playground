#!/usr/bin/python3
import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('127.0.0.1', 55555))
my_socket.listen()

while True:
    client, address = my_socket.accept()
    print(f"Connected to {address}!")
    client.send("You are connected!".encode())
    client.close()


# AF_INET -> Internet Socket
# SOCK_STREAM -> TCP
# SOCK.DGRAM -> UD
