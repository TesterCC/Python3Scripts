#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 22:04'

"""
5-3 list中extend方法区别
"""

from collections import abc

a = [1, 2]

c = a + [3, 4]
print(c)

# # 就地加
# a += [3, 4]
# print(a)
#
# a += (3, 4)
# print(a)
#
# a.extend(range(3))
# print(a)

d = (1, 2)
d += (3, 4)
print(d)

a.append((1, 2))
print(a)

a.extend((5, 6))
print(a)
