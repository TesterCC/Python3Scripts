#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-16 18:49'

"""
最简单的FTP下载文件

先执行服务端，再执行客户端，最后会在upload文件夹下看到你上传的文件。
"""

# TCP客户端_client.py
import socket
import struct
import os

sk = socket.socket()  # 创建socket对象
sk.connect(("127.0.0.1", 6666))  # 连接服务端
file_name = "test.jpg"
file_size = os.path.getsize(file_name)
sk.send(struct.pack("i", file_size))
with open(file_name, "rb") as f:
    for line in f:
        sk.send(line)
print(f"文件{file_name}上传完成！")
sk.close()