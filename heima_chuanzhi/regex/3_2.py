#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/20 23:56'

"""
正则表达式的单字符匹配

.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符
"""

import re

# []

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())

ret = re.match("[hH]", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]", "7Hello Python")
print(ret.group())

# 匹配0到9第三种写法
ret = re.match("\d", "7Hello Python")
print(ret.group())

