#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/18 16:36'


"""
geekxueyuan 零基础学Python
3.多态和封装 练习题
建立一个类，名字是Person，有关于人的基本信息
再建立一个程序员类，继承Person， 增加有关程序员的个性化信息
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_sleeptime(self):
        return 11


class Programmer(Person):
    def __init__(self, name, lang, age):
        super(Programmer, self).__init__(name, age)     # Attention
        self.lang = lang

    def get_sleeptime(self):
        return 1


class Tester(Person):
    def __init__(self, name, worktype, age):
        super(Tester, self).__init__(name, age)
        self.worktype = worktype

    def get_sleeptime(self):
        return 3

if __name__ == '__main__':
    p = Programmer("Lily", "Python", 22)
    print(p.lang)
    print(p.get_sleeptime())

    t = Tester("Mary", "Automated", 28)
    print(t.worktype)
    print(t.get_sleeptime())
    print(t.age)
