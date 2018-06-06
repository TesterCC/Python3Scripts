#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/5 22:32'

"""
14章 Pythonic与Python杂记
"""


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknown'


switcher = {
    0: get_sunday,  # 注意这里是函数，不是函数的调用
    1: get_monday,
    2: get_tuesday,
}

# day = 1
day = 8

day_name = switcher.get(day, get_default)()

print(day_name)
