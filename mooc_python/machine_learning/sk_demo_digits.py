#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-27 17:43'

"""
sklearn库的基本功能:
用于完成：分类任务、回归任务、聚类任务、降维任务、模型选择以及数据的预处理
"""

# 手写数字数据集
from sklearn.datasets import load_digits

from matplotlib import pyplot as plt

digits = load_digits()

print(digits.data.shape)

print(digits.target.shape)

plt.matshow(digits.images[1])
plt.show()
