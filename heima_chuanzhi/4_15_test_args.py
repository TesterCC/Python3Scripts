#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/4 20:33'


"""
05-15-拆包，元组、字典
"""


def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# test(11, 22, 33, 44, 55, 66, 77, task=99, done=89)

A = (44, 55, 66)
B = {"name": "Alice", "age": 18}

test(11, 22, 33, *A, **B)