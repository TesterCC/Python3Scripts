# coding=utf-8
'''
DATE: 2020/09/26
AUTHOR: Yanxi Li

2-8 Socket网络编程 Server
'''

import socket

language = {"what is your name": "I'm Robot.", "how old are you": "2 years old", "bye": "Bye!"}
HOST = "127.0.0.1"
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
s.bind((HOST, PORT))
s.listen(1)
print("[+] Listening at port %d" % PORT)

conn, addr = s.accept()
print('[S] Connect by: ', addr)

while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print("[S] Received message: ", data)
    conn.sendall(language.get(data, "Nothing").encode())

conn.close()
s.close()
