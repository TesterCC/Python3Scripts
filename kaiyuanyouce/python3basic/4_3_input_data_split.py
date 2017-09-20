#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/19 17:42'


'''
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484014&idx=1&sn=9d76477385260f66078b35e9eb2dbf99&scene=19#wechat_redirect
'''

if __name__ == '__main__':

    # 读取键盘任意输入
    data = input("Please input a string: ")

    # 以空格切割输入的字符串
    list_data = data.split(' ')

    # 打印切割后的列表数据
    print(list_data)