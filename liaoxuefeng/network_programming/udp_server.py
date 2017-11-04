#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/4 22:11'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000
UDP编程 服务端
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999 ...')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s...' % addr)
    if not data or data.decode('utf-8') == 'exit':
        print('UDP Connection from %s:%s closed.' % addr)
    s.sendto(b"Hello, %s!" % data, addr)

# 注意这里省掉了多线程，因为这个例子很简单。

# s.close()    # 一般不让服务端关闭