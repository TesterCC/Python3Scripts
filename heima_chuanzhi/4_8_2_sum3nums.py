#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/4 16:06'

'''
02基础-04-15
1.写一个函数求三个数的和
2.写一个函数求三个数的平均值
'''


def sum_3_nums(a, b, c):
    """求三个整数的和"""
    result = a+b+c
    # print("%d+%d+%d=%d" % (a, b, c, result))
    return result


def average_3_nums(a, b, c):
    result = sum_3_nums(a, b, c)
    avg = result/3   # result /= 3
    print("平均值是: %d" % avg)


num1 = int(input("请输入第1个数字："))
num2 = int(input("请输入第2个数字："))
num3 = int(input("请输入第3个数字："))


sum_3_nums(num1, num2, num3)   # 无print

average_3_nums(num1, num2, num3)