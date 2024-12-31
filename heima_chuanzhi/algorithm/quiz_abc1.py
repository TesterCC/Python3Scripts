#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/21 03:36'

"""
1-算法引入

如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），
如何求出所有a、b、c可能的组合

> 200s
"""

import time

# T(n) = 1000 * 1000 * 1000 * 2 = c * n**3
# T(n) = k * g(n) + c
# 渐进函数g(n) = n**3
# T(n) = g(n)
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" % (a, b, c))
end_time = time.time()

print("times: %s seconds" % (end_time - start_time))
print("finished")
