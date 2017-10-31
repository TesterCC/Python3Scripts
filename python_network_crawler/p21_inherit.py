#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/31 15:03'

"""
Python网络爬虫--从入门到实践   P21 继承
"""


class Animal(object):
    def eat(self):
        print("%s 吃" % self.name)

    def drink(self):
        print("%s 喝" % self.name)

    def shit(self):
        print("%s 拉" % self.name)

    def pee(self):
        print("%s 撒" % self.name)


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print("喵喵叫")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print("汪汪叫")


if __name__ == '__main__':
    c1 = Cat('Lily家的小猫')
    c1.eat()
    c1.cry()

    d1 = Dog('Tom家的小狗')
    d1.drink()
    d1.cry()
