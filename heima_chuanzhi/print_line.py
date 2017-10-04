#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/4 17:24'

'''
4.8.1
写一个函数打印一条横线
打印自定义行数的横线
'''


def print_line():
    """打印单横线"""
    print("-" * 50)


def print_double_line():
    """打印双横线"""
    print("=" * 50)


def print_multi_line(line_nums=2):
    i = 0
    while i < line_nums:
        print_line()
        i += 1


def print_multi_double_line(line_nums=2):
    i = 0
    while i < line_nums:
        print_double_line()
        i += 1


if __name__ == '__main__':
    print_line()
    print_double_line()
    print(">>>>>>")
    print_multi_line(4)
    print_multi_double_line(5)
