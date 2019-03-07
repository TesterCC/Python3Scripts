#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-07 17:18'

"""
the basic syntax
P28
"""

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print("A0:\n{}".format(A0))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)    # python3 is a iterator object, python2 is a list
# python3 range() equal to python2 xrange()
print("list A1:\n{}".format(list(A1)))
# list A1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

A2 = [i for i in A1 if i in A0]
print("A2:\n{}".format(A2))
# []

A3 = [A0[s] for s in A0]
print("A3:\n{}".format(A3))
# [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
print("A4:\n{}".format(A4))
# [1, 2, 3, 4, 5]

A5 = {i:i*i for i in A1}
# {0:0, 1:1, 2:4, 3:9, 4:16, ..., 9:81}
print("A5:\n{}".format(A5))

A6 = [[i, i*i] for i in A1]
# [[0,0],[1,1],[2,4],[3,9],...,[9,81]]
print("A6:\n{}".format(A6))