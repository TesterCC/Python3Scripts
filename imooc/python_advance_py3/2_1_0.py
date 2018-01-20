#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

# 1 过滤掉列表中的负数 -- 通用方式

data = [1, 5, -3, -2, 6, 0, 9]
L = [3, 7, 9, -1, 20, 30, -2, -7, 18]

res = []
for x in data:
    if x >= 0:
        res.append(x)

print(res)


resp = []
for i in L:
    if i >= 0:
        resp.append(i)

print(resp)



