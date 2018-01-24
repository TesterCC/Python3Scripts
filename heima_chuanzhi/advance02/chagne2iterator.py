#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/21 03:25'


"""
生成器都是 Iterator 对象
把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数
凡是可作用于 for 循环的对象都是 Iterable 类型；
凡是可作用于 next() 函数的对象都是 Iterator 类型
集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。
"""

a = [11, 22, 33, 44]
type(a)

print("user iter()")
b = iter(a)
print(b)

print("单独调next()")
print(next(b))

print("遍历")
for e in b:
    print(e)
