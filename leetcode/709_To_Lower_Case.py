#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-22 00:32'

"""
https://leetcode-cn.com/problems/to-lower-case/

PS:这道题虽然python有极简做法，但是实际考的知识点参考这个。
极简：
return str.islower()

ASCII不经过比较转换字母大小写
https://blog.csdn.net/dd864140130/article/details/41578501
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        new_ch_list = []
        for ch in str:
            if  65 <= ord(ch) < 97:
                new_ch_list.append(chr(ord(ch)+32))
            else:
                new_ch_list.append(ch)

        return "".join(new_ch_list)


if __name__ == '__main__':
    targets = ["Hello", "here", "LOVELY", "tESt"]
    so = Solution()
    for target in targets:
        print(so.toLowerCase(target))
