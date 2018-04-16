#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/13 23:46'

"""
《Python+Cookbook》第三版中文v3.0.0
1.2 解压可迭代对象赋值给多个变量
P16
"""

# 星号表达式在迭代元素为可变长元组的序列时是很有用的。

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

