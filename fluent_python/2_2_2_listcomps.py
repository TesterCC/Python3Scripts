#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/14 09:41'

"""
列表推导式 list comprehension (listcomps)
生成器表达式 generator expression (genexps)
P72-73  2.2.2 列表推导同filter和map的比较

filter和map合起来能做的事情，列表推推导式也可以做到，且不需要难以理解和阅读的lambda表达式
"""

import time

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print("function used: {} s".format(end-start))
        return wrapper

symbols = "$＊$€¥¢£₽₵₤"


start1 = time.clock()
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
end1 = time.clock()
elapsed_time1 = end1-start1

print(beyond_ascii)
print(elapsed_time1)

# 则种方法明显复杂了
start2 = time.clock()
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
end2 = time.clock()
elapsed_time2 = end2-start2

print(beyond_ascii)
print(elapsed_time2)

print(elapsed_time1>elapsed_time2)



