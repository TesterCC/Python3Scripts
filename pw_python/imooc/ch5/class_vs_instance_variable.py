#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/9 01:01'

"""
### 类变量和实例变量的区别

- 类变量由所有实例共享
- 实例变量由实例单独享有，不同实例之间不影响
- 当我们需要在一个类的不同实例之间共享变量的时候使用类变量
"""

class Person:
    Country = 'China'  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量（属性）

    def print_name(self):
        print(self.name)


if __name__ == '__main__':
    laowang = Person('laowang')
    laoli = Person('laoli')
    laowang.print_name()
    laoli.print_name()
    print(laowang.Country)
    print(laoli.Country)
