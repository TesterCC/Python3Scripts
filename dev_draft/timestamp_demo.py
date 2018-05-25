#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/25 09:24'

"""
场景，前端返回unix时间戳字符串，后端转化处理
"""

from datetime import datetime

request = {'timestamp': '1527264000'}

timestamp = int(request.get('timestamp'))

print(type(timestamp))

time = datetime.fromtimestamp(timestamp)

print(time)