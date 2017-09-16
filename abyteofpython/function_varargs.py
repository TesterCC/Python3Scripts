#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/15 22:57'

# A Byte of Python -- P63-64 -- Python3


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))