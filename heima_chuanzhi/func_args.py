#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/4 16:06'

'''
02基础-05-带有参数的函数
'''


def sum_2_nums(a, b):
    """用来完成对2个数求和"""
    result = a+b
    print("%d+%d=%d" % (a, b, result))


num1 = int(input("请输入第1个数字："))
num2 = int(input("请输入第2个数字："))

sum_2_nums(num1, num2)