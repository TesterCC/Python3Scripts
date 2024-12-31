#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 http://www.imooc.com/video/12984
 2维numpy数组
'''

import numpy as np

np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2, 63.6, 88.4, 68.7]])    #([x,y])

print(np_2d)
print(np_2d.shape)   #显示行列
print("-----------------------------")

print(np_2d[0])
print(np_2d[0][2])   #先行后列
print(np_2d[0, 2])   #先行后列
print("-----------------------------")

print(np_2d[:, 1:3])   #先行后列
print("-----------------------------")
print(np_2d[1, :])     #先行后列
print("-----------------------------")


test1 = np.array([['a','b','c'],['d','e','f']])
test2 = np.array([['1','2','3'],['4','5','6']])

print(test1)
print(test2)
