#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/3 09:08'


"""
1.6 字典中映射多个值

一个字典就是一个键对应一个单值的映射。

问题：
怎样实现一个键对应多个值的字典（也叫multidict）?

解决方案：
将值放到另外的容器中，比如列表或集合
"""

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# 如果想保持元素的插入顺序，就应该使用列表
# 如果想去掉重复元素且不关心顺序问题，就使用集合set

print(d)
print(e)

# 可以用collections模块中的defaultdict来构造这样的字典
from collections import defaultdict

f1 = defaultdict(list)

f1['a'].append(1)
f1['a'].append(2)
f1['b'].append(4)

print(f1)


f2 = defaultdict(set)

f2['a'].add(1)
f2['a'].add(2)
f2['4'].add(4)

print(f2)

# 需要注意：defaultdict会自动为将要访问的键(就算目前字典中并不存在这样的键)创建实体。
# 如果你不需要这样的特性，你可以在一个普通的字典上使用setdefault()方法来代替
new_dict = {}   # A regular dictionary
new_dict.setdefault('a', []).append(1)
new_dict.setdefault('a', []).append(2)
new_dict.setdefault('b', []).append(4)
print(new_dict)


# 自己实现一个多值映射字典

# Method 1

def custom_multi_dict(pairs):

    d = {}

    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)


# Method 2
def custom_multi_dict_v2(pairs):

    d = defaultdict(list)

    for key, value in pairs:
        d[key].append(value)




