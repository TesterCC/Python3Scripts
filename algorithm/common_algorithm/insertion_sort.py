# -*- coding:utf-8 -*-

"""
插入排序是一种简单直观的排序算法。

时间复杂度最坏与平均情况：需 O(n^2) 次比较和移动。
空间复杂度：O(1)，原地排序。

工作原理是将未排序数据插入到已排序序列的合适位置。

基本思路：
插入排序把数组分成已排序和未排序两部分。
起初，第一个元素属于已排序部分，后续元素都在未排序部分。
每一轮中，从未排序部分取出一个元素，将其插入到已排序部分的恰当位置。

具体步骤如下：
1.把第一个元素视为已排序序列。
2.从第二个元素开始，将其与已排序序列中的元素依次比较，找到合适的位置插入。
3.重复步骤 2，直到整个数组排序完成。

插入排序是 稳定排序，相等元素的相对顺序在插入时保持不变。

优化方向：
希尔排序：通过分组插入排序优化整体效率（时间复杂度可降至 O(n1.3)。
"""
import random


def generator():
    """
    测试数据生成函数，随机生成1-1000之间无序序列整数数据
    """
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


def insertion_sort(arr):
    n = len(arr)
    # 从第二个元素开始遍历数组,（索引范围是1到n-1）
    for i in range(1, n):
        # 当前待插入元素
        current = arr[i]
        # 已排序区间的末尾索引
        j = i - 1
        # 将当前元素current与已排序元素从后向前比较
        # j >= 0确保不越界访问数组（当 j = -1 时终止循环）；
        # current < arr[j]：若当前元素小于已排序元素，触发后移操作。
        while j >= 0 and current < arr[j]:
            # 将 arr[j]（较大的已排序元素）复制到后一位，为 current 腾出插入空间。效果：已排序区间中比 current 大的元素全部后移一位。
            arr[j + 1] = arr[j]
            j -= 1  # 索引指向前一个已排序元素，arr[j+1]留出空间
        # 当循环终止时，j 指向第一个小于等于 current 的元素位置（或 j=-1）。
        # 插入 current 到合适的位置，j + 1 即为 current 的正确位置。
        arr[j + 1] = current   # 插入到正确位置
    return arr


if __name__ == '__main__':

    # 测试示例
    print("插入排序示例1, 测试指定数组：")
    arr = [12, 11, 13, 5, 6, 1, 7]
    print("原始数组:", arr)

    sorted_arr = insertion_sort(arr)
    print("插入排序后的数组:", sorted_arr)

    print("插入排序示例2, 测试随机数组：")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print("生成随机序列：")
    print(random_data)

    # 插入排序
    sorted_data = insertion_sort(random_data)

    # 打印排序结果
    print("完成插入排序的序列：")
    print(sorted_data)