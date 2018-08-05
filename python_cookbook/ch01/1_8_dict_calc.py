#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/5 23:33'

"""
1.8 怎么在字典中进行一些计算操作（求最大值、最小值、排序等）
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。
如需展示列表，需手动 list() 转换。
"""
# 用zip函数将键和值反转过来，再计算
# min price
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

# max price
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 用sorted()来排列字典数据, 默认从小到大
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
print(prices_sorted)

