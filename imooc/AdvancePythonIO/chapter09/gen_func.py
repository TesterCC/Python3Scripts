#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/20 13:18'


# 生成器函数，函数里只要有yield关键字
def gen_func():
    yield 1
    yield 2    # use
    # 为惰性求值和延迟求值提供了可能，举例：斐波拉契数列 08:29


def func():
    return 1
    return 2    # no use


if __name__ == '__main__':
    # 调生成器函数返回生成器对象，生成器对象是python编译字节码的时候就产生了  python代码运行前会将代码变成字节码
    gen = gen_func()
    for value in gen:
        print(value)
    re = func()
    pass
