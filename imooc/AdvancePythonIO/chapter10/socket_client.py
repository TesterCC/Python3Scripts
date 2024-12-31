#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-26 01:25'

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP -> SOCK_STREAM   # UDP -> SOCK_DGRAM

client.connect(('127.0.0.1', 7777))  # 明确指明IP地址

client.send("CTF Test 测试".encode("utf8"))   # server接收的是bytes类型的所以这里要编码

data = client.recv(1024)
print(data.decode("utf8"))

client.close()