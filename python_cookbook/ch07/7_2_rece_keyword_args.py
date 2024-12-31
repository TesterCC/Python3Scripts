#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/10 09:16'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.2 只接受关键字参数的函数    P216
"""


# 希望函数的某些参数强制使用关键字参数传递

# 将强制关键字参数放到某个*参数或单个*后面

def recv(maxsize, *, block):
    'Receive a message'
    pass


# recv(1024, True)    # TypeError
recv(1024, block=True)  # OK
help(recv)   # 会打印输出到控制台


# 在接受任意多个位置参数的函数中指定关键字参数
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(mininum(1, 5, 2, -5, 10))  # return -5
print(mininum(1, 5, 2, -5, 10, clip=0))  # return 0
