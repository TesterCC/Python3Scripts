#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/1 23:07'


"""
Python网络爬虫--从入门到实践   P32 3.3.1 传递URL参数
Crawler Target: http://httpbin.org/get?key1=value1
"""

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com', headers=headers)
print('URL已经正确解码：', r.url)
print('字符串方式的响应体：\n', r.text)
print("文本响应状态码:", r.status_code)