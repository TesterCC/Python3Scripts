#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 23:00'


name_tuple = ("MFC1", "MFC2")

# tuple 拆包的用法
user_tuple = ("MFC", 25, 160, "beijing")

name, age, height, city = user_tuple   # 拆包到3个变量分别映射
print(name, age, height, city)

print("-"*50)

name, *other = user_tuple
print(name, other)

print("-"*50)

# tuple不可变不是绝对的
test_tuple = ("MFC", [25, 160])    # not recommend
test_tuple[1].append(22)    # 修改时[25, 160]id未变
print(test_tuple)

# dict key
user_info_dict = {}
user_info_dict[user_tuple] = "MFC"
print(user_info_dict)
