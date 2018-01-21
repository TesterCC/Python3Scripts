#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/21 03:14'

"""
01.python高级1
   02.python高级2-生成器、闭包、装饰器
      01-迭代器
      
可以使用 isinstance() 判断一个对象是否是 Iterable 对象
"""

from collections import Iterable

print(isinstance("abc", Iterable))  # True
print(isinstance([], Iterable))   # True
print(isinstance(100, Iterable))  # False


