#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/27 01:22'

"""
https://www.cnblogs.com/c-x-a/p/9333826.html

f-Strings：一种改进Python格式字符串的新方法
F字符串在这里可以节省很多的时间,使格式化更容易。
自Python 3.6开始加入标准库。您可以在PEP 498中阅读所有内容。
"""

name = "Tester"
age = 77

print(f"Hello, I'm {name}, {age} years old.")

# 大写字母F也是有效的
print(F"Hello, I'm {name}, {age} years old.")

# 由于f字符串是在运行时进行渲染的，因此可以将任何有效的Python表达式放入其中。这可以让你做一些漂亮的事情。
print(f"{2 * 64}")

print(f"{name.lower()} is seriously.")
print(f"{name.upper()} is cute.")

# 可以使用带有f字符串的类创建对象。



