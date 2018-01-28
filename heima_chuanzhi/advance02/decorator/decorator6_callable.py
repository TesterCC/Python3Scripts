# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/28 23:59'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    09-装饰器对有参数、无参数函数进行装饰
    5. 装饰器示例  例6：类装饰器（扩展，非重点）
    
    装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
    在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，那么这个对象就是callable的。
"""


class Test():
    def __call__(self):
        print('call me!')


t = Test()
t()   # call