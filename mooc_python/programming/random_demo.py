#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-14 01:24'

import random

# random库提供6个扩展随机数函数

# 1.生成[a,b]之间的随机整数
print(random.randint(10,100))
print(random.randint(50,55))

print("*"*90)
# 2.生成一个[m,n)之间以k为步长的随机整数
print(random.randrange(45,77,10))
print(random.randrange(45,77,10))

# 3.生成一个k比特长的随机整数
print(random.getrandbits(16))   # 16 bits
print(random.getrandbits(16))

# 4.生成一个[a,b]之间的随机小数    Python的浮点数取值范围是小数点后16位
print(random.uniform(10,20))
print(random.uniform(10,20))

# 5.从序列seq中随机选取一个元素
print(random.choice(["a","b","c","d","A","B","X","Y","Z"]))
print(random.choice([1,3,5,7,9,11]))

# 6.将序列seq中的元素随机排列，返回打乱后的序列
s = ["a","b","c","d","X","Y","Z"]
random.shuffle(s)
print(s)

print("*"*90)
# 7.从序列seq list中随机获取N个元素，作为一个片断返回
print(random.sample(s, 3))
print(random.sample(s, 5))

print("*"*90)
# 利用随机数种子产生"确定"的伪随机数
random.seed(10)   # 设定seed的目的，是复现随机事件，因为不设定seed的话，默认是用的当前系统时间，精确到微妙且随时在变化

print(random.random())   # 用了固定seed，所以输入的随机数都能复现
print(random.random())   # 0.生成一个[0,1]之间的随机小数
print(random.random())