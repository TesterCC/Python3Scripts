#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/25 17:29'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    05-装饰器 02 函数式编程
公司有N个业务部门:
1个基础平台部门，基础平台负责提供底层的功能，如：数据库操作、redis调用、监控API等功能。
业务部门使用基础功能时，只需调用基础平台提供的功能即可。
"""


# 代码要遵循开放封闭原则
# 规定已经实现的功能代码不允许被修改，但可以被扩展
def w1(func):
    def inner():
        # verification 1
        print("---正在验证权限---")
        # verification 2
        # verification 3
        func()
    return inner


# 基础平台提供的功能如下
# 增加装饰器扩展功能
# @函数名 是python的一种语法糖
# 将 @w1 下面的函数作为w1函数的参数，即：@w1 等价于 w1(f1) 所以，内部就会去执行

@w1
def f1():
    print('f1')


@w1
def f2():
    print('f2')


@w1
def f3():
    print('f3')


@w1
def f4():
    print('f4')


# 仅仅对基础平台的代码进行修改，就可以实现在其他人调用函数 f1 f2 f3 f4 之前都进行 验证 操作，并且其他业务部门无需做任何操作。

if __name__ == '__main__':
    f1()
    f2()
    f3()
    f4()

