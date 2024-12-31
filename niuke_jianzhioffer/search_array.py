#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/29 15:39'

'''
题目描述:
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

数组	二维数组中的查找
'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = False
        for index in range(len(array)):
            if target in array[index]:
                flag = True
        return flag


if __name__ == '__main__':
    arr = [[0, 1, 0], [0, 1, 0], [7, 1, 0]]
    so = Solution()
    result = so.Find(7, arr)
    print(result)    # return True 表示含有