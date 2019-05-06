#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 14:48'

# 导入sklearn包导datasets模块
from sklearn import datasets

boston = datasets.load_boston()  # 加载自带的波士顿房价数据集

X = boston.data
y = boston.target

# 打印维数  506条记录，每条记录包含房屋的13条属性
print(X.shape)

# 打印数据集描述
print(boston.DESCR)
