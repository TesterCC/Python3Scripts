#!/usr/bin/env python
# coding:utf-8


from random import randint
from collections import Counter

# http://coding.imooc.com/lesson/62.html#mid=837
# 1.某随机序列[12,5,6,5, ...]中，找到出现次数最高的3个元素，它们出现次数是多少？

data = [randint(0, 20) for _ in range(30)]
print(data)

# data作key，0作value
c = dict.fromkeys(data, 0)    # 方法用于创建一个新的字典
print(c)

# 统计出现次数
for x in data:
    c[x] += 1

print(c)
print("------------------------------")

# 找到出现次数最高的3个元素
# 一般来说就是对字典data中的值进行排序
# Here use collections.Counter object.
c2 = Counter(data)     # 词频统计结果
# print(c2[10])

res = c2.most_common(3)    # 找到出现频度最高的三个元素  list object
print("出现次数最高的3个(元素:次数): "+str(res))








