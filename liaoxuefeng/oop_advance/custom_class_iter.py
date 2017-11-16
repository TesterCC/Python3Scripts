#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 12:05'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
"""

# 以斐波那契数列为例，写一个Fib类，可以作用于for循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1    # 初始化两个计数器a,b

    def __iter__(self):
        return self    # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b   # 计算下一个值
        if self.a > 100000:   # 退出循环的条件
            raise StopIteration()
        return self.a      # 返回下一个值

for n in Fib():
    print(n)

