#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 18:28'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
sorted

排序也是在程序中经常用到的算法。
无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
"""

# Python内置的sorted()函数就可以对list进行排序
L = [36, 5, -12, 9, -21]
print(sorted(L))   # 默认升序排列

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
r = sorted([36, 5, -12, 9, -21], key=abs)    # 按绝对值大小升序排列
print(r)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的。
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。A-Z < a-z
r2 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(r2)

print("---------忽略大小写，按照字母序排序----------")
r3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(r3)

print("---------忽略大小写，按照字母序反向排序----------")
r4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(r4)


