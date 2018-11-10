#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/10 23:42'

"""
从零开始学Python网络爬虫(Yellow Cover) 3-2-1
"""

import requests

TARGET_URL = 'http://bj.xiaozhu.com/'
res = requests.get(TARGET_URL)

print(res)
print(res.reason)
print(res.text)
print("*" * 90)
print(type(res.text))



