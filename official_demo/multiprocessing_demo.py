# coding=utf-8
"""
DATE:   2021/8/13
AUTHOR: TesterCC
"""

# 基于进程的并行 https://docs.python.org/zh-cn/3/library/multiprocessing.html

from multiprocessing import Pool

def f(x):
    return x*x*x

if __name__ == '__main__':
    # 最基本的使用
    with Pool(4) as p:
        print(p.map(f,[1,2,3,4,5]))