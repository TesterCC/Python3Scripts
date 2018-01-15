# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 22:47'

"""
生成器和迭代器
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484049&idx=1&sn=cc9a4ea66a8efa78f975d35a1d35bbef&scene=19#wechat_redirect
"""

import sys


def iterator_demo():
    seq_tuple = (1, 2, 3, 4, 5, 6)

    # 创建迭代器
    seq_it = iter(seq_tuple)

    # 访问打印第一个元素
    print("第一个元素：%s" % next(seq_it))

    # 访问打印第二个元素
    print("第二个元素：%s" % next(seq_it))

    # 访问打印第三个元素
    print("第三个元素：%s" % next(seq_it))

    # 使用for循环来遍历迭代器对象
    print("\nfor循环遍历迭代器对象： ")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x, end=' ')

    # 使用while结合next遍历迭代器对象
    print("\n\nwhile & next遍历迭代器对象： ")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()


if __name__ == '__main__':
    iterator_demo()