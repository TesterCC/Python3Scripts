#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/5 22:32'

"""
14章
"""

day = 6

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
}

# day_name = switcher[day]

day_name = switcher.get(day, 'Unknown')

print(day_name)


