#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-11-28 10:34'

"""
P331 26-5 不符合开放封闭原则的举例

场景：动物园里有多种动物，游客希望观察每一种动物是怎样活动的。
"""


class TerrestrialAnimal:
    def __init__(self, name: str):
        self.__name = name

    def running(self):
        print(self.__name + " is running...")


class AquaticAnimal:
    def __init__(self, name: str):
        self.__name = name

    def swimming(self):
        print(self.__name + " is swimming...")


class Zoo:

    def __init__(self):
        self.__animals = [
            TerrestrialAnimal('Cat'),
            AquaticAnimal('Fish')
        ]

    def displayActivity(self):
        for animal in self.__animals:
            if isinstance(animal, TerrestrialAnimal):
                animal.running()
            else:
                animal.swimming()


if __name__ == '__main__':
    zoo = Zoo()
    zoo.displayActivity()
