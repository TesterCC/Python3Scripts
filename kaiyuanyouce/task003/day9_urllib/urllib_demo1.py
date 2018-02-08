# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/8 10:07'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484160&idx=1&sn=0a42d651e5d3d6e5b4c2d7fe376c626a&scene=19#wechat_redirect
"""

from urllib.parse import urlparse


print("urllib url切割实例")

url = "http://username:password@www.baidu.com:80/q=python"

# parse模块可以把url进行拆分或组合
result = urlparse(url)

print("看下切割后的整体结果: ")
print(result)

print("协议: ", result.scheme)
print("连接字符串：", result.netloc)
print("端口号：", result.port)
print("uri资源：", result.path)
print("用户名：", result.username)
print("密码：", result.password)
