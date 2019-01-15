#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-26 01:25'

"""
# 先运行server，再运行client，client端先发送内容
使用多线程，时间服务器和多client聊天
"""

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP -> SOCK_STREAM   # UDP -> SOCK_DGRAM

server.bind(('0.0.0.0', 7777))

server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        # print(data)
        if data.decode("utf8") == "exit":
            break
        re_data = input()
        sock.send(re_data.encode("utf8"))

    sock.close()   # 关闭与client的连接

# 获取从客户端发送的数据
# 一次获取1k的数据

while True:
    sock, addr = server.accept()

    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))   # 注意这里是传函数的名称，而不是函数的调用
    client_thread.start()
