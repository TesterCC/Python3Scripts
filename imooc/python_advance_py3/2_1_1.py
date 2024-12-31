#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint
import time

data = [randint(-10, 10) for _ in range(300)]   # python3 on xrange()
print("Random Int Data List >>>> "+str(data))  # data is List class, need to convert
print("--------------------------------")

# Method 1 -- 使用filter函数，过滤掉负数 -- 30个左右filter效率高的多
start = time.clock()
r1 = filter(lambda x: x >= 0, data)
end = time.clock()
print("R1 run time: %f" % (end-start))
print(list(r1))     # in python3, filter() return need user list() to display


# Method 2 -- 使用列表解析，过滤掉负数 -- 10个元素的话 quicker
start = time.clock()
r2 = [x1 for x1 in data if x1 >= 0]
end = time.clock()
print("R2 run time: %f" % (end-start))
print(r2)
print("--------------------------------")



