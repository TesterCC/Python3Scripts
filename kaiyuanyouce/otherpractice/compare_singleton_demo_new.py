#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-01 10:43'

"""
https://www.cnblogs.com/guomeina/p/7687012.html
使用__new__来控制实例的创建过程

单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。


https://www.cnblogs.com/shenbuer/p/7724091.html
方法一、实现__new__方法，然后将类的一个实例绑定到类变量_instance上；
如果cls._instance为None，则说明该类还没有被实例化过，new一个该类的实例，并返回；
如果cls._instance不为None，直接返回_instance
"""

class Singleton:
    def __new__(cls, *args, **kwargs):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj_1 = Singleton()
obj_2 = Singleton()

print(obj_1 == obj_2)
print(obj_1 is obj_2)