#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-11 13:34'

"""
P29 状态模式
"""

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """
    State abstract class
    """

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        """
        behavior in different state
        :param water:
        :return:
        """
        pass

class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f"我性格高冷，当前体温{str(water.getTemperature())}摄氏度")

class LiquidState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f"我性格温和，当前体温{str(water.getTemperature())}摄氏度")

class GaseousState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print(f"我性格热烈，当前体温{str(water.getTemperature())}摄氏度")



class Wather:
    """
    water H2O
    """

    def __init__(self, state):
        self.__temperature = 25  # default temperature
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if (self.__state):
            print(f"由{self.__state.getName()}变为{state.getName()}")
        else:
            print(f"初始化为{state.getName()}")
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if (self.__temperature <= 0):
            self.changeState(SolidState("固态"))
        elif (self.__temperature <= 100):
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)

if __name__ == '__main__':
    water = Wather(LiquidState("液态"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()