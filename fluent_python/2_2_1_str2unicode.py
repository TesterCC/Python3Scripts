#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/14 09:26'

"""
P70 2-1 把一个字符串变成Unicode码位列表
"""

# e.g. 2-1
symbols = "$！@＃$％&＊$€¥¢£₽₵₤"

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# e.g. 2-2
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

# e.g. 2-3  P72-73
# python2 issue:在列表推导中，for关键词之后的赋值操作可能会影响列表推到上下文中的同名变量。
# python3 不会有这个问题，python3中有自己的局部作用域，表达式内部的变量和赋值只在局部起作用，表达式的上下文里面的同名变量还可以被正常引用
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)





