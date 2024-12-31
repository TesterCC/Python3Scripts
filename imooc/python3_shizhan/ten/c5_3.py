#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 01:14'

"""
概括字符集

\d  数字字符   \D  非数字字符
\w  单词字符   \W  非单词字符
\s  空白字符   \S  非空白字符
.   匹配除换行符\n之外其他所有字符   
"""

import re

a = 'python 11\t11java&678p\nh\rp'

r = re.findall('\s', a)
print(r)

r2 = re.findall('.', a)
print(r2)