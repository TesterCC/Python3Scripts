#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/3 18:53'

import socket   # 导入socket库

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000
TCP编程--客户端
"""

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 9999))   # 参数是一个tuple，包含地址和端口号

# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))

for data in [b"Michael", b"Tracy", b"Sarah"]:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')

# 关闭连接
s.close()

