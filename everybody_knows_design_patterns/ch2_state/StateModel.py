#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-11 23:37'

"""
P32 什么是状态模式:
允许一个对象在其内部发生改变时改变其行为，使该对象看上去像改变了类型一样

注意开闭原则
注意表示状态的类应该只会有一个实例

抽象出状态模式的框架模型

状态模式框架模型
"""

from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """
    状态模式的上下文环境类  负责具体状态的切换
    """

    def __init__(self):
        self.__states = []
        self.__curState = None

        # 状态发生变化依赖的属性，当这一变量由多个变量共同决定时可以将其单独定义成一个类
        self.__stateInfo = 0

    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self, state):
        if state is None:
            return False

        if self.__curState is None:
            print("初始化为：", state.getName())
        else:
            print("由",self.__curState.getName(),"变为",state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """Base Class of state 负责状态的定义和接口的统一"""
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        """
        状态属性stateInfo是否在当前状态范围内
        :param stateInfo:
        :return:
        """
        return False

    @abstractmethod
    def behavior(self, context):
        pass




