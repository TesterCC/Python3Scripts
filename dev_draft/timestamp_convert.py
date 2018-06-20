#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/20 16:05'

"""
前端传过来时间戳(timestamp),后端接收转化处理
"""

import time

ts = 1528128000

time_array = time.localtime(ts)
print(type(time_array))

format_time = time.strftime("%Y--%m--%d %H:%M:%S", time_array)
print(format_time)
