# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/12 21:15'


"""
什么是队列，简单而言：先进先出。 (FIFO, First in first out)
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484074&idx=1&sn=3d653e0211403def9d46a59eecaa9453&scene=19#wechat_redirect
"""


class Queue:

    def __init__(self, size=30):
        # 初始化队列长度
        self.size = size

        # 初始化队列列表
        self.queue = []

        # 初始化队列前端、后端位置
        self.front = 0
        self.rear = -1

    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.rear == 0   # return True or False

    def is_full(self):
        """
        判断队列是否满了
        """
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True
        return res

    # 入队
    def add(self, obj):
        if self.is_full():
            raise Exception("队列满了")
        else:
            self.queue.append(obj)
            self.rear += 1

    # 出队
    def delete(self):
        if self.is_empty():
            raise Exception("队列是空的，出不了")
        else:
            self.rear -= 1
            self.queue.pop(0)

    # 队列头元素
    def first(self):
        if self.is_empty():
            raise Exception("队列是空的")
        else:
            return self.queue[self.front]

    # 队列尾元素
    def last(self):
        if self.is_empty():
            raise Exception("队列是空的")
        else:
            return self.queue[self.rear]

    # 打印队列
    def show(self):
        print(self.queue)


if __name__ == "__main__":

    print("队列实现示例:")

    # 初始化长度为5的队列
    queue = Queue(5)

    # 先把1-5的数据入队
    for index in range(1, 6):
        queue.add(index)

    # 打印下队列数据
    queue.show()

    # 打印下队列头
    print(queue.first())

    # 打印下队列尾
    print(queue.last())

    # 出个队试试
    print("delete一个")     # 先进先出
    queue.delete()

    # 打印下队列看下是否出队了
    queue.show()

    # 再出个队试试
    print("再delete一个")
    queue.delete()

    # 打印下队列看下是否出队了
    queue.show()
