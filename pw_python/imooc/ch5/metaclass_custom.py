#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/9 01:30'

"""
#### 元类(Meta Class)是创建类的类

- 元类允许我们控制类的生成，比如修改类的属性等
- 使用type来定义元类
- 元类最常见的一个使用场景就是ORM框架

__new__ 生成实例
__init__ 初始化实例
"""
# 如何编写元类
# 功能：把类的属性名称改成小写
# 元类继承自 type
class LowercaseMeta(type):
    """修改类的属性名称为小写的元类"""
    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k,v in attrs.items():
            if not k.startswith('__'):   # 排除 魔术方法 magic method
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v
        return type.__new__(mcs,name,bases,lower_attrs)

# 使用自定义的元类
class LowercaseClass(metaclass=LowercaseMeta):
    BAR = True

    def HELLO(self):
        print('hello')

print(dir(LowercaseClass))  # 会发现 BAR 和 HELLO 都变成小写了

LowercaseClass().hello()  # 用一个类的实例调用hello方法，此时已修改了类定义时的属性名（定义时为大写）

# LowercaseClass().HELLO()  # 调用会报错，因为函数名已经变成小写了