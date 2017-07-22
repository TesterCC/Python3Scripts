#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint

data = [randint(-10, 10) for _ in range(10)]   # python3 on xrange()
print("Random Int Data List >>>> "+str(data))  # data is List class, need to convert
print("--------------------------------")