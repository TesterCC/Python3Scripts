#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 18:27'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
map()
"""

# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x*x

r = map(f, L)

print(list(r))

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
# map()作为高阶函数，事实上它把运算规则抽象了