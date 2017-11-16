#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 21:07'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000
使用枚举类

为这样的枚举类型定义一个class类型,每个常量都是class的一个唯一实例
Python提供了Enum类来实现这个功能
"""

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)      # value属性则是自动赋给成员的int常量，默认从1开始计数

print(Month._member_map_)
print(Month.__members__)
print(Month._member_names_)
