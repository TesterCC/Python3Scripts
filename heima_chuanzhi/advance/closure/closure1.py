#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/23 18:44'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    02-闭包
"""


def test():
    print("--1--")


print("打印test():")
print(test())   # 调用函数使之执行

print("打印test:")
print(test)

b = test    # b --> func body

print("打印b:")
print(b)

print("打印b():")
print(b())
