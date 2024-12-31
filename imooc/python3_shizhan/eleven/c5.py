#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/17 13:42'

from enum import Enum

"""
枚举的比较运算
"""


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


result = VIP.GREEN == VIP.GREEN
print(result)

