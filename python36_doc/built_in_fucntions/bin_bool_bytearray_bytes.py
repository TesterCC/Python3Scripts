#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/2 15:31'

"""
Python 3.6.3 doc in Dash
b开头的Python内置函数
"""

print('bin() example:')
# Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression.
# If x is not a Python int object, it has to define an __index__() method that returns an integer.

print(bin(3))
print(bin(-10))
print(bin(123456789876543210))

print(format(14, '#b'))  # 前缀'0b'是需要的
print(format(14, 'b'))  # 不需要前缀'0b'

print('bool() example:')
print(bool(''))
print(bool(0))
print(bool(None))
print(bool(False))

print(bool('x'))
print(bool(1))
print(bool(type))
print(bool(True))

print('bytearray() example:')
# Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.
# It has most of the usual methods of mutable sequences
print(bytearray())
print(bytearray([1, 2, 3]))
print(bytearray('DevOps', 'utf-8'))
