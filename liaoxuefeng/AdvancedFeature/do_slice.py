#!/usr/bin/env python
# coding:utf-8

# 切片 Slice
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
# 笨办法
print(L[0], L[1], L[2])

print("-----use slice-----")

# use slice
print(L[0:3])   # 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[:3])    # 如果第一个索引是0，还可以省略
print(L[1:3])   # 可以从索引1开始，取出2个元素出来
print(L[-1])    # L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:-1])  # get L[-2],记住倒数第一个元素的索引是-1
print(L[-3:-1])
print(L[-1:-2])  # empty, 顺序不能乱

print("--------------------")
# 先创建一个0-99的数列
L1 = list(range(100))
print(L1)

print(L1[:10])   # 取出某一段数列前10个数
print(L1[-10:])  # 后10个数
print(L1[10:20])  # 前11-20个数
print(L1[:10:2])   # 前10个数，每2个取一个
print(L1[::5])     # 所有数，每5个取一个
print(L1[:])       # 什么都不写，只写[:]就可以原样复制一个list

print("----------Tuple-----------")
T = (0, 1, 2, 3, 4, 5)
print(T[:3])

print("------------slice str-----------")
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
S = 'ABCDEFG'
print(S[:3])
print(S[::2])