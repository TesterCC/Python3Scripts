#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-11 16:47'

"""
工作日的力量
"""

dayup = 1.0
dayfactor = 0.01

for i in range(365):
    if i % 7  in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)


print("工作日的力量{:.2f}".format(dayup))