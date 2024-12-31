#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/20 21:04'


# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint

data = [randint(-100, 100) for _ in range(30000)]

# Method 4 -- 筛出集合{77,89,32,20...}中能被3整除的元素   集合Set
s = set(data)
# print("未过滤set数据：")
# print(s)
result = {x for x in s if x % 3 == 0}
print("过滤后set数据：")
print(result)

# print("-"*70)

# blog
# data = [66, 77, 89, 33, 17, 20, 11]
# s = set(data)
# result = {x for x in s if x % 3 == 0}
# print("过滤后set数据：")
# print(result)

