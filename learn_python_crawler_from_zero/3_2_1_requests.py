#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/10 23:42'

"""
从零开始学Python网络爬虫(Yellow Cover) 3-2-1

# "http://httpbin.org/ip"
# "https://httpbin.org/get?show_env=1"
# "http://2018.ip138.com/ic.asp"
"""

import requests

TARGET_URL = "https://httpbin.org/get?show_env=1"

# 伪装User-Agent, 可以直接用3rd-party lib fake_useragent, usage: from fake_useragent import UserAgent
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/61.0'

headers = {
    "User-Agent": user_agent
}

res = requests.get(TARGET_URL, headers=headers)

print(res)
print(res.reason)
print("*" * 90)
print(res.text)
print("*" * 90)
print(type(res.text))



