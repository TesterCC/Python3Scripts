#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-11-28 11:39'

"""
P332 26-6 遵循开放封闭原则的设计
"""

# 引入以便定义抽象类
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    def __init__(self, name:str):
        self._name = name

    @abstractmethod
    def moving(self):
        pass


class TerrestrialAnimal(Animal):
    """陆生生物"""
    def __init__(self, name:str):
        super().__init__(name)

    def moving(self):
        print(self._name + " run in land...")


class AquaticAnimal(Animal):
    """水生生物"""
    def __init__(self, name:str):
        super().__init__(name)

    def moving(self):
        print(self._name + " swim in water...")


class BirdAnimal(Animal):
    """
    鸟类动物
    """
    def __init__(self, name:str):
        super().__init__(name)

    def moving(self):
        print(self._name + " fly in sky...")


class Zoo:
    """
    动物园
    """
    def __init__(self):
        self.__animals = []

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("Observe all kinds of animal's lifestyle: ")
        for animal in self.__animals:
            animal.moving()


if __name__ == '__main__':
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("Dog"))
    zoo.addAnimal(AquaticAnimal("Fish"))
    zoo.addAnimal(BirdAnimal("Bird"))

    zoo.displayActivity()

