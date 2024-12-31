#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-08 17:45'

"""
打印完数：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如 6 = 1＋2＋3。（10分）
题目内容：

输入一个正整数n（n<1000），输出1到n之间的所有完数（包括n）。

输入格式:

共一行，为一个正整数。

输出格式：

若干行，从小到大输出完数，一行为一个数。

输入样例：

30

输出样例：

6

28

REF: 
https://blog.csdn.net/byakki/article/category/8603686/4?
https://blog.csdn.net/byakki/article/details/86607770
"""

n = int(input())
for i in range(1, n + 1):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(s)
