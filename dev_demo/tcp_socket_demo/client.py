# -*- coding:utf-8 -*-
# client

import socket

client = socket.socket()
print(f"client fd no: {client.fileno()}")

# windows use 0.0.0.0 will report error
CONN_ADDR = ('127.0.0.1', 9999)
client.connect(CONN_ADDR)

while True:
    content = input(">>>")
    client.send(bytes(content, "utf-8"))
    content = client.recv(1024)
    print(f"client receive content: {content}")
