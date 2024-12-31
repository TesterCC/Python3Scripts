#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 01:29'

"""
正则替换
"""

import re

language = 'PythonC#JavaPHP'

r = re.sub('C#', 'Go', language)   # 匹配到C#并替换为Go

print(r)

language2 = 'PythonC#JavaC#PHPC#'

r2 = re.sub('C#', 'Go', language2, 2)   # 匹配到C#并替换为Go，只进行前2个的替换

print(r2)

# 不推荐，python的替换法,不灵活，不能指定替换次数
language = language2.replace('C#', 'Go')
print(language)
