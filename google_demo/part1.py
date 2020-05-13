#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/13 20:21'

"""
ref:
机器学习从零到一  第一节：机器学习简介
机器学习从零到一  第二集 - 机器学习中的基本计算机视觉概念 Fashion MNIST数据集
https://www.bilibili.com/video/BV1kZ4y1p7rb
"""

import keras
import numpy as np

# 定义单层神经网络，只有一个神经元units=1，input_shape输入执行为1
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# optimizer 优化函数  和 loss 损失函数  会使结果更趋近于 正确值。  关键：这2个函数会决定数据如何变化
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=700)


print(model.predict([10.0]))
