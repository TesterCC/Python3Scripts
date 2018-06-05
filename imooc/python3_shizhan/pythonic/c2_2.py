#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/5 22:32'

"""
14章
"""


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


switcher = {
    0: get_sunday,  # 注意这里是函数，不是函数的调用
    1: get_monday,
    2: get_tuesday,
}

day = 1

day_name = switcher.get(day, 'Unknown')()

print(day_name)
