#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 14:48'

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import datasets


boston = datasets.load_boston()  # 加载自带的波士顿房价数据集

# 房屋13个属性数据
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=['MEDV'])

# statsmodels中的线性回归模型没有截距项，下行给训练集加上一列数值为1的特征
X_add1 = sm.add_constant(X)
model = sm.OLS(y, X_add1).fit()    # sm.OLS()为普通最小二乘回归模型，fit()用于拟合
# print(model.summary())

# 移除两个属性/特征
X.drop('AGE', axis=1, inplace=True)
X.drop('INDUS', axis=1, inplace=True)

# 重新训练
X_add1 = sm.add_constant(X)
model = sm.OLS(y, X_add1).fit()    # sm.OLS()为普通最小二乘回归模型，fit()用于拟合
print(model.summary())

# coef列即为计算出的回归系数，可以输入
print("print coef")
print(model.params)

# 假设数据计算
#  第一个数1为同样添加的常数项
print("-"*90)
X_test= np.array([[1,0.006,18.0,0.0,0.52,6.6,4.87,1.0,290.0,15.2,396.2,5]])

# 直接利用模型预测结果
print(model.predict(X_test))