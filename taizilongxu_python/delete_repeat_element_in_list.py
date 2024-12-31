#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/27 19:03'

"""
要求是把列表里的重复元素删除，只保留没有重复的元素。
例如：
a=['a','b','c','d','a','a']
如何变成：
a=['b','c','d']

level easy
"""

# Method 1 -- 只保留没有重复的元素
a = ['a', 'b', 'c', 'd', 'a', 'a']
b = [x for x in a if a.count(x) == 1]
print(b)

# Method 2  --  保留所有不重复的，重复的只保留一个  # 删除一个list里面的重复元素
a2 = ['a', 'b', 'c', 'd', 'a', 'a']
b2 = list(set(a2))
print(b2)





