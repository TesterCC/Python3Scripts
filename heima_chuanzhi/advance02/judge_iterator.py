#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/21 03:14'

"""
01.python高级1
   02.python高级2-生成器、闭包、装饰器
      01-迭代器
      
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用 isinstance() 判断一个对象是否是 Iterator 对象
"""

from collections import Iterator

print(isinstance("abc", Iterator))  # Fasle
print(isinstance([], Iterator))   # False
print(isinstance(100, Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True


