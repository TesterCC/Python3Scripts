#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/1 23:03'


"""
Python网络爬虫--从入门到实践   P32 3.2 get response info
Crawler Target: www.santostang.com
"""

import requests
r = requests.get('http://www.santostang.com')
print("文本编码:", r.encoding)
print("文本响应状态码:", r.status_code)
print("字符串方式的响应体:\n", r.text)