#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/15 21:08'

"""
https://docs.python.org/3.6/library/collections.html

defaultdict  调用一个工厂函数来为dict的values的缺失提供值   用c语言实现，性能高

defaultdict是dict的子类，传递一个可调用对象, 简化数据初始化代码和规避一些异常
"""

from collections import defaultdict

# example 1 -- method3 更简单的写法

users = ["lily1", "lily2", "lily3", "lily1", "lily2", "lily2"]

default_dict = defaultdict(int)

for user in users:
    default_dict[user] += 1

print(f"Test resulte: \n {default_dict}")

print("*" * 90)


# example 2  10:56  4-1 defaultdict的功能详解
def gen_default():
    return {
        "name": "",
        "nums": 0
    }


default_dict2 = defaultdict(gen_default)

default_dict2['group_a']
