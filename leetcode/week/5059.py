#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-24 22:54'

"""
leetcode 5059. 单行键盘
week7
"""

class Solution:

    """
    bad answer
    """
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_list = list(keyboard)
        index_list = [i for i in range(26)]
        key_dict = dict(zip(key_list, index_list))

        ans = 0

        for i in range(len(word) - 1):
            tmp = abs(key_dict.get(word[i]) - key_dict.get(word[i + 1]))

            ans += tmp

        ans += key_dict.get(word[0])

        return ans



class Solution2:
    pass

if __name__ == '__main__':
    # keyboard = "abcdefghijklmnopqrstuvwxyz"
    # word = "cba"
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    so = Solution()
    ret = so.calculateTime(keyboard, word)
    print(ret)
