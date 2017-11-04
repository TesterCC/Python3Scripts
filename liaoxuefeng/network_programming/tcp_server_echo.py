#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/4 18:41'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000
TCP编程--服务端
编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。
"""

import socket   # 导入socket库
import threading
from time import sleep

# 创建一个基于IPv4和TCP协议的Socket       # SOCK_STREAM 流式socket，用于TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定
# 监听端口
s.bind(('127.0.0.1', 9999))

# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量  listen(max)
s.listen(5)
print('Waiting for connection...')


# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s ...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('TCP Connection from %s:%s closed.' % addr)

# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

