#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 18:27'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
reduce()
"""

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

# 一个序列求和


def add(x, y):
    return x+y

r = reduce(add, [1, 3, 5, 7, 9])       # 求和运算可以直接用Python内建函数sum()，没必要动用reduce
print(r)

print("-------test-------")

# 可以做编程题
# 把序列[1, 3, 5, 7, 9]变换成整数13579


def fn(x, y):
    return x*10+y

r2 = reduce(fn, [1, 3, 5, 7, 9])

print(r2)
print(type(r2))

print("--------str to int----------")
# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

def fn(x, y):
    return x*10 + y

def char2num(s):
    return {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
            }[s]

r3 = reduce(fn, map(char2num, '13579'))
print(r3)
print(type(r3))