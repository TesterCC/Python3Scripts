# coding=utf-8
"""
DATE:   2020/11/30
AUTHOR: Yanxi Li

4.1.1 DNS解析
"""

# 1. IP查询 - 查询 域名 对应的 IP
import socket
ip = socket.gethostbyname('x.threatbook.cn')
print(ip)

# 2. Whois查询 通过whois模块查询域名
# pip install python-whois -i https://pypi.tuna.tsinghua.edu.cn/simple/
from whois import whois

data = whois('x.threatbook.cn')
print(data)

