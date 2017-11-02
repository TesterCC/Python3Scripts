#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/2 21:37'

"""
Python3 正则表达式
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
"""

import re

# 分组
# 可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')   # 用()表示的就是要提取的分组（Group）

print(m.group())
print(m.group(0))   # group(0)永远是原始字符串
print(m.group(1))
print(m.group(2))

t = '19:05:30'

mt = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print(mt.group())
print(mt.group(0))
print(mt.group(1))
print(mt.group(2))
print(mt.group(3))