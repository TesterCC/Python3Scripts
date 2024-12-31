#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

# num = [1,2,3,4]
num = range(1, 5)
b = []

for i in num:
    for j in num:
        for k in num:
            if i != j and j != k and k != i:
                # result = i*10**2 + j*10 + k
                result = i*100 + j*10 + k
                b.append(result)

print(len(b))
print(b)