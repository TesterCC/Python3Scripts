# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/12 13:03'

"""
heap是堆，stack是栈

数据结构-堆栈
什么是堆栈，简单而言：后进先出。(LIFO)

使用了python list的特性，实现了堆栈的算法原理

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484073&idx=1&sn=952a299c4912aa52ae287d1888ff7eb0&scene=19#wechat_redirect
"""


class Stack:
    def __init__(self, size=30):
        # 初始化堆栈大小
        self.size = size

        # 初始化堆栈列表
        self.stack = []

        # 初始化堆栈默认top值
        self.top = -1

    # 设置堆栈大小
    def set_size(self, size):
        self.size = size

    # 判断堆栈是否为空
    def is_empty(self):
        res = False
        if self.top == -1:
            res = True
        return res

    # 判断堆栈是否满了
    def is_full(self):
        res = False
        if self.top + 1 == self.size:
            res = True
        return res

    # 打印堆栈里所有内容
    def show(self):
        print(self.stack)   # 入栈

    # 压入
    def push(self, obj):
        if self.is_full():
            raise Exception("堆栈满了")
        else:
            self.stack.append(obj)
            self.top += 1

    # 出栈
    def pop(self):
        if self.is_empty():
            raise Exception("堆栈是空的")
        else:
            self.top -= 1
            return self.stack.pop()


if __name__ == '__main__':
    print("堆栈实现示例")
    # 初始一个长度为5的堆栈实例
    stack = Stack(5)

    # 入栈 整数1-5
    for index in range(1, 6):
        stack.push(index)

    # 打印下堆栈的内容
    stack.show()

    # 出栈, data的值应该为5
    data = stack.pop()
    print(data)

    # 打印下堆栈的内容，弹出最后进入的5，此时应该是[1,2,3,4]
    stack.show()
