# coding=utf-8
"""
DATE:   2021/8/13
AUTHOR: TesterCC
"""

# 基于进程的并行 https://docs.python.org/zh-cn/3/library/multiprocessing.html
# Process类

from multiprocessing import Process


def f(name):
    print(f"Hello, {name}")


if __name__ == '__main__':
    # 最基本的使用，和Threading使用相似
    p = Process(target=f, args=('alice',))
    p.start()
    p.join()
