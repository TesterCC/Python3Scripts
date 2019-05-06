#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 15:58'

import matplotlib.pyplot as plt
import numpy as np

# 假设有一组特征x为2、3、5、7、6，标签y为6、10、14.5、21、18.5，将两者之间的关系用散点图进行展现

X = np.array([2,3,5,7,6]).reshape(-1,1)  # -1表示基于另一个确定的值

y = np.array([6,10,14.5,21,18.5])
plt.scatter(X, y, color='blue')

plt.show()   # 显示绘图