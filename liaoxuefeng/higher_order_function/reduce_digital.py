#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 21:42'


"""
编程题：
把序列[1, 3, 5, 7, 9]变换成整数13579
"""

from functools import reduce


def fn(x, y):
    return x*10+y

r2 = reduce(fn, [1, 3, 5, 7, 9])

print(r2)