#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-16 00:05'

# request->urllib->socket

import socket

from urllib.parse import urlparse

"""
10-4 socket模拟http请求

用urlparse是为了方便解析URL
"""

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host =  url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    # key content
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]   # 不返回header info
    print(html_data)

    # close connection
    client.close()

if __name__ == '__main__':
    get_url("http://www.baidu.com")