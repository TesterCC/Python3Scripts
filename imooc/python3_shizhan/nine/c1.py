#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/30 23:58'

"""
第9章 高级部分：面向对象
9-1  5:54
"""

# 编写有意义的面向对象的代码
# 类＝面向对象
# 类、对象
# 实例化
# 类最基本的作用封装


class Student():
    name = ''
    age = 0

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student = Student()
student.print_file()