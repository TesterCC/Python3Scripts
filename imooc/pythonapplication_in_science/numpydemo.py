#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 http://www.imooc.com/learn/727
Python中的包Numpy
'''


import numpy as np


height = [1.73,1.68,1.71,1.89,1.79]

weight = [65.4,59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)

np_weight = np.array(weight)

bmi = np_weight/np_height**2

print(bmi)

print(type(bmi))

print("------------------------")

print(bmi[0])

print(bmi[bmi>23])


