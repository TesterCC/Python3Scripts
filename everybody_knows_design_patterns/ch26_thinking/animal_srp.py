#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-11-28 09:58'

"""
单一职责原则 SRP, Single Responsibility Principle

核心思想：一个类应该有且仅有一个原因引起它的变更。

优点：
1) 功能单一，职责清晰。
2) 增强可读性，方便维护。

缺点:
1) 拆分得太细，类得数量会急剧增加。
2) 职责得度量没有统一得标准，需要根据项目实现情况而定。

P330 26-4

动物都能跑，需求变更，PM要求动物不只有路生哺乳动物，还要有水生动物，水生动物在水里游。
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


if __name__ == '__main__':
    TerrestrialAnimal('Neko(Cat)').running()
    AquaticAnimal('Uo(Fish)').swimming()
