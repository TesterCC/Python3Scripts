"""
Queue 队列
FIFO, First In First Out,先进先出

进来的顺序：1,2,3,4
出去的顺序：1,2,3,4

一般在BFS（广度优先）算法中用到

双端队列 左右都可以顺序进出

Python中的表示方法：
1.list
2.collections.deque   双端队列 # from collections import deque

一般的组合使用：
1.append() 和 popleft() 组合
2.appendleft() 和 pop()组合


ref:
https://www.bilibili.com/video/BV1Lk4y117Cb/?p=10
"""

from collections import deque
q = deque([1,2,3])

print(q)

q.append(4)
print(q)

q.pop()
print(q)

q.appendleft(0)
print(q)

q.popleft()
print(q)

print(max(q))
print(min(q))
print(len(q))

