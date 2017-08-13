#!/usr/bin/env python
# coding=utf-8

# A Byte of Python -- P33-34 -- Python3

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# result = name + ' is ' + str(age) + ' years old'   # don't recommand
# print(result)

print('------------------------------------------------')
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
print('------------------------------------------------')

# 对于浮点数'0.333'	保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
print('{0:.4f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用(^)定义	'___hello___'字符串长度为11
print('{0:_^11}'.format('Hello'))

# 基于关键词输出'Swaroop wrote A Byte of Python'
print('{name} worte {book}.'.format(name='Swaroop', book='A Byte of Python'))
print('------------------------------------------------')

#  end指定其应以空白结尾
print('a', end='')
print('b', end='^-^')
print('\n------------------------------------------------')   # because former row has not input \n
print('a', end='    ')
print('b', end='    ')
print('c', end='')
