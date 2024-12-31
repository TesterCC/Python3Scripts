#!/usr/bin/env python
# coding=utf-8

'''
Author: Yanxi
Date: 2017/06/15
Describe: 实现简单计算器 + - * /
Web接口开发与自动化测试-基于Python语言  P97-P98
'''


class Calculator():
    '''  实现两个数的加减乘除  '''

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b


