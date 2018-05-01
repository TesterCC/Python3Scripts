#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/1 15:50'

"""
3-1 什么是魔法函数
"""

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):  # 定义这个可以迭代
        return self.employee[item]


company = Company(["tom", "bob", "jane"])


# 没有实现__getitem__()时
# employee = company.employee
# for em in employee:
#     print(em)

# 实现__getitem__()后的用法
for em in company:    # for 优先取迭代器（实现__iter__()才有），Python优化，如果没有迭代器，就去一次次调__getitem__()
    print(em)
