#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/8 13:28'

"""
4-9 python对象的自省机制

自省是通过一定的机制查询到对象的内部结构
"""

from imooc.AdvancePythonIO.chapter04.class_method import Date


class Person:
    """
    Class Person
    """
    name = "user"


class Student(Person):
    def __init__(self, scool_name):
        self.scool_name = scool_name


if __name__ == '__main__':
    user = Student("Python全栈研习社")
    print(user.__dict__)
    print(user.name)
    print(user.scool_name)

    user.__dict__['school_addr'] = "Beijing"
    print(user.school_addr)
    print(Person.__dict__)
    print(user.name)
    print(dir(user))

