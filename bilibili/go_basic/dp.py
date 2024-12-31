# -*- coding:utf-8 -*-
# https://www.bilibili.com/video/BV11Q4y157um
# 2个长度为1000000的数组求求内积，向量内积计算, python version, go version in learn go project

import time
import numpy as np

LEN = 1000000
arr = []
brr = []

for i in range(LEN):
    value = i % 10
    arr.append(value)
    brr.append(value)

array1 = np.array(arr)
array2 = np.array(brr)

begin = time.time()
prod = 0.0
for i in range(LEN):
    prod += arr[i] * brr[i]
end = time.time()

print("测试2个长度为1000000的数组求内积，向量内积计算）: %.2e\t\t用时%f秒\n" % (prod, end - begin))
