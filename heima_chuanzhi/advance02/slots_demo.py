#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/30 23:43'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    16-__slots__的作用
"""


class Person(object):
    __slots__ = ("name", "age")


class SubPerson(Person):
    pass


if __name__ == '__main__':
    P = Person()
    P.name = "Alan"
    P.age = 20
    # P.score = 100
    print(P.name, P.age)

    print("-" * 70)
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    t = SubPerson()
    t.score = 99

    print(t.score)
