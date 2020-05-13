#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/13 21:34'

"""
ref:
机器学习从零到一  第二集 - 机器学习中的基本计算机视觉概念 Fashion MNIST数据集
https://www.bilibili.com/video/BV1kZ4y1p7rb
"""

import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
# 训练数据集 About 6000 pics, 另外1万张pics是测试数据
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),   # 28x28, 图像的像素
    # 激励函数
    keras.layers.Dense(128, activation=tf.nn.relu),  # 第一层激励函数，线性整流函数，返回大于0的数值。 128  f0到f127，共128个函数且每个函数都有参数
    keras.layers.Dense(10, activation=tf.nn.softmax)  # 第二层激励函数，选出这个集合中最大的数。  10，数据集中服装类别的种类
])

# 神经网络初始都使用随机数值, 用损失函数测量结果的好坏，然后用优化器生成新的参数输入到这个函数中，看看能不能得到更好的结果。
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy')

model.fit(train_images,train_labels,epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

predictions = model.predict(my_images)   # my_images没有给出