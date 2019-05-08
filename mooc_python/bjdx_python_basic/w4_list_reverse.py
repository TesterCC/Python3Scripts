#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-08 11:05'

"""
输入一个列表，将其反转后输出新的列表。
输入样例：
1 2 3

输出样例：
[3, 2, 1]
"""

alist = list(map(int, input().split()))
alist.reverse()
print(alist)
