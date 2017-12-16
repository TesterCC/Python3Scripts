#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/17 06:46'

"""
3. 使用property取代getter和setter方法

@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，主要有2个作用

将方法转换为只读
重新实现一个属性的设置和读取方法,可做边界判定
"""


class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        self.__num = newNum


if __name__ == '__main__':
    t = Test()

    t.num = 300     # 相当于调用了t.setNum(300)
    print(t.num)    # 相当于调用了t.getNum()
