#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/22 15:41'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.1 可接受任意数量参数的函数    P215
"""


# Scenario 1: 让一个函数能接受任意数量的位置参数，使用一个*参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# sample use
print(avg(1, 2))
print(avg(1, 2, 3, 4, 5))

print("Scenario 2---> make_element")
# Scenario 2: 接受任意数量的关键字参数，使用一个**开头的参数
import html


def make_element(name, value, **attrs):
    """
    :param name:
    :param value:
    :param attrs: 是一个包含所有被传入进来的关键字参数的字典
    :return:
    """
    keyvals = [' %s="%s" ' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element


# Example
# Creates '<item size="large" quantity="6">Testcase</item>'
ret = make_element('item', 'Testcase', size='large', quantity=6)
print(ret)

# Creates '<p>&lt;spam&gt;</p>'
ret = make_element('p', '<spam>')
print(ret)

print("Scenario 3---> any_args")


# P216  # Scenario 3: 函数能同时接受任意数量的位置参数和关键字参数，可以同时使用*和**
def any_args(*args, **kwargs):
    print(args)  # A tuple  存放所有位置参数
    print(kwargs)  # A dict   存放所有关键字参数


print(any_args("a", {'test': 'value1'}, size=6, age=21))


# *参数只能出现在函数定义中最后一个位置参数后面，但*参数后面仍然可以定义其他参数
# **参数只能出现在最后一个参数

def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass
