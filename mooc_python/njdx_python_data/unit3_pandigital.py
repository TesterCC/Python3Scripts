#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-01 17:54'

"""
题目内容：

如果一个n位数刚好包含了1至n中所有数字各一次则称它们是全数字（pandigital）的，例如四位数1324就是1至4全数字的。从键盘上输入一组整数，输出其中的全数字，若找不到则输出“not found”。

输入格式: 多个数字串，中间用一个逗号隔开

输出格式: 满足条件的数字串，分行输出


输入样例:

1243,322,321,1212,2354

输出样例：

1243

321
"""

def pandigital(nums):
    flag = False
    for num in nums:
        num = str(num)
        all_number_list = [str(i) for i in range(1, len(num) + 1)]
        all_number_in_num_list = [j for j in all_number_list if j in num]
        if len(all_number_list) == len(all_number_in_num_list):
            print(num)
            flag = True
    if flag == 0:
        print('not found')
        
if __name__ == "__main__":
    lst = pandigital(eval(input()))