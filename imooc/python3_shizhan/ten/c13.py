#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 01:05'

"""
正则模式

概括字符集

\d  数字字符   \D  非数字字符
\w  单词字符   \W  非单词字符
\s  空白字符   \S  非空白字符
.   匹配除换行符\n之外其他所有字符
"""

import re

language = 'PythonC#JavaPHP'

r = re.findall('c#', language)

r2 = re.findall('c#', language, re.I)   # 忽略大小写 正则模式

print(r)
print(r2)

r3 = re.findall('c#.{1}', language, re.I)
r4 = re.findall('c#.{1,4}', language, re.I)

print(r3)
print(r4)
