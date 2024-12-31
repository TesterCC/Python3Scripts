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
"""

from enum import Enum, unique


@unique           # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0    # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问这些枚举类型可以有若干种方法
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))


print('-----All Weekday-----')
# Method X
for name, member in Weekday.__members__.items():
    print(name, '=>', member)




