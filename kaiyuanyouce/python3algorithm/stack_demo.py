#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-29 15:36'

"""
https://mp.weixin.qq.com/s/5VFc7Z_pcQQgZXz1M4ElBg

什么是堆栈，简单而言：后进先出

算法原理：

1.进栈（PUSH）算法

若TOP≥n时，则给出溢出信息，作出错处理（进栈前首先检查栈是否已满，满则溢出；不满则作2）

置TOP=TOP+1（栈指针加1，指向进栈地址）

S(TOP)=X，结束（X为新进栈的元素）

2.退栈（POP）算法

若TOP≤0，则给出下溢信息，作出错处理(退栈前先检查是否已为空栈， 空则下溢；不空则作2)

X=S(TOP)，（退栈后的元素赋给X）

TOP=TOP-1，结束（栈指针减1，指向栈顶）

"""


# 算法实现：示例中利用python list的特性，实现堆栈的算法原理


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
        print(self.stack)  # 入栈

    def push(self, obj):
        if self.is_full():
            raise Exception("堆栈满了……")
        else:
            self.stack.append(obj)
            self.top += 1

    # 出栈
    def pop(self):
        if self.is_empty():
            raise Exception("堆栈是空的……")
        else:
            self.top -= 1
            return self.stack.pop()


if __name__ == "__main__":

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

    # 打印下堆栈的内容，此时应该是[1,2,3,4]
    stack.show()
