#!/usr/bin/env python
# coding:utf-8


from random import randint
from collections import Counter

# http://coding.imooc.com/lesson/62.html#mid=837
# 1.某随机序列[12,5,6,5, ...]中，找到出现次数最高的3个元素，它们出现次数是多少？

data = [randint(0, 20) for _ in range(30)]
print(data)

# data作key，0作value
d = dict.fromkeys(data, 0)    # 方法用于创建一个新的字典, 这个字典中的key为data中的元素，值全是0
print(d)

# 统计出现次数
for x in data:
    d[x] += 1

print(d)

print("-----------根据频度排序，降序-------------------")

print("="*15 + "method 1" + "="*15)
# ret = sorted([(v, k) for k, v in d.items()], reverse=True)

ret = sorted(((v, k) for k, v in d.items()), reverse=True)
# 用生成器解析比列表解析更节约空间
# 但这种方法总得来说不好，需要对整个列表进行排序

print(ret)

print("----找到出现次数最高的3个元素----")
print(ret[:3])

print("="*15 + "method 2" + "="*15)
# Python3实用编程技巧进阶 2-4 如何统计序列中元素的频度 04:24
# 在很大的列表中找到前3个，通常使用堆这个数据结构

import heapq

ret1 = heapq.nlargest(3, ((v, k) for k, v in d.items()))

ret2 = heapq.nsmallest(3, ((v, k) for k, v in d.items()))

print("----找到出现次数最高的3个元素----")
print(ret1)

print("----找到出现次数最低的3个元素----")
print(ret2)


print("="*15 + "method 3" + "="*15)
print("----找到出现次数最高的3个元素----")
# 找到出现次数最高的3个元素
# 一般来说就是对字典data中的值进行排序
# Here use collections.Counter object.    05:25
c2 = Counter(data)     # 词频统计结果
# print(c2[10])

print(c2)
res = c2.most_common(3)    # 找到出现频度最高的三个元素  list object
print("出现次数最高的3个(元素:次数): "+str(res))








