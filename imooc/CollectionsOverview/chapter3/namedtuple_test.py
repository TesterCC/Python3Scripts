# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/15 16:28'

from collections import namedtuple

"""
https://docs.python.org/3.6/library/collections.html
namedtuple()这是个工厂方法,生成有命名字段的tuple子类(译注: tuple中的元素可以用名字的方式来访问)
namedtuple是继承自tuple的子类。namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性。
"""

User = namedtuple("User", ["name", "age", "height", "edu"])
# user = User(name="MFC", age=25, height=160)
user_tuple = ("MFC", 25, 160)
user = User(*user_tuple, "master")
print(user.name, user.age, user.height, user.edu)

print("-" * 50)

user_dict = {
    "name": "Tom",
    "age": 30,
    "height": 175
}

user = User(**user_dict, edu="master")
print(user.name, user.age, user.height, user.edu)


# 函数参数
def ask(*args, **kwargs):  # tuple, dict
    pass


# ask("Jerry", 33)    # return tuple
# ask(name="Jason", age=35)     # return dict


user_tuple2 = ("MFC2", 29, 160, "tuple-master")
user_list = ["MFC", 30, 160, "list-master"]
user_dict2 = {
    "name": "Tom",
    "age": 30,
    "height": 175,
    "edu": "doctor"
}

print("讲解_make方法：")
user2 = User._make(user_tuple2)  # 传入可迭代对象
user3 = User._make(user_list)
# user4 = User._make(user_dict2)   # return key

print(user2.name, user2.age, user2.height, user2.edu)
print(user3.name, user3.age, user3.height, user3.edu)

print("-" * 50)
print("讲解_asdict方法：")
user = User(*user_tuple, edu="master")
user_info_dict = user._asdict()
print(user.name, user.age, user.height, user.edu)
print(user_info_dict)  # return OrderedDict 根据参数名排序

# namedtuple也有拆包功能
print("-" * 50)
print("namedtuple拆包：")
name, age, *other = user
print(name, age, *other)
