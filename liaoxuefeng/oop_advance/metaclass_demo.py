#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/17 11:59'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000

metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
先定义metaclass，就可以创建类，最后创建实例。
metaclass允许你创建类或者修改类。
换句话说，你可以把类看成是metaclass创建出来的“实例”。

"""


# 这个metaclass可以给我们自定义的MyList增加一个add方法

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
# metaclass是类的模板，所以必须从type类型派生

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。

# 测试一下MyList是否可以调用add()方法
L = MyList()
L.add(1)
print(L)

# L2 = list()
# L2.add(1)

