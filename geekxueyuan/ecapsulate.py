#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/18 16:29'

"""
3.多态和封装
"""


class ProtectMe(object):
    def __init__(self):
        self.me = "lily"
        self.__name = 'testercc'

    def __python(self):
        print("I love Python")

    def code(self):
        print("Which language do you like?")
        self.__python()

    @property         # 把name变为属性
    def name(self):
        return self.__name


if __name__ == '__main__':
    p = ProtectMe()
    print(p.me)
    # print(p.__name)

    p.code()
    # p.__python()

    print(p.name)
