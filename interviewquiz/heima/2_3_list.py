#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-07 17:43'

# P29

l = []

for i in range(10):
    l.append({'num': i})

print(l)
# [{'num': 0}, {'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}, {'num': 7}, {'num': 8}, {'num': 9}]

print("--" * 60)

l = []
a = {'num': 0}

for i in range(10):
    a['num'] = i
    l.append(a)   # 把字典a的引用传到列表l中，

print(l)
# [{'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}]

'''
两段代码运行结果不相同，因为字典是可变对象。
在下方的l.append(a)的操作中是把字典a的引用传到列表l中，当后续操作修改 a[‘num’]的值的时候，l中的值也会跟着改变，相当于浅拷贝。
'''