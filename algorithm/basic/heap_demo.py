"""
Heap堆（大堆，小堆）

大堆：每次从一组数据中取出顶端数据是最大值
小堆：每次从一组数据中取出顶端数据是最小值

ref:
https://www.bilibili.com/video/BV1Lk4y117Cb?p=12

Python中的表示:
Python中叫堆heapq，Java中叫PriorityQueue

这种数据结构适合前k个数据这种题
"""

from heapq import heapify, heappush, heappop, nlargest, nsmallest
import heapq

'''
heapify()  # 将一个list转变成heap, 默认是小堆
heappush   # 放入一个值
heappop    # 删除一个值
nlargest   # 前n个中最大的值
nsmallest  # 前n个中最小的值
'''

a = [1, 2, 3]
print(type(a))

# 小堆
heapify(a)  # 变成小堆
heappush(a, 4)
print(a)   # [1, 2, 3, 4]
# print(type(a))  # debug

heappop(a)   # 小堆弹出最小值
print(a)     # [2, 3, 4]

print(nlargest(2, a))   # 最大的2个值  [4, 3]
print(nsmallest(2, a))  # 最小的2个值  [2, 3]

print("--"*11)
# 以前Python3默认没有支持大堆,所以如果是整数，可以把各个元素*-1来处理，但是最终输出时也要乘*-1来还原
# 现在也有大堆函数了，可以直接
b = [1,2,3]
heapq._heapify_max(b)  # 变成大堆
print(b)
heapq._heappop_max(b)
print(b)