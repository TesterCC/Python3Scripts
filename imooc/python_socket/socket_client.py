#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/8 14:05'


"""
2-2 socket客户端程序  TCP
https://www.imooc.com/video/17676
"""

import socket

client = socket.socket()

# bind ip and port
ip_port = ("127.0.0.1", 8888)

client.connect(ip_port)

# 接收主机信息  服务器回的消息
data = client.recv(1024)   # 1024字节

# print receive data, python3.x以上默认这里传bytes
print(data.decode())
