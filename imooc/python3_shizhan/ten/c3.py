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

10-2 元字符与普通字符 13:50

'Python' 普通字符
'\d'   一种元字符串， 学习正则表达式就是学习各种各样的元字符
"""

import re

a = 'C0C++7Java8C#9Python6Javascript'

# 将字符串中的所有数字都提取出来
r = re.findall(r'\d', a)    # \d  匹配数字
if len(r) > 0:
    print(r)
else:
    print("No")

r = re.findall(r'\D', a)    # \D  匹配非数字
if len(r) > 0:
    print(r)
else:
    print("No")






