#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-18 22:54'

"""
5372. 逐步求和得到正数的最小值 显示英文描述 (第 24 场双周赛第1题)

给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。
"""
from typing import *


# 100%AC但不够优雅

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sl = []

        flag = True

        for i in range(-32768,32768):
            sums = i

            for j in nums:
                sums += j

                if sums < 1:
                    flag = False
                    break
                else:
                    flag = True

            if flag and i > 0:
                sl.append(i)
            continue

        return sl[0]

if __name__ == '__main__':
    # nums = [-3, 2, -3, 4, 2]
    nums = [-22,-29,-21,0,-4,-26,10,-11,-14,-11]
    so = Solution()
    print(so.minStartValue(nums))