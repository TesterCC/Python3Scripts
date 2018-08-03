#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/3 10:37'

"""
怎么在两个字典中寻找相同点（如相同的值，相同的键）
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 寻找字典的相同点，在两个字典的keys() or items()返回的结果上执行集合操作。
# Find keys in common
print(a.keys() & b.keys())

# Find keys in a that are not in b
print(a.keys() - b.keys())

# Find (key, value) pairs in common
print(a.items() & b.items())






