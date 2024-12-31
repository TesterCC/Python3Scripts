#!/usr/bin/env python
#coding=utf-8

'''
 Python在数据科学中的应用  imooc
 直方图
 http://www.imooc.com/video/12987
'''


import matplotlib.pyplot as plt

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]

plt.hist(values, bins=3)
plt.show()
