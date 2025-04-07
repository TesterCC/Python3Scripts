# https://www.bilibili.com/video/BV1Lk4y117Cb?p=7
# LeetCode刷题常用数据结构
# Array数组，其实python中叫list列表，go和java里都叫数组
# 读快，用索引；查询慢

a = [1,2,3,4,5,6,7]
print(a[3])
print("-"*33)

# https://www.bilibili.com/video/BV1Lk4y117Cb?p=8
# LinkList 链表
'''数组和链表的区别
数组 vs 链表

数组：访问快，搜索慢，插入和删除也慢
链表：插入删除快，搜索慢

'''

# Define for singly-linked list. initial
class ListNode:
    def __init__(self, x):
        self.val = x      # 表示当前value值
        self.next = None  # 表示下一个指针，最后一个的self.next也指向None


