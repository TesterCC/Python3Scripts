#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/31 14:52'

"""
Python网络爬虫--从入门到实践   P17-18 2.2.5 面向对象编程
"""


class Person(object):

    def __init__(self, name, age):    # __init__()为类的构造方法
        self.name = name
        self.age = age

    def detail(self):   # 通过self调用被封装的内容
        print(self.name)
        print(self.age)

if __name__ == '__main__':

    obj1 = Person('Santos', 28)
    obj1.detail()  # Python将obj1传给self参数，即：obj1.detail(obj1)，此时内部self＝obj1

