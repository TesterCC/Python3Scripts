#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 21:37'

"""
Python3 正则表达式
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
"""

import re

m = re.match(r'^\d{3}-\d{3,8}$', '010-1234567')
print(m.group())
print(m.group(0))

# User input str
test = input("Please input telephone number: ")

if re.match(r'^\d{3,4}-\d{3,8}$', test):
    print('Telephone is OK.')
else:
    print('Failed, please check it.')