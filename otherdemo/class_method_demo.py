#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/22 14:29'

"""
### @staticmethod和@classmethod的用法

一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。

- @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
- @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
"""

class Demo:
    bar = 1
    def foo(self):
        print('foo')
        print(self.bar)
        print('>>foo end')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(Demo.bar)
        print('>>static_foo end')

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(Demo.bar)
        cls().foo()    # 调用了foo
        print('>>class_foo end')

if __name__ == '__main__':
    Demo.static_foo()
    Demo.class_foo()

    d = Demo()
    d.foo()