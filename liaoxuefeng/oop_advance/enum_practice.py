#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 21:07'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000
使用枚举类

为这样的枚举类型定义一个class类型,每个常量都是class的一个唯一实例
Python提供了Enum类来实现这个功能

如果需要更精确地控制枚举类型，可以从Enum派生出自定义类

Q:把Student的gender属性改造为枚举类型，可以避免使用字符串

官方文档：
https://docs.python.org/3/library/enum.html

推荐阅读：
http://www.cnblogs.com/ucos/p/5896861.html

Python版本低于3.4时默认不带enum模块
"""

from enum import Enum, unique


# 把Student的gender属性改造为枚举类型，可以避免使用字符串

@unique
class Gender(Enum):
    Male = 0
    Female = 1
    Privacy = 2


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

print(Gender(1))
print(Gender.Male)
print(Gender['Privacy'])

print(Gender.Male is not Gender.Female)

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


