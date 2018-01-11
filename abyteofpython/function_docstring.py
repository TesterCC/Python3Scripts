#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/16 16:01'

# A Byte of Python -- Python3 - P65


def print_max(x, y):
    """
    Prints the maximum of two numbers. 打印两个数值中的最大数。
    
    The two values must be integers. 这两个数都因该是整数。
    """

    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
help(print_max)