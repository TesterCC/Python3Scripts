#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=826
# 2-2 如何为元组中的每个元素命名, 提高程序可读性


# Method 1 -- 定义类似与其他语言的枚举类型，也就是定义一系列数值常量
# 通过常见定义元组中的字段
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3

# recommand method
NAME, AGE, SEX, EMAIL = range(4)
print(NAME)
print(NAME, AGE, SEX, EMAIL)


student = ('Jim', 16, 'male', 'jim8721@mail.com')

# name
# print(student[0])
print(student[NAME])

# age
if student[AGE] >= 18:
    print(student[AGE])
else:
    print("Student less than 18.")

# sex
if student[SEX] == 'male':
    print(student[SEX])
else:
    print("female")