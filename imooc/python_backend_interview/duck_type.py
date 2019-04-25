#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-25 16:22'

"""
A Demo of Duck Type
鸭子类型更关注接口而非类型
"""


class Duck:
    def quack(self):
        print("gua gua gua")


class Person:
    def quack(self):
        print("I'm human, but I also can gua gua gua.")


def in_the_forest(duck):
    duck.quack()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
    print(type(donald))
    print(type(john))
    print(isinstance(donald,Duck))
    print(isinstance(john,Person))    # 还可以使用自省来判断类型，后面讲


game()
