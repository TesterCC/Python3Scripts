#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/15 13:33'

"""
10-5 数量词
"""

import re

a = 'python 1111java678php'

r = re.findall('[a-z]{3}', a)
print(r)

r1 = re.findall(r'[a-z]{3}', a)
print(r1)

r2 = re.findall('[a-z]{3,6}', a)  # 匹配3到6个连续字母，默认为贪婪匹配
print(r2)

r3 = re.findall('[a-z]{3,6}?', a)  # 匹配3到6个连续字母，设置为非贪婪匹配
print(r3)



