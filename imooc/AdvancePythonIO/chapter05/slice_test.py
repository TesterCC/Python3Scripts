#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 22:09'

"""
5-4 实现可切片的对象
"""

aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]

print(aList[::])  # 返回包含原列表中所有元素的新列表
print(aList[::-1])  # 返回包含原列表中所有元素的逆序列表
print(aList[::2])  # 隔一个取一个，获取偶数位置的元素
print(aList[1::2])  # 隔一个取一个，获取奇数位置的元素
print(aList[3:6])  # 指定切片开始和结束的位置
print(aList[0:100])  # 切片结束位置大于列表长度时，从列表尾部截断
print(aList[100:])  # 切片开始位置大于列表长度时，返回空列表

aList[len(aList):] = [9]  # 在列表尾部增加元素
print(aList)
aList[:0] = [1, 2]  # 在列表头部插入元素
print(aList)

aList[:3] = [1, 2]  # 替换列表元素，等号两边的列表长度相等，注意理解
print(aList)

aList[3:] = [4, 5, 6]  # 替换列表元素，等号两边的列表长度也可以不相等
print(aList)

aList[::2] = [0] * 3  # 从0开始，隔一个修改一个
print(aList)

aList[::2] = ['a', 'b', 'c']  # 从0开始，隔一个修改一个
print(aList)

# aList[::2] = [1, 2]   # 左侧切片不连续，等号两边列表长度必须相等，不相等则报错
# print(aList)

aList[:3] = []  # 删除列表中的前3个元素 index 0，1，2
print(aList)

del aList[:3]  # 切片元素连续删除
print(aList)

del aList[::2]  # 切片元素不连续，隔一个删一个
