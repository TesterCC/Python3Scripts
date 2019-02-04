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
