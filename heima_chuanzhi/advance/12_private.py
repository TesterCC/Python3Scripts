#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/17 05:19'


class Test(object):
    def __init__(self):
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self, newNum):
        self.__num = newNum



if __name__ == '__main__':
    t = Test()
    print(t.getNum())

    t.setNum(77)
    print(t.getNum())