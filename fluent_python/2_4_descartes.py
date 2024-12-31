# coding=utf-8
'''
DATE: 2020/09/03
AUTHOR: Yanxi Li

用列表推导可以生成两个或以上的可迭代类型的笛卡儿积。

笛卡儿积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元组，因此笛卡儿积列表的长度等于输入变量的长度的乘积
'''

# 3 种不同尺寸的 T 恤衫，每个尺寸 2 种颜色

colors = ['black', 'white']

sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

