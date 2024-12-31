#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/17 05:53'


"""
属性property

1. 私有属性添加getter和setter方法   -- 12_private.py
2. 使用property升级getter和setter方法  -- 见本文件
3. 使用property取代getter和setter方法  -- 04_property2.py

@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，主要有2个作用

将方法转换为只读
重新实现一个属性的设置和读取方法,可做边界判定
"""


class Test(object):
    def __init__(self):
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self, newNum):
        self.__num = newNum

    num = property(getNum, setNum)    # 必须先get，后set，有参数的必须在后面


if __name__ == '__main__':
    t = Test()
    print(t.getNum())

    t.setNum(77)
    print(t.getNum())

    print("-" * 70)

    t.num = 200
    print(t.num)