#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-19 17:38'

"""
lesson 1 - 监听模式

监听者：洗澡模式、饮用模式
被监听对象：热水器

监听模式：在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被同志并自动更新。

设计模式之监听模式（观察者模式与监听模式区别）
ref:
https://www.cnblogs.com/jackson-zhangjiang/p/7784694.html
"""

from abc import ABCMeta, abstractmethod
# 引入ABCMeta, abstractmethod来定义抽象类和抽象方法

class WaterHeater:
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("Current temperature is : " + str(self.__temperature) + " degree centigrade")
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """洗澡模式和饮用模式的父类, 抽象类"""

    # 抽象类中只定义要实现的方法，不需要定义方法中的逻辑
    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """洗澡模式"""
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(Observer):
    """饮用模式"""
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

if __name__ == '__main__':
    testWaterHeater()