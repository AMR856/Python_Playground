#!/usr/bin/python3
import socket
import threading
import sys

ip_address = '127.0.0.1'
port = int(sys.argv[1])
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, port))

my_nickname = input("Please enter your nickname!: ")

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii').strip()
            if msg == 'Nick':
                client.send(my_nickname.encode('ascii'))
            else:
                joining_string = f"{my_nickname} joined!! Losers!"
                if msg == joining_string:
                    pass
                else:
                    print(msg)
        except:
            print("Something really bad happened!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(my_nickname, input(""))
        client.send(message.encode('ascii'))

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
