#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/23 13:05'

"""
3. 无重复字符的最长子串

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
https://leetcode.com/problems/longest-substring-without-repeating-characters

同：
剑指Offer 48 寻找最长不含有重复字符的子串
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

官方题解：
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/

推荐 滑动窗口 的解法

"""

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1 , 0
        for i in range(n):
            pass


