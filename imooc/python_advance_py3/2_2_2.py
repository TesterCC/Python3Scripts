#!/usr/bin/env python
# coding:utf-8


from collections import namedtuple

# http://coding.imooc.com/lesson/62.html#mid=826
# 2-2 如何为元组中的每个元素命名, 提高程序可读性

# Method 2 -- 使用标准库中collections.namedtuple替代内置tuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('Jim', 16, 'male', 'jim8721@mail.com')
s2 = Student(name='Lily', age=26, sex='female', email='lily123@mail.com')
print(s)
print(s2)
print(s.age)
print(s2.sex)

print(isinstance(s, tuple))    # 判断s是否为tuple类型
print(isinstance(s2, tuple))    # 判断s2是否为tuple类型