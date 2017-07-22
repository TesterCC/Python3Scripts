#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

# 1 过滤掉列表中的负数 -- 通用方式

data = [1, 5, -3, -2, 6, 0, 9]

res = []
for x in data:
    if x >= 0:
        res.append(x)

print(res)