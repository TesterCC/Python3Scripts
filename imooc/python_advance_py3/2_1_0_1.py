#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/20 20:50'

import time

# data = [3, 7, 9, -1, 20, 30, -2, -7, 18]
data = [3, 7, 9, -1, 20, 30, -2, -7, 18, 33, 34, 22, 79, -21, -7]

# Method 1 -- 使用filter函数，过滤掉负数
start = time.clock()
r1 = filter(lambda x: x >= 0, data)
end = time.clock()
print("R1 run time: %f" % (end-start))
print(list(r1))     # in python3, filter() return need user list() to display


# Method 2 -- 使用列表解析，过滤掉负数 -- quicker -- 更快，故首选列表解析
start = time.clock()
r2 = [x1 for x1 in data if x1 >= 0]
end = time.clock()
print("R2 run time: %f" % (end-start))
print(r2)
print("-"*70)


