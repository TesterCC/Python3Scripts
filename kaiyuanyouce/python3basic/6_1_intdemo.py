#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/20 21:01'

'''
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484016&idx=2&sn=f16f4b5accfdb85e258f1819f4779eb6&scene=19#wechat_redirect
'''

if __name__ == '__main__':
    x = 1.68
    y = 10

    # 将x转换为整数
    print(int(x))

    # 将y转换为浮点数
    print(float(y))

    # 复数: a + bj
    # 将x转换为复数， 实数部分为x，虚数部分为0
    print(complex(x))

    # 将x，y转换为复数， 实数部分为x，虚数部分为y
    print(complex(x, y))