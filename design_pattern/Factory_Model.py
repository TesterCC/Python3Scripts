#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/13 21:35'

"""
工厂模式
举例，改功能并不复杂，实际写一个类即可解决
"""


# 运算类基类
class Operation(object):
    def __init__(self):
        self.numberA = None
        self.numberB = None

    def get_result(self):
        result = 0
        return result


# 具体运算类(加法)
class OperationAdd(Operation):
    def __init__(self):
        super(OperationAdd, self).__init__()

    def get_result(self):
        return self.numberA + self.numberB


# 工厂类
class OperationFactory:
    def create_factory(self):
        oper = OperationAdd()
        return oper


if __name__ == '__main__':
    factory = OperationFactory()
    oper = factory.create_factory()
    oper.numberA = 2
    oper.numberB = 3

    print(oper.get_result())
