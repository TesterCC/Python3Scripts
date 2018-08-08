#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/8 13:32'

"""
2-1 服务器端程序   TCP
https://www.imooc.com/video/17675
"""

import socket

# create instance

sk = socket.socket()

# bind ip and port
ip_port = ("127.0.0.1", 8888)

# bind listen
sk.bind(ip_port)

# max keep connection
sk.listen(5)     # 处理的只有1个，另外4个处于等待状态，最小为1

# notice info
print(">>>>!!! Waiting for accept data...")

# accept data
conn, address = sk.accept()     # 程序在这里是阻塞的

msg = "Hello World"

# return msg
# Python 3.X以上，网络数据的发送和接受都是byte类型
# 如果发送的数据是str类型，则需要进行编码
conn.send(msg.encode())

# initiative close connection
conn.close()
