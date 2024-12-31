#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-19 13:07'

"""
Detail explain: 
https://www.cnblogs.com/kaituorensheng/p/6139573.html

Why set literal is faster in performance testing?
"""

import timeit
import dis


def f():
    return set([1, 2, 3])


def h():
    return set((1, 2, 3))


def g():
    return {1, 2, 3}

# print(f())
# print(h())
# print(g())

print(min(timeit.repeat(f)))
print(min(timeit.repeat(h)))
print(min(timeit.repeat(g)))     # set literals is the best

print("*"*90)
# reason
dis.dis(f)
print(">"*90)
dis.dis(h)
print(">"*90)
dis.dis(g)
print("*"*90)


'''
分析:
f()需要载入全局函数set，把三个元素放入栈中，然后调用set()函数，就生成了set()

h()也需要载入全局函数set，不是把三个元素载入栈，而是把一个元组常量放入栈，然后调用set()函数，就生成了set()

g()是直接把三个元素放入栈，然后就生成了set()


总结:
尽管这里生成set()的方式对性能的提升很小，set literals不用花费时间调用函数处理中间数据，并且这种写法是非常漂亮的，所以建议用set literals的方式
'''

