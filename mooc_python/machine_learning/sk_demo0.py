#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-27 11:28'

from sklearn.datasets import load_boston, load_iris

# 波士顿房价数据集
boston = load_boston()

print(boston.data.shape)
data, target = load_boston(return_X_y=True)
print(data.shape)
print(target.shape)


# 鸢尾花数据集
iris = load_iris()
print(iris.data.shape)

print()


