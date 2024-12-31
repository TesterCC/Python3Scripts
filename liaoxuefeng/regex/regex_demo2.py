#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 21:37'

"""
Python3 正则表达式
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
"""

import re

# 切分字符串

m1 = re.split(r'\s+', 'a  b     c  d')    # 无论多少个空格都可以正常分割

m2 = re.split(r'[\s,]+', 'a , b  ,,,   c  d, e')  # 无论多少个空格和,都可以正常分割

m3 = re.split(r'[\s,;]+', 'a; , b  ,,,   c;;  d, e')  # 无论多少个空格和, ;都可以正常分割

print(m1)
print(m2)
print(m3)



