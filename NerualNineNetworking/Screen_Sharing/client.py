#!/usr/bin/python3
from vidstream import ScreenShareClient
import threading

client = ScreenShareClient('192.168.1.5', 9999)

my_thread = threading.Thread(target=client.start_server)
my_thread.start()

while input() != 'STOP':
    continue

client.stop_server()
