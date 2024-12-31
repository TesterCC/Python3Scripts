#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-02-04 18:36'

"""
1.4 查找最大或最小的N个元素

Q: 怎样从一个集合中获得最大或最小的N个元素列表？
A: heapq模块的两个元素nlargest()和nsamllest()
"""

import heapq

nums = [18,2,23,7,-4,18,23,42,37,2]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]

# 以price的指进行比较
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# 以shares的值进行比较
share = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])

print(cheap)
print(expensive)
print(share)
