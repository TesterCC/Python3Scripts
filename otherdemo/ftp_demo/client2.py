#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-16 19:20'


"""
优化版ftp上传

即便是视频文件，也是可以按行来读取的，也可以readline，也可以for循环，但是读取出来的数据大小就不固定了，影响效率，有可能读的比较小，
也可能很大，像视频文件一般都是一行的二进制字节流。
所有我们可以用read，设定一个一次读取内容的大小，一边读一边发，一边收一边写。
"""

import os
import json
import struct
import socket

client = socket.socket()
ip_port = ("127.0.0.1", 8001)
client.connect(ip_port)
buffer = 1024
header = {  # 报头为dict类型
    "filename": "test.jpg",
    "filepath": "",
    "filesize": 0,
}
file_path = os.path.join(header['filepath'], header['filename'])
file_size = os.path.getsize(file_path)
header['filesize'] = file_size
header_json = json.dumps(header)  # 报头序列化为json字符串
header_bytes = header_json.encode("utf-8")  # 报头编码为bytes类型
client.send(struct.pack('i', len(header_bytes)))  # 发送4个字节的报头大小
client.send(header_bytes)  # 发送报头
print(file_size, buffer)
with open(file_path, "rb") as f:
    while file_size:
        if file_size >= buffer:
            client.send(f.read(buffer))
            file_size -= buffer
            print(file_size, buffer, "第一次或中间的")
        else:
            client.send(f.read(buffer))
            print(file_size, buffer, "最后一次")
            break
client.close()