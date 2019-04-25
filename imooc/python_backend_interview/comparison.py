#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-25 17:32'

"""
A Demo of List Comprehension
"""

a = ['a', 'b', 'c']
b = [1, 2, 3]

# d = {'a':1, 'b':2, 'c':3}
d = {}
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)

# simplify
d = {k: v for k, v in zip(a, b)}
print(d)

l = [i for i in range(10)]
print(l)
print(type(l))

l = (i for i in range(10))
print(type(l))

for i in l:
    print(i, end='')