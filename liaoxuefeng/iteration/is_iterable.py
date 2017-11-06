#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/6 22:34'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000
迭代器
"""

from collections import Iterable
from collections import Iterator

print("------测试可迭代--------")

print(isinstance([], Iterable))   # 判断是否可迭代

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100, Iterable))

print("------测试迭代器--------")

print(isinstance((x for x in range(10)), Iterator))    # 判断是否是迭代器

print(isinstance([], Iterator))   # 判断是否可迭代

print(isinstance({}, Iterator))

print(isinstance('abc', Iterator))

print("------测试iter()--------")
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))

print(isinstance(iter('abc'), Iterator))

