#!/usr/bin/env python
# coding=utf-8

'''
53 给定一个字符串，逐个翻转字符串中的每个单词。
单词的构成：无空格字母构成一个单词
输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
http://www.lintcode.com/zh-cn/problem/reverse-words-in-a-string/
'''

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):

        # write your code here
        # bad smell
        try:
            if 'str' in type(s):
                ss = s.strip(s)
                print(ss[::-1])
        except TypeError:
            return "Type is not str."

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Hello, world"))
    # print(type("test aa"))