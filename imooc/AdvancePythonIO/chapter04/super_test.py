#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/8 23:03'

"""
4-10 super真的是调用父类吗？
"""


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        # super(B, self).__init__()   # Python2 继承父类的写法
        super().__init__()  # Python3 继承父类的写法


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):  # 多重继承，优先级从左到右
    def __init__(self):
        print("D")
        super(D, self).__init__()


from threading import Thread


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        # self.name = name
        super().__init__(name=name)  # 优化写法，不是自定义实例变量


# 既然我们重写B的构造函数，为什么还要去调用super？
# super到底执行顺序是什么样的？


if __name__ == "__main__":
    b = B()

    print(D.__mro__)  # D B C A obj
    d = D()
    print(d, type(d))
