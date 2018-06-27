#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/27 09:31'

"""
编写高质量代码：改善Python程序的91个建议  P3
充分利用Python语法，而不应过分地使用奇技淫巧

实现功能: 列表和字符串逆序
"""

# Method 1
a = [1, 2, 3, 4]
b = 'abcdef'

print(a[::-1])
print(b[::-1])    # str

# Method 2
print(list(reversed(a)))
print(list(reversed(b)))   # list