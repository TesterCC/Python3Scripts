#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 13:31'

"""
4-1 鸭子类型和多态
"""

# example 3
a = ["tester1", "tester2"]
b = ["tester2", "tester"]
name_tuple = ["tester3", "tester4"]
name_set = set()
name_set.add("tester5")
name_set.add("tester6")
a.extend(b)
print(a)
a.extend(name_set)
print(a)


# example 4
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):  # 定义这个可以迭代,支持for和切片
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
a = ["tester1", "tester2"]
a.extend(company)
print(a)