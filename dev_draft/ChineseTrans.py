#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/17 09:07'

"""
Python 3 中文汉字和utf-8转换
"""

# python3 print()打印和ipython中的输出是一致的，python 2不是

# a = "\u738b\u8d85\uff08\u5317\u4eac\u4e2d\u5174\u65b0\u666f\u4fe1\u606f\u6280\u672f\u7814\u7a76\u9662\uff09"

a = u'王超'

print(a.encode('utf-8'))   # utf-8, ipython, b'\xe7\x8e\x8b\xe8\xb6\x85'

print(a.encode('unicode_escape'))    # bytes, ipython b'\\u738b\\u8d85'

print(a)


a2 = u'\u738b\u8d85'

print(a2)