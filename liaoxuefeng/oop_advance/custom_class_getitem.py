#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 17:44'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素  Fib()[5]

要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
"""

# 以斐波那契数列为例，写一个Fib类，可以作用于for循环


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

f = Fib()
print(f[0])
print(f[20])
print(f[300])

# 但是list有个神奇的切片方法
# list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断