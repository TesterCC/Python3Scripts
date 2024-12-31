#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/15 21:56'


"""
https://docs.python.org/3.6/library/collections.html#collections.defaultdict
https://yiyibooks.cn/xx/python_352/library/collections.html

除了从tuple继承而来的方法，namedtuple还支持另外三个方法和两个属性。为了避免和字段冲突，这些方法和属性都以下划线开头
"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# 3 method, 2 property
# somenamedtuple._make(iterable)   类方法, 从现有的列表或迭代器创建一个新的实例
t = [11, 22]
obj = Point._make(t)
print(obj)

# somenamedtuple._asdict()  返回一个OrderedDict(有序字典)，每个键对应于该字段的值

