# -*- coding:utf-8 -*-
# 算法图解 P7 1.2

def binary_search(arr, target):
    # 基准条件自己做判断
    # 二分查找的核心算法
    # 范围值是目标在列表中的索引
    low = 0     # 查找范围的最大值
    high = len(arr) - 1    # 查找范围的最小值，索引从0开始，所有范围是len(arr)-1

    # 只要范围没有缩小到只包含一个元素，就检查中间元素
    while low <= high:
        mid = (low + high) // 2  # 检查中间元素 , python3自动向下取整
        #  只要范围没有缩小到只包含一个元素，就检查中间元素
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # 中间值都比目标值大，自然下一次遍历最大值要比现在的mid小才行，故为 mid-1
            high = mid - 1
        else:
            # arr[mid] < target
            # 中间值都比目标值小，下次的最小值也应该比中间值大
            low = mid + 1
    return None

if __name__ == '__main__':
    List1 = [-2,-1, 0, 1, 2, 3, 4, 5,7,9,11]
    List2 = [2, 3, 4, 5, -2,-1, 0, 1,7,9,11]
    print(binary_search(List1, 7))
    print(binary_search(List1, -1))
    print(binary_search(List2, 0))
