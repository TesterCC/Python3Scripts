#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/21 00:28'

"""
原始字符串
Python中字符串前面加上 r 表示原生字符串, 如: r'abc'
"""

import re

mm = "c:\\a\\b\\c"

print(mm)

# ret = re.match("c:\\a", mm).group()   # 未处理转义，所以匹配不到
# print(ret)

ret = re.match(r"c:\\a", mm).group()  # 防止字符转义
print(ret)



