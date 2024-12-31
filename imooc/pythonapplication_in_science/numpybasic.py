#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 http://www.imooc.com/video/12985
 Numpy的基本统计学
'''


import numpy as np

# 生成大量数据
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height,weight))

# np_city = np.array([[1.64, 71.78],
#                     [1.37, 63.35],
#                     [1.60, 55.09],
#                     [2.04, 74.85],
#                     [2.04, 68.72],
#                     [2.01, 73.57]])

print(np_city)
print("------------------------------")
print(np_city[:,0])
print(np.mean(np_city[:,0]))    #抽出身高求平均    #先行后列
print("------------------------------")
print(np.median(np_city[:,0]))    #求中位数
print("------------------------------")
print(np.corrcoef(np_city[:,0], np_city[:,1]))
print("------------------------------")
print(np.std(np_city[:,0]))     #标准差