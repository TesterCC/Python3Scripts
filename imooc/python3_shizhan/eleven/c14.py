#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/1 08:58'

"""
闭包
L E G B
01:33:00
"""


def f1():
    a = 10

    def f2():
        # a 此时将被python认为是一个局部变量
        a = 20
        print(a)

    print(a)
    f2()
    print(a)


f1()

# def时不运行print()
# 10 20 10
