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

正则表达式的重点在于规则 10-1
"""

import re

a = 'C|C++|Java|C#|Python|Javascript'

# 最基本方法
r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print("No")






