#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-11-28 09:58'

"""
P328 26-1 不符合单一职责原则的举例

动物都能跑，PM要求动物只有路生哺乳动物
"""

class Animal:
    def __init__(self, name:str):
        self.__name = name

    def running(self):
        print(self.__name + " is running...")


if __name__ == '__main__':
    Animal('Neko(Cat)').running()
    Animal('Iru(Dog)').running()
