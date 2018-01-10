# -*- coding:utf-8 -*-

"""
Task001-2
随机生成100个10至1000之间的数,对生成的100个数进行排序,
禁止使用Python自带的排序函数,要自己实现排序函数
"""

import random


# random_data = [randint(10, 1001) for i in range(100)]
# print(data)


class MySort:
    """
       生成随机数,返回排序后的结果
       start, end为限制随机数生成的范围
       count为生成的随机数个数
    """

    def __init__(self, start, end, count):
        """
        初始化数据
        """
        self.start = start
        self.end = end
        self.count = count

        # 生成随机实数列表
        self.__random_data = [random.uniform(self.start, self.end) for i in range(self.count)]

    def get_random_data(self):
        return self.__random_data

    def sort(self):
        """
        对随机实数列表进行排序 冒泡排序
        冒泡排序原理：
        从数组下标为0的位置开始，比较下标位置为0和1的数据，
        如果0号位置的大，则交换位置，如果1号位置大，则什么也不做，
        然后右移一个位置，比较1号和2号的数据，和刚才的一样，如果1号的大，则交换位置，
        以此类推直至最后一个位置结束，到此数组中最大的元素就被排到了最后，
        之后再根据之前的步骤开始排前面的数据，直至全部数据都排序完成。
        """
        array = self.get_random_data()
        n = len(array)

        if n <= 1:
            return array
        else:
            for i in range(n):
                for j in range(0, n-i-1):
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
            return array


if __name__ == '__main__':
    sorted_data = MySort(10, 1000, 100)

    print(sorted_data.get_random_data())

    # 打印排序后的结果
    print(sorted_data.sort())   # 输入list，但格式不好看，想好看就遍历

    for num in sorted_data.sort():
        print(num)



