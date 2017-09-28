#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/27 23:45'

'''
2-4 如何根据字典中值的大小, 对字典中的项排序
http://coding.imooc.com/lesson/62.html#mid=824
成绩以字典形式存储，如：{'Tom': 99, 'Lily': 88, 'Lucy': 70}
根据成绩高低，计算成绩排名

解决方案：
使用内置函数sorted
2.传递sorted参数的key参数
'''

from random import randint


# create score dict
d = {x: randint(60, 100) for x in "xyzabc"}
print(d) 

print("------------------------")
print(sorted(d))
print(d.items())    # key, value  python3 dict items

print('------------sorted-----------')
print(sorted(d.items(), key=lambda x: x[1]))   # x[0]是xyzabc的位置，x[1]是分数