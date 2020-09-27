# coding=utf-8
'''
DATE: 2020/09/26
AUTHOR: Yanxi Li

2-8 Socket网络编程 Client
'''

import socket
import sys

HOST = "127.0.0.1"
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except Exception as e:
    print("Server not found!")
    sys.exit()

while True:
    c = input("YOU SAY:")
    s.sendall(c.strip().encode())
    data = s.recv(1024)
    data = data.decode()
    print("[C] Received: ", data)
    if c.lower() == "see ya":
        break
