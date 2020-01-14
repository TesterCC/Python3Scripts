#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-13 17:52'

import collections

"""
4-1 Python内置数据结构算法常考

collections主要的:
namedtuple()
deque
Counter
OrderedDict
defaultdict

建议看源码了解底层结构和实现原理，面试问得深会问到。
举个例子：OrderedDict如何实现有序的？
使用循环双端链表保存key进入的顺序。
"""

print("*"*30 + " namedtuple " + "*"*30)
# 推荐的学习方式，看官方文档
# namedtuple, 让tuple属性可读
Point = collections.namedtuple('Point', 'x,y')

p = Point(1,2)

print(p.x)
print(p.y)

print(p[0],p[1])

print(p.x == p[0])


# deque，双端队列，可以方便地实现queue/stack
print("*"*30 + " deque " + "*"*30)

de = collections.deque()

# 后方（右侧）加入1
de.append(1)

# 前方（左侧）加入0
de.appendleft(0)

print(de)

# 右边弹出
print(de.pop())

# 左边弹出
print(de.popleft())

# Counter，需要计数器的地方使用
print("*"*30 + " Counter " + "*"*30)

c = collections.Counter('abcab')

print(c)

print(c['a'])
print(c['c'])

# 根据数量多少排序展示
print(c.most_common())


print("*"*30 + " OrderedDict " + "*"*30)

# OrderedDict的key顺序是第一次插入的顺序
# 使用OrderedDict实现LRUCache
od = collections.OrderedDict()
od['c'] = 'c'
od['a'] = 'a'
od['t'] = 't'

print(od)
print(od.keys())
print(list(od.keys()))

print("*"*30 + " defaultdict " + "*"*30)

# defaultdict, 带有默认值的字典
dd = collections.defaultdict(int)

print(dd['a'])  # 0

dd2 = collections.defaultdict(bool)
print(dd2['a']) # False