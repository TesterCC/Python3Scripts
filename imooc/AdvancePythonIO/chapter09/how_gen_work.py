#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-25 14:40'

"""
9-4 Python生成器原理 2:20
1. python中函数的工作原理
"""

import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


# python解释器是用C来写的
# python.exe会用一个叫做PyEval_EvalFramEx(C函数)去执行foo函数
# 首先会创建一个栈帧(stack frame),这个栈帧实际上是一个上下文
"""
python一切皆对象，栈帧对象，字节码对象。
当foo函数调用子函数bar，又会创建一个栈帧。

所有栈帧都是存放在堆内存上，这就决定了栈帧可以独立于调用者存在
"""

import dis

# print(dis.dis(foo))  # 查看foo的字节码

foo()
print(frame.f_code.co_name)

caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 33
    return "imooc"  # 早期版本这样return会抛异常


gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

a = [1, 2, 3]

# 只要实现__getitem__()就可以进行for循环遍历，顺序是先找iter(),再找__getitem__()
for i in a:
    print(i)


from collections import UserList   # 以Python方式解释list如何实现, 且可以集成，方便自定义List
