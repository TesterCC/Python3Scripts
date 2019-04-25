#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-25 17:18'

"""
A Demo of Introspection
自省：运行时判断一个对象的类型的能力
"""

ll = [1, 2, 3]

d = dict(a=1)  # {a:1}

print(type(ll))
print(type(d))

print(isinstance(ll, list))
print(isinstance(d, dict))


# my demo
def add(a, b):
    if isinstance(a, int):
        return a + b
    elif isinstance(a, str):
        return a.upper() + b


print(add(1, 2))
print(add("head", "tail"))

print(id(ll))
print(id(d))
print(ll is d)
print(ll is ll)

