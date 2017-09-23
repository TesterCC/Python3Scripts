#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/24 05:08'


'''
小甲鱼Python 050模块：模块就是程序
摄氏度和华氏度的转换
'''

from fishc.ex50 import TemperatureConversion as tc

print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))