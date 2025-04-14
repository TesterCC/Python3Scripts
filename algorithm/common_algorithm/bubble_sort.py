#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/7 11:15'


"""
标准解法：
冒泡排序原理即：
从数组下标为0的位置开始，
比较下标位置为0和1的数据，如果0号位置的大，则交换位置，如果1号位置大，则什么也不做，然后右移一个位置，
比较1号和2号的数据，和刚才的一样，如果1号的大，则交换位置，
以此类推直至最后一个位置结束，到此数组中最大的元素就被排到了最后，之后再根据之前的步骤开始排前面的数据，直至全部数据都排序完成。
http://blog.csdn.net/mrlevo520/article/details/77829204


冒泡算法的原理是比较相邻的元素,如果第一个比第二个大（正序，升序），就交换他们两个的位置，然后继续往下找，每次找出最大或最小的那个值放在顶端

时间复杂度：
最坏和平均时间复杂度：O(N^2)

空间复杂度：
O(1)

稳定排序

缺点: 冒泡排序解决了桶排序浪费空间的问题, 但是冒泡排序的效率特别低
"""


def bubble_sort(nums):
    len_list = len(nums)

    if len_list <= 1:
        return nums
    else:
        # 对于长度为 n 的列表，最多需要进行 n - 1 轮冒泡排序，就可以确保整个列表有序。因为在第 n - 1 轮排序结束后，剩下的最后一个元素必然是最小的，此时整个列表已经完成排序。
        for i in range(len_list-1):
            # i：是外层循环的计数器，代表当前正在进行第几轮排序。每一轮排序结束后，就会有一个元素被排到正确的位置。
            for j in range(len_list-i-1):    # j为列表下标，每轮剩下的最后一个元素必然是最小的
                if nums[j] > nums[j+1]:         # 如果第一个比第二个大（正序，升序）
                    nums[j], nums[j+1] = nums[j+1], nums[j]       # 就交换他们两个的位置
        return nums


if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    List2 = [-3, 8, 12, 0, 3, 1, 5, 9, 6]
    List3 = [6]
    List4 = [4, 4]
    List5 = [5, 5, 5]
    print(bubble_sort(List))
    print(bubble_sort(List2))
    print(bubble_sort(List3))
    print(bubble_sort(List4))
    print(bubble_sort(List5))

    print("reverse list: ")
    ret = bubble_sort(List)
    ret.sort(reverse=True)
    print(ret)