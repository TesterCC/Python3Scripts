#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 21:37'

"""
Python3 正则表达式
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
"""

import re

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 举例如下，匹配出数字后面的0
# 默认贪婪匹配
m = re.match(r'^(\d+)(0*)$', '102300')   # 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
m2 = re.match(r'^(\d+?)(0*)$', '102300')

print("贪婪匹配")
print(m.groups())
print("非贪婪匹配")
print(m2.groups())


