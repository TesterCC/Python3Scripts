#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-26 01:25'

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP -> SOCK_STREAM   # UDP -> SOCK_DGRAM

server.bind(('0.0.0.0', 7777))

server.listen()

sock, addr = server.accept()

# 获取从客户端发送的数据
 


