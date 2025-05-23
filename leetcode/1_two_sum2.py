#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/29 18:50'

'''
https://leetcode.com/problems/two-sum/description/
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

一个数组里面找两个数加和为指定数。注意要求返回的是数字所在的index。另外要注意每个数只能用一次。

So:这道题的解题思路很简单，利用python中的字典记录记录下每个元素出现的位置，也就是其他语言中的哈希表。
'''

from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,x in enumerate(nums):
            if target - x in hashtable:
                return [hashtable[target-x], i]  # 返回的是对应数字的索引
            hashtable[x]=i
            # hashtable[nums[i]]=i # 也可以
        return []



if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 25
    nums = [3, 2, 4]
    target = 6
    so = Solution()
    print(so.twoSum(nums, target))
