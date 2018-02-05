# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/5 15:38'

"""
在Python csv模块中还提供了另外一种方式来读写csv文件，就是通过字典方式来读写，其提供的主要方法为：DictReader、DictWriter
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484123&idx=1&sn=26e850ce17b9ed9fd535e35ed34b8cb8&scene=19#wechat_redirect
"""

import csv


def csv_dict_write():
    # 写csv文件
    print("写入一些简单数据到csv_dict_data.csv文件中")

    with open('csv_dict_data.csv', 'w') as csvfile:
        # 写csv头
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 写csv内容
        writer.writerow({'first_name': 'Baked',
                         'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely',
                         'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful',
                         'last_name': 'Spam'})


def csv_dict_read():
    print("读取csv_dict_data.csv问内容:")
    with open('csv_dict_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 遍历每行中的数据
            print(row['first_name'], row['last_name'])


if __name__ == '__main__':
    print("python csv文件字典写读操作示例：")
    csv_dict_write()
    print("---"*30)
    csv_dict_read()

