#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-30 09:53'

"""
for fix bug
https://www.cnblogs.com/xingxingchaji/p/9750267.html
https://www.cnblogs.com/jfl-xx/p/8024596.html
"""

import time

# 1. 时间戳转换为日期
time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(time_now)

time_past = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1556583758))
print(time_past)

# 2. 日期转换为时间戳
time2stamp = time.mktime(time.strptime('2019-04-29 17:44:10', '%Y-%m-%d %H:%M:%S'))
print(time2stamp)      # float

# 3. 日期转换为时间戳2

test_time = '2019-04-29 17:44:10'
timeArray = time.strptime(test_time, "%Y-%m-%d %H:%M:%S")
time_stamp = int(time.mktime(timeArray))
print(time_stamp)      # long int