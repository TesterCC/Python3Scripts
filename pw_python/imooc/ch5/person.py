#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/4 17:03'

"""
5-1 面向对象基础及Python类常考问题
#### 什么是面向对象编程(OOP, Object Oriented Programming)？

- 把对象作为基本单元，把对象抽象成类（Class），包含成员和方法
- 数据封装、继承、多态
- Python中使用类来实现。
  - 过程式编程（使用函数）
  - OOP编程（使用类）

"""


class Person(object):    # 兼容python2， python3直接可以写成 class Person

    # 定义类的成员
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._sex = "secret"   # _ 表明属性不希望被外界访问私有属性， __len__(self) 这种是魔术方法

    # 定义类的方法
    def print_name(self):
        print('My name is {}'.format(self.name))