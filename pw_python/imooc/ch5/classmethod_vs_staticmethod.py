#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/9 01:19'

"""

### classmethod和staticmethod的区别

- 都可以通过Class.method()的方式使用
- classmethod的第一个参数是cls，可以引用类变量
- staticmethod使用起来和普通函数一样，只不过放在类里去组织
  - classmethod是为了使用类变量
  - staticmethod是代码组织的需要，完全可以放到类之外
"""

class Person:

    Country = 'China'  # class variable

    def __init__(self,name):
        self.name = name

    @classmethod
    def print_country(cls):
        print(cls.Country)

    @staticmethod
    def join_name(first_name, last_name):
        return last_name + first_name    # last_name 姓，first_name 名