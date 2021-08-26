# coding=utf-8
"""
DATE:   2021/8/13
AUTHOR: TesterCC
"""

# 基于进程的并行 https://docs.python.org/zh-cn/3/library/multiprocessing.html
# Process类
# 显示所涉及的各个进程ID，这是一个扩展示例
import os
from multiprocessing import Process



def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print(f"Hello, {name}")


if __name__ == '__main__':
    # 最基本的使用，和Threading使用相似
    info('main line')
    p = Process(target=f, args=('alice',))
    p.start()
    p.join()
