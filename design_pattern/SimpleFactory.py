#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/13 21:48'

"""
大话设计模式Python实现-简单工厂模式
简单工厂模式(Simple Factory Pattern):
是通过专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类.

https://www.cnblogs.com/onepiece-andy/p/python-simple-factory-pattern.html
"""


class Operation(object):
    '''
    四则运算的父类,接收用户输入的数值
    '''

    def __init__(self, number1=0, number2=0):
        self.num1 = number1
        self.num2 = number2

    def GetResult(self):
        pass

    pass


# 加法运算类
class OperationAdd(Operation):
    def GetResult(self):
        return self.num1 + self.num2


# 减法运算类
class OperationSub(Operation):
    def GetResult(self):
        return self.num1 - self.num2


# 乘法运算类
class OperationMul(Operation):
    def GetResult(self):
        return self.num1 * self.num2


# 除法运算类
class OperationDiv(Operation):
    def GetResult(self):
        if self.num2 == 0:
            return '除数不能为0'
        return 1.0 * self.num1 / self.num2


# 其他操作符
class OperationUndef(Operation):
    def GetResult(self):
        return '操作符错误'


# 简单工厂类
class OperationFactory(object):
    def choose_oper(self, ch):
        if ch == '+':
            return OperationAdd()
        elif ch == '-':
            return OperationSub()
        elif ch == '*':
            return OperationMul()
        elif ch == '/':
            return OperationDiv()
        else:
            return OperationUndef()


if __name__ == '__main__':
    flag = ''
    while not flag == 'q':
        print("请按提示输入: ")
        num1 = int(input('Please input first number value: '))
        ch = str(input("Please input a operator:"))
        num2 = int(input('Please input second number value: '))

        OF = OperationFactory()
        oper_obj = OF.choose_oper(ch)
        oper_obj.num1 = num1
        oper_obj.num2 = num2

        print('运算结果为: {}'.format(oper_obj.GetResult()))

        flag = str(input("是否开始计算，继续请按Enter，退出请输入'q'并回车:"))
