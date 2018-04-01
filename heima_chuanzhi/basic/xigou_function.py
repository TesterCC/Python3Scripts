#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/1 23:03'

"""
传智播客Python课件/2016基础班课件/第09天/01-课件/09day/section.6.html
析构

创建对象时，默认调用构造方法；
当删除一个对象时，同样也会默认调用一个方法，这个方法为析构方法
"""


class Animal:
    # 构造方法
    def __init__(self):
        print("__init__构造方法被调用")

    def __del__(self):
        print("__del__析构方法被调用")


if __name__ == '__main__':
    cat = Animal()
    print("实例化Animal")

    del cat

