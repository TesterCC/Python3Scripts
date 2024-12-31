#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-14 23:42'

from random import random
from time import perf_counter

# 当前抛洒点的总数量
DARTS = 1000 * 1000

# 在圆内部的点的总数量
hits = 0.0

start = perf_counter()

# 对所有点进行抛洒
for i in range(1, DARTS+1):
    x,y = random(), random()
    # 看这个点到圆心的距离是否等于1，以此判断点是否落在圆内
    dist = pow(x**2+y**2, 0.5)   # 开方
    if dist <= 1.0:
        hits += 1

pi = 4 * (hits/DARTS)
print("圆周率近似值是：{}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter()-start))