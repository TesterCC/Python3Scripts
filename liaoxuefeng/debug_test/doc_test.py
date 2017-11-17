#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/17 21:54'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000
文档测试
"""

import doctest


def abs(n):
    '''
    Function to get absolute value of number.
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else -n

if __name__ == '__main__':
    doctest.testmod()     # 固定执行语句，如果有错就会提示
