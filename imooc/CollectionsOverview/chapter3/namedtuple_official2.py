#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/15 21:12'

"""
https://docs.python.org/3.6/library/collections.html#collections.defaultdict
https://yiyibooks.cn/xx/python_352/library/collections.html

namedtuple 在为 csv or sqlite3 模块返回的元组命名显得十分有用
"""

from collections import namedtuple

import csv

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):    # need employees.csv 类方法。从现有的列表或迭代器创建一个新的实例
    print(emp.name, emp.title)

import sqlite3

conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, department, paygrade FROM employees')

for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

# 除了从tuple继承而来的方法，namedtuple还支持另外三个方法和两个属性。为了避免和字段冲突，这些方法和属性都以下划线开头


