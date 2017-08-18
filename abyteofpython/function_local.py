#!/usr/bin/env python
# coding=utf-8

# A Byte of Python -- P60 -- Python3

x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)    # 不受局部变量影响
print('x is still', x)