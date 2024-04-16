#!/usr/bin/python3
from vidstream import StreamingServer
import threading

server = StreamingServer('192.168.1.5', 9999)

my_thread = threading.Thread(target=server.start_server)
my_thread.start()

while input() != 'STOP':
    continue

server.stop_server()
