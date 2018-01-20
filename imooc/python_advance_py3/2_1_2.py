#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint


# 筛出字典{'Lilei':79, 'Lucy':92 ...}中值高于90的项
# 随机生成一个字典

d = {x: randint(60, 100) for x in range(1, 21)}
print(d)

r = {k: v for k, v in d.items() if v > 90}

print("高于90的结果：")
print(r)

print("-"*70)

d1 = {'Alice': 77, 'Bob': 69, "Mary": 82, "Tom": 91, "Lily": 93}
r1 = {k: v for k, v in d1.items() if v > 90}

print(r1)