#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/21 03:04'

"""
01.python高级1
   02.python高级2-生成器、闭包、装饰器
      01-迭代器
"""

for a in "abc":
    print(a)

print("-" * 60)
# 生成器可迭代
b = (x for x in range(10))

print(b)

for temp in b:
    print(temp)