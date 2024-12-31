#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/15 21:12'

"""
https://docs.python.org/3.6/library/collections.html#collections.defaultdict
https://yiyibooks.cn/xx/python_352/library/collections.html
在版本3.1中已更改：添加了对重命名的支持
"""

from collections import namedtuple

# Basic Example

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)

print(p[0] + p[1])

x, y = p

print("x->{}, y->{}".format(x, y))

print(p.x + p.y)

print(p)

