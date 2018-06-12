#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/12 14:32'

import requests

req = requests.Request(method='POST', data={'a': 23, 'b': 'funny'}, url='http://httpbin.org/post')

pre = req.prepare()

print(pre.body)

print(pre.headers)

# use json parameter
print('>>' * 10 + 'use json parameter' + '<<' * 10)
req2 = requests.Request(method='POST', json={'a': 23, 'b': 'funny'}, url='http://httpbin.org/post')

pre2 = req2.prepare()

print(pre2.body)

print(pre2.headers)
