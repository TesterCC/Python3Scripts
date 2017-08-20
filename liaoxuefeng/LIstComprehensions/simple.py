#!/usr/bin/env python
# coding:utf-8

# 列表生成式
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000

import os

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))


# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
# complex method
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# simple method
L2 = [x * x for x in range(1, 11)]
print(L2)
print("-------------------")

# 筛选出仅偶数的平方
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)
print("-------------------")

# 使用两层循环，可以生成全排列
L4 = [m+n for m in "ABC" for n in "1234"]
print(L4)
print("-------------------")

# 9x9 table
L5 = [("%d * %d = %d" % (m, n, m*n)) for m in range(1, 10) for n in range(m, 10)]
print("\n".join(L5))
print("-------------------")

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])   # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}

