#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/3 13:36'

"""
3-3 python魔法函数一览
"""


class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


my_num = Nums(-1)
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x=self.x, y=self.y)


first_vec = MyVector(1, 2)
second_vec = MyVector(2, 3)
print(first_vec + second_vec)
