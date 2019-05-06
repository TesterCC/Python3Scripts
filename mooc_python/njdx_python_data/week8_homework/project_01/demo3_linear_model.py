#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 16:42'

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

clf = linear_model.LinearRegression()

X = np.array([2, 3, 5, 7, 6]).reshape(-1, 1)
y = np.array([6, 10, 14.5, 21, 18.5])

clf.fit(X, y)  # 训练模型
b, a = clf.coef_, clf.intercept_
print(b, a)

x = [[4]]

print(clf.predict(x))  # 预测

# 基于方程可以拟合的直线绘制出来

plt.plot(X, a+b*X, color='red')

plt.scatter(X, y, color='blue')

plt.show()


