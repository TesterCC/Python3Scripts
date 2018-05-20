#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/20 23:48'

import re

"""
re.match() 能够匹配出以xxx开头的字符串
"""

result = re.match("fullstack", "fullstackpentest.com")

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
# 若字符串匹配正则表达式，则match方法返回匹配对象（Match Object），否则返回None（注意不是空字符串""）
print(result.group())