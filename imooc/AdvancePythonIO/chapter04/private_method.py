#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/7 13:40'

"""
4-8 数据封装和私有属性
"""

from imooc.AdvancePythonIO.chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # return age
        return 2018 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1990, 12, 12))
    print(user._User__birthday)  # __attr的值其实通过这种方式也能获取到
    print(user.get_age())
