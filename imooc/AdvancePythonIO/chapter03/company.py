#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/3 13:29'

"""
3-3 python魔法函数一览
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return "-".join(self.employee)


company = Company(["tom", "bob", "jane"])

print(company)
