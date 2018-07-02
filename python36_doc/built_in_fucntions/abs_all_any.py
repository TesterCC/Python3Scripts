#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/26 09:36'

"""
Python 3.6.3 doc in Dash
a开头的Python内置函数
"""

print('abs() demo:')
print(abs(-2))
print(abs(3))

print('all() demo:')
"""
    Return True if bool(x) is True for all values x in the iterable.

    If the iterable is empty, return True.
"""
# Return True if all elements of the iterable are true (or if the iterable is empty).
# http://www.runoob.com/python/python-func-all.html

list1 = [1, True, 't']
list2 = []

list3 = [False, '']
list4 = ['']
list5 = [None]
list6 = [1, True, False, '']

print(all(list1))  # True
print(all(list2))  # True

print(all(list3))  # False
print(all(list4))  # False
print(all(list5))  # False
print(all(list6))  # False

print('any() demo:')
# Return True if any element of the iterable is true. If the iterable is empty, return False.
# http://www.runoob.com/python/python-func-any.html
print(any(list2))  # False
print(any(list3))  # False
print(any(list4))  # False
print(any(list5))  # False
print(any(list6))  # True


print('ascii() demo:')
# ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
text = '测试DevOps0'
print(ascii(text))
