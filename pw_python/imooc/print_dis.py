#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-10 00:08'

"""
Python中什么操作才是原子的？
一步到位执行完。

1.一个操作如果是一个字节码指令可以完成的，就是原子的。
2.原子的是可以保证线程安全的
3.使用dis操作来分析字节码

非原子操作不是线程安全的
可以通过加锁保证线程安全
"""

import dis

def update_list(l):
    l[0] = 1 # 原子操作，不用担心线程安全问题

dis.dis(update_list)
"""
 18           0 LOAD_CONST               1 (1)
              2 LOAD_FAST                0 (l)
              4 LOAD_CONST               2 (0)
              6 STORE_SUBSCR                        # 单字节码操作，线程安全
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""


def incr_list(l):
    l[0] += 1   # 注意，不是原子操作

dis.dis(incr_list)
"""
 32           0 LOAD_FAST                0 (l)
              2 LOAD_CONST               1 (0)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_CONST               2 (1)
             10 INPLACE_ADD                      # 需要多个字节码操作，有可能在线程执行过程中切到其他线程
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
"""
