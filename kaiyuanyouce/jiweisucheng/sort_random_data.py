# -*- coding:utf-8 -*-

import random

'''
    随机生成100个10至1000之间的数，对生成的100个数进行排序，禁止使用Python自带的排序函数，要自己实现排序函数
'''


class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.random_data = [] 
    
    # 生成数据
    def __generator(self):
        # 生成指定范围指定数量的随机数
        
        for i in range(0, self.count):
            self.random_data.append(random.uniform(self.start, self.end))

    # 实现排序
    def sort(self):
        
        self.__generator()

        # 用冒泡排序来实现
        # 计算待排序数据长度
        n = len(self.random_data)

        for i in range(0, n):
            for j in range(1, n-i):
                if self.random_data[j-1] > self.random_data[j]:
                    self.random_data[j-1], self.random_data[j] = self.random_data[j], self.random_data[j-1]

        return self.random_data


# 使用示例
if __name__ == "__main__":
    sorted_data = MySort(10, 1000, 100)

    # 排序
    data = sorted_data.sort()

    # 打印排序后的结果
    for d in data:
        print(d)
