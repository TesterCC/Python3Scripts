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

10-3 字符集 22:00 -30:00 error

'Python' 普通字符
'\d'   一种元字符串， 学习正则表达式就是学习各种各样的元字符

字符集
"""

import re

a = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('a[c-f]c', a)    # 匹配中间包含c-f
print(r)


r = re.findall('a[^c-f]c', a)   # 匹配中间不包含c-f
print(r)

r = re.findall('a[^cdf]c', a)   # 匹配中间不包含c-f
print(r)







