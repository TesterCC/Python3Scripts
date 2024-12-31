#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-04 22:59'


import collections
import copy
s = "我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！/"
s_list = s.split('/')
# 为避免迭代时修改迭代对象本身，创建一个列表的深拷贝，也可用浅拷贝s_list_backup = s_list[:]
s_list_backup = copy.deepcopy(s_list)
# print(s_list_backup)
[s_list.remove(item) for item in s_list_backup if item in '，。！”“']
print(s_list)
print(collections.Counter(s_list))