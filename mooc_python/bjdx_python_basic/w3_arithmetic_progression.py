#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-08 11:07'

"""
等差数列末项计算
给出一个等差数列的前两项a1，a2，求第n项是多少

arithmetic progression

输入格式:

三行，包含三个整数a1，a2，n

输出格式：

一个整数，即第n项的值

输入样例：

1
4
100

输出样例：

298

"""

a1 = int(input())
a2 = int(input())
m = a2 - a1
n = int(input())
N = a1 + m * (n - 1)
print(N)
