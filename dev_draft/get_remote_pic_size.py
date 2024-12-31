#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/17 23:16'

import requests

"""
Python快速获取图片文件大小

https://www.v2ex.com/t/67865
https://blog.csdn.net/pud_zha/article/details/8809878
HTTP之Content-Length
"""

# url = 'https://pic.huodongjia.com/event/2017-12-20/1513755021.78.jpg'
# url = 'https://pic.huodongjia.com/event/2018-02-23/1519357566.95.jpg'

url = 'http://www.huodongxing.com/logodownload/logo_huodongx_green.png'

# 两种写法都可用
# pre_img_size = requests.head(url).headers.get('content-length')   # content-length单位为字节
pre_img_size = requests.get(url).headers['content-length']

print(requests.get(url).headers)
print(pre_img_size)   # 1343024字节/1024

image_size = int(pre_img_size)/1024

if image_size > 2000:
    print("下载图片不能大于2M")
else:
    print("开始下载")

print("{} k".format(image_size))



