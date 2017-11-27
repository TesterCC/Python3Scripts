#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/27 20:42'


"""
Python代码实现:删除一个list里面的重复元素

方法一：是利用map的fromkeys来自动过滤重复值，map是基于hash的，大数组的时候应该会比排序快点吧
方法二：是用set(),set是定义集合的,无序，非重复
方法三：新建一个list，便利原list，判断新list中是否存在原list中的元素，如果有，则重复了，不添加到新list,

Q: 给定一个列表，去掉其重复的元素，并输出

"""

a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]


# 方法一：是利用map的fromkeys来自动过滤重复值，map是基于hash的，大数组的时候应该会比排序快点吧
# 个人推荐

def sortFun1(a):
    b = {}
    b = b.fromkeys(a)
    # print(b)
    # print(b.keys())
    r = list(b.keys())
    print(r)

sortFun1(a)


# 方法二：是用set(),set是定义集合的,无序，非重复
def sortFun2(a):
    r = list(set(a))
    print(r)

sortFun2(a)


# 判断list元素是否在list中，如果有，则重复了。
def sortFun3(a):
    l2 = []
    for i in a:
        if i not in l2:
            l2.append(i)
        else:
            continue
    print(l2)

sortFun3(a)








