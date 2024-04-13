#!/usr/bin/python3
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 55555))
msg = my_socket.recv(1024)

print(msg.decode())
