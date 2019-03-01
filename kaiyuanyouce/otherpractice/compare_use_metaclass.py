#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-01 11:16'

"""
REF:
https://www.cnblogs.com/shenbuer/p/7724091.html  (更好)
https://www.cnblogs.com/guomeina/p/7687012.html


元类可以控制类的创建过程，它主要做三件事：

　　- 拦截类的创建

　　- 修改类的定义

　　- 返回修改后的类



方法二、使用元类实现单例模式
本质上是方法一（实现__new__方法，然后将类的一个实例绑定到类变量_instance上）的升级版，使用metaclass（元类）的python高级用法

class Singleton中的__init__在Foo声明的时候被执行Foo=Singleton()
Foo()执行时，最先执行父类的__call__方法（object,Singleton都作为Foo的父类，
根据深度优先算法，会执行Singleton中的__call__()，Singleton中的__call__()写了单例模式）
"""

class Singleton(type):   # 所有基础方法继承自type

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance

# right in python3
# 在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。
class Foo(object, metaclass=Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(id(foo1))
print(id(foo2))

print(Foo.__dict__)
print("*"*30)

print(foo1 is foo2)  # False  不知道为什么



