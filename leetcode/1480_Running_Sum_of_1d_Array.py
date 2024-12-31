# coding=utf-8
"""
DATE:   2021/3/12
AUTHOR: Yanxi Li
"""
from typing import List

"""
https://leetcode-cn.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/running-sum-of-1d-array

给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。


示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/running-sum-of-1d-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 这个解法很容易理解，运用了动态规划的思想
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        tmp = 0

        for i in nums:
            tmp = tmp + i
            ret.append(tmp)

        return ret

# Python3取巧的解法： itertools accumulate函数
# accumulate函数的功能是对传进来的iterable对象逐个进行某个操作（默认是累加）
class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return list(accumulate(nums))

