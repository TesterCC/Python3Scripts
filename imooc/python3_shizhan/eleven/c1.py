#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/17 13:45'

"""
类型
绿钻、黄钻、红钻、黑钻

Python2 字典
Python3 枚举   单例模式
"""

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    BLUE = 'blue'


print(VIP.YELLOW)
print(VIP.GREEN)
print(VIP.BLUE)

print('-----------------')
print(VIP.GREEN.value)
print(VIP.BLUE.value)

print('-----------------')
print(VIP.GREEN.name)
print(VIP.BLUE.name)
