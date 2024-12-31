#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-16 18:35'


"""
最简单的FTP上传文件

先执行服务端，再执行客户端，最后会在upload文件夹下看到你上传的文件。
"""

# TCP服务端_server.py
import socket
import struct

sk = socket.socket()  # 创建socket对象
sk.bind(("127.0.0.1", 6666))  # 绑定IP和端口号
sk.listen()  # 开启监听
print("开启监听！")
conn, address = sk.accept()  # 等待客户端连接 阻塞
print("客户端连接成功！")
file_size = struct.unpack("i", conn.recv(4))[0]
f = open("upload/flower.jpg", "wb")
while file_size > 0:
    msg = conn.recv(1024)
    f.write(msg)
    file_size -= len(msg)

conn.close()
sk.close()