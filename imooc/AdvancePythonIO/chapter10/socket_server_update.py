#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-26 01:25'

"""
# 先运行server，再运行client，client端先发送内容
"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP -> SOCK_STREAM   # UDP -> SOCK_DGRAM

server.bind(('0.0.0.0', 7777))

server.listen()

sock, addr = server.accept()

# 获取从客户端发送的数据
# 一次获取1k的数据

while True:

    data = sock.recv(1024)
    print(data.decode("utf8"))   # 返回的是bytes类型，需要decode
    re_data = input()
    sock.send(re_data.encode("utf8"))


    # print("reply message...")
    # sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))    # send的数据也要是bytes类型
    # server.close()
    # sock.close()  # 真正的server一般不会close

