#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/27 17:53'


a = 1   # immutable object


def fun(a):
    print("func_in", id(a))  # func_in 41322472
    a = 2
    print("re-point", id(a), id(2))   # re-point 41322448

print("func_out", id(a), id(1))    # func_out 41322472 41322472
fun(a)
print(a)   # 1

# 类型是属于对象的，而不是变量
# 而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。
# 在python中，strings, tuples, 和numbers是不可更改（immutable）的对象，
# 而 list, dict, set 等则是可以修改（mutable）的对象。