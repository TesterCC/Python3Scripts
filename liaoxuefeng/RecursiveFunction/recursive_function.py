#!/usr/bin/env python
# coding:utf-8

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000


'''
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
'''


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    print(fact(1))
    print(fact(5))
    print(fact(100))
    # print(fact(1000))    # 栈溢出