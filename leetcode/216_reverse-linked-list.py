"""
https://leetcode.cn/problems/reverse-linked-list/description/

206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

头插法的本质理解
头插法是链表操作中一种常用的节点插入策略，核心思想是每次将新节点插入到目标链表的头部，从而实现链表的反转或重组。
举个例子：
原链表：1 → 2 → 3 → null（头节点是 1）
目标是构建一个新链表，通过头插法依次插入原链表的节点：
插入 1 到空链表：1 → null（新链表头是 1）
插入 2 到新链表头部：2 → 1 → null（新链表头是 2）
插入 3 到新链表头部：3 → 2 → 1 → null（新链表头是 3）
最终得到反转后的链表。
"""

from typing import List, Optional

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # 代码实现逻辑：迭代法，本质是头插法的变形
    # time complexity：O(n)，其中 n 为链表节点个数。
    # complexity：O(1)，仅用到若干额外变量。
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None  # 指向已反转链表的头节点（初始时为空链表）（初始时无节点，为 null）。
        cur = head  # 指向当前正在处理的节点（从原链表头开始）（从原链表的头节点开始，逐个向后遍历）。
        # 每次处理一个节点，将其插入到已反转链表的头部
        while cur: # 当cur不为空时，还有节点需要处理
            next = cur.next  # 保存当前节点的下一个节点（避免断链）
            cur.next = pre   # 将当前节点的next指向已反转链表的头节点（实现“头插”）
            pre = cur        # 已反转链表的头节点更新为当前节点
            cur = next       # 处理下一个节点
        return pre
