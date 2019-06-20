#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-20 13:16'

"""
监听模式的抽象模型  P19-20
根据1_1，抽象出监听模式的框架模型

Observable: 被观察者的抽象类
Observer: 观察者的抽象类

"""

from abc import ABCMeta, abstractmethod  # 引入ABCMeta, abstractmethod来定义抽象类和抽象方法

# 抽象出监听模式的框架模型
class Observer(metaclass=ABCMeta):
    """base class of Observer 观察者的抽象类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """base class of Observable 被观察者的抽象类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


"""
P21 基于框架实现热水器 Version 2.0
"""


class WaterHeater(Observable):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("Current temperature is : " + str(self.__temperature) + " degree centigrade")
        self.notifyObservers()
        pass
