#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/4 22:27'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000
UDP编程 客户端
"""

import socket

# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后不需要调用connect()，直接通过sendto()给服务器发数据
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.sendto(b'exit', ('127.0.0.1', 9999))
# 关闭连接
s.close()