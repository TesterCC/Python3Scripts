#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/13 23:46'

"""
《Python+Cookbook》第三版中文v3.0.0
1.2 解压可迭代对象赋值给多个变量

你在学习一门课程,在学期 末的时候,你想统计下家庭作业的平均成绩,但是排除掉第一个和最后一个分数。如果 只有四个分数,你可能就直接去简单的手动赋值,但如果有 24 
"""

print("-" * 5 + "example 1" + "-" * 5)


def avg(list_):
    avg_ = sum(list_) / len(list_)
    return avg_


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


result = drop_first_last([1, 2, 2, 2, 2, 10])
print(result)

print(avg([1, 2, 2, 2, 2, 10]))

print("-" * 5 + "example 2" + "-" * 5)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(*phone_numbers)

