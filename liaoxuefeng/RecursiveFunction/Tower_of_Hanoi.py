#!/usr/bin/env python
# coding:utf-8

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000
# 汉诺塔的移动可以用递归函数非常简单地实现

'''
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法
https://www.zhihu.com/question/37152936

'''


def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


if __name__ == '__main__':
    move(3, 'A', 'B', 'C')