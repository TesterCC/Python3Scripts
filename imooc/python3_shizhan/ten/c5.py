#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/2 21:48'

"""
第10章 正则表达式与JSON
正则表达式
JSON XML

正则表达式是一个特殊的字符序列，一个字符串是否与我们所设定的这样的字符序列相匹配。

快速检索文本、实现一些替换文本的操作

1.检查一串数字是否是电话号码
2.检测一个字符串是否符合email
3.把一个文本里指定的单词替换为另外一个单词

如果正则用的6，可以不用很多内置方法

正则表达式的重点在于规则 

10-4 概括字符集  31:30

'Python' 普通字符
'\d'   一种元字符串， 学习正则表达式就是学习各种各样的元字符
"""

import re

# 概括字符集    \d 数字    \D 非数字  32:41
a = 'python1111java678php'

# 匹配数字
r = re.findall('\d', a)
print(r)

# 匹配非数字
r = re.findall('\D', a)
print(r)

# 匹配数字
r = re.findall('[0-9]', a)
print(r)

# 匹配非数字
r = re.findall('[^0-9]', a)
print(r)

# 匹配数字和字母  \w   35:05
r = re.findall('\w', a)
print(r)







