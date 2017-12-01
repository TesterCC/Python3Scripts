#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/1 23:07'


"""
Python网络爬虫--从入门到实践   P32 3.3.1 传递URL参数
Crawler Target: http://httpbin.org/get?key1=value1
"""

import requests
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get?key1=value1', params=key_dict)
print('URL已经正确解码：', r.url)
print('字符串方式的响应体：\n', r.text)