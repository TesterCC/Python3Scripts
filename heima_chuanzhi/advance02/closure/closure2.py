#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/23 22:48'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    02-闭包
"""


# define a function
def test(number):
    """
    在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
    那么将这个函数以及它用到的一些变量称之为闭包
    :param number:
    """
    print("--1--")

    def test_in(number_in):
        print("--2--")
        print('in test_in function, number_in is %d' % number_in)
        return number + number_in

    print("--3--")
    # 其实这里返回的就是闭包的结果
    return test_in     # 返回的是函数test_in,不是函数的调用


print("start to run test()")
# 给test函数赋值，这个20就是给参数number
ret = test(20)

print("start to run ret(100)")
# 注意这里的100其实给参数number_in
print(ret(100))

print("start to run ret(200)")
# 注意这里的200其实给参数number_in
print(ret(200))
