#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/9 00:34'


"""
Python网络爬虫 P159
cookies文件中是登陆后直接copy的抓到的报的cookie
Failed, don't use
"""

import requests
import http.cookiejar as cookielib


session = requests.session()
session.get("https://www.huodongjia.com/")

session.cookies = cookielib.LWPCookieJar(filename='cookies')

session.cookies.save()


session.cookies.load(ignore_discard=True)
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
# ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入。

print("Cookie cannot load.")

