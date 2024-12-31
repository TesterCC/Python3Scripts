# coding=utf-8
"""
DATE:   2020/11/25
AUTHOR: Yanxi Li

https://docs.python.org/zh-cn/3/library/multiprocessing.html
"""

from multiprocessing import Pool


def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(10) as p:
        print(p.map(f,[i for i in range(100)]))  # 1000就很慢了