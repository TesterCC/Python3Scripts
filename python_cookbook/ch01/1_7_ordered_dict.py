#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/3 01:06'

"""
1-7 字典排序

问题：
你想创建一个字典，并且在迭代和序列化这个字典的时候能够控制元素的顺序。

解决方案：
为了控制一个字典中元素的顺序，可以使用collections模块中的OrderedDict类，在迭代的时候它会保持元素被插入时的顺序。
"""

from collections import OrderedDict

d = OrderedDict()

d['Bob'] = 1
d['Charles'] = 2
d['David'] = 3
d['Alice'] = 4
d['Alan'] = 5

for key in d:
    print(key, d[key])

ret_dict = {key: d[key] for key in d}   # unordered because dict
print("ret_dict: ", ret_dict)

print('--' * 50)
ret_list = [(key,d[key]) for key in d]   # ordered because list
print("ret_list: ", ret_list)
ret_list.sort()   # 按key排序
print("ret_list: ", ret_list)


# 控制以json编码后字段的顺序
import json

json_str = json.dumps(d)
print(json_str)   # ordered





