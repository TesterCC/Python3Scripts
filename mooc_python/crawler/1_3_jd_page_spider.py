#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-11 16:22'

import requests

"""
实战一： 爬京东单页面
"""

url = "https://item.jd.com/2967929.html"

try:
    r = requests.get(url)
    print(r.status_code)
    print(r.encoding)
    print(r.text[:1000])
except:
    print("Crawl info failed.")