#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-14 23:17'

"""
2.3 元祖不仅仅是不可变的列表
元组的作用:
1.不可变列表
2.没有字段名的记录

2.3.2 元组拆包可以运用到任何对象上，唯一要求是被迭代对象中的元素数量必须要跟接受这些元素的元组的空档数一致
"""

# 把元组用作记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

# 优雅写法，不使用中间变量交换两个变量的值   b,a = a,b

# 用*运算符把一个可迭代对象拆开作为函数的参数
t = (20, 8)
quotient, remainder = divmod(*t)

print(quotient, remainder)

# 元组拆包用法：让一个函数可以用元组的形式返回多个值
import os

# 使用 _ 占位，但在国际化软件中不是一个好占位符，因为是gettext.gettext函数的常用别名 https://doc.python.org/3/library/gettext.html
_, filename = os.path.split("/Users/TesterCC/Desktop/div_demo/div_demo.html")
print(filename)

# 用*args来获取不确定数量的参数是一种经典写法。
# Python 3中被扩展到平行赋值
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

# 在平行赋值中，*变量名  即是说*前缀只能用在一个变量名前面，这种形式只能有一个，但可以出现在赋值表达式的任意位置
a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)
