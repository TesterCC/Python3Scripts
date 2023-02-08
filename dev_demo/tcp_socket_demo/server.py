# -*- coding:utf-8 -*-
# server
import socket

# 1.创建套接字
server = socket.socket()

# 打印套接字文件描述符
print(f"server fd no: {server.fileno()}")

# 2.绑定套接字
CONN_ADDR = ('127.0.0.1', 9999)
server.bind(CONN_ADDR)

# 3.监听套接字
server.listen(1)

# 4.接受连接
s, addr = server.accept()

print(f'socket file no: {s.fileno()}, connect addr: {addr}')

# 服务端把收到的信息再重新发回给客户端
while True:
    # receive data
    content = s.recv(1024)
    if not content:
        break
    # send data
    s.send(content.upper())
    print('recv: ', content)
