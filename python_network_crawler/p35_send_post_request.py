#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/2 22:31'

"""
Python网络爬虫--从入门到实践   P35 3.3.3 发送POST请求
Crawler Target: http://httpbin.org/get?key1=value1
"""

import requests

key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)   # post default argus data
print(r.text)


