#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-09 10:53'

"""
递归的两个管家特征：
链条：计算过程存在递归链条
基例：存在一个或多个不需要再次递归的基例子

程序结构：函数+分之结构

关于阶乘徐需要明确的概念
1.任何一个非零数的零次方为1
2.0的阶乘为1
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(10))
