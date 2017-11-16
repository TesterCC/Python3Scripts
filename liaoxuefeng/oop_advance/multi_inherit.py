#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 11:37'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318680104044a55f4a9dbf8452caf71e8dc68b75a18000
多重继承
"""


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


# 肉食动物
class CarnivorousMixIn(object):
    def eat(self):
        print('Eat meat ...')


# 植食动物
class HerbivoresMixIn(object):
    def eat(self):
        print('Eat herb ...')


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# 各种动物:
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Parrot(Bird, FlyableMixIn):
    pass


class Ostrich(Bird, RunnableMixIn):
    pass

# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# Java只能单继承，通过接口实现多功能
# 只允许单一继承的语言（如Java）不能使用MixIn的设计





