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
        new_str = ""
        for i in str:
            if "A" <= i <="Z":
                new_str += chr(ord(i)+32)
            else:
                new_str += i
        return new_str

if __name__ == '__main__':
    targets = ["Hello", "here", "LOVELY", "tESt"]   # test case
    so = Solution()
    for target in targets:
        print(so.toLowerCase(target))
