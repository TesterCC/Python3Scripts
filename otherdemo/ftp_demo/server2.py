#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-16 18:59'

"""
优化版ftp上传

即便是视频文件，也是可以按行来读取的，也可以readline，也可以for循环，但是读取出来的数据大小就不固定了，影响效率，有可能读的比较小，
也可能很大，像视频文件一般都是一行的二进制字节流。
所有我们可以用read，设定一个一次读取内容的大小，一边读一边发，一边收一边写。
"""

import json
import socket
import struct

server = socket.socket()
ip_port = ("127.0.0.1", 8001)
buffer = 1024
server.bind(ip_port)
server.listen(5)
print("开启监听！")
conn, addr = server.accept()
print("客户端连接成功！")
header_len = conn.recv(4)  # 接收报头长度
header_bytes = conn.recv(struct.unpack('i', header_len)[0])  # 接收报头
header = json.loads(header_bytes.decode("utf-8"))  # 报头解码->反序列化
file_size = header['filesize']  # 文件的大小
print(file_size, buffer)
with open("upload/"+header['filename'], "wb") as f:   # 上传到upload目录
    while file_size:
        if file_size >= buffer:
            f.write(conn.recv(buffer))
            file_size -= buffer
            print(file_size, buffer)
        else:
            f.write(conn.recv(buffer))
            print(file_size, buffer)
            break
conn.close()
server.close()