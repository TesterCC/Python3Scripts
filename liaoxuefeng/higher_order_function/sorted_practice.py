#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/9 21:39'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
sorted

假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序
再按成绩从高到低排序
"""

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print("======by name======")


def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)


print("======by score======")


def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score)
print(L3)


print("--------简化----------")
L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
r1 = sorted(L, key=lambda x: x[0].lower())
print(r1)
r2 = sorted(L, key=lambda x: x[1])
print(r2)






