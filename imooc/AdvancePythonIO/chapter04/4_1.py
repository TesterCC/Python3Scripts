#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 13:31'

"""
4-1 鸭子类型和多态
"""


class Cat(object):
    def say(self):
        print("I am a cat")


class Dog(object):
    def say(self):
        print("I am a dog")


class Duck(object):
    def say(self):
        print("I am a duck")


class Horse(object):
    def say(self):
        print("I am a horse")


# example 1
# animal = Cat
# animal().say()
#
# animal = Duck
# animal().say()

# example 2
animal_list = [Cat, Dog, Duck, Horse]
for animail in animal_list:
    animail().say()
