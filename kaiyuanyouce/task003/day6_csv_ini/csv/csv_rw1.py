# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/5 15:38'

"""
1.先使用writer函数写一个csv文件

2.使用reader函数读取上述步骤写的csv文件内容，并在console中输出

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484123&idx=1&sn=26e850ce17b9ed9fd535e35ed34b8cb8&scene=19#wechat_redirect
"""

import csv


def write_csv():
    # 写csv文件
    print("写入一些简单数据到csv_data.csv文件中")
    with open('csv_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,  # 为打开要写的文件对象
                                delimiter=','  # 分隔符
                                )
        spamwriter.writerow(['csv_demo'] * 5 + ['FullStakPentest'])
        spamwriter.writerow(['hello',
                             'Study Python3', 'Auto Testing'])

        csvfile.close()


def read_csv():
    print("读取csv_data.csv问内容:")
    with open('csv_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print("row的类型： ", type(row))
            print(row)

            # 遍历每行中每个数据项
            print("遍历每行中每个数据项:")
            for data in row:
                print(data, end="  ")
            print("")    # 格式问题

        f.close()


if __name__ == '__main__':
    print("python csv文件写读操作示例:")
    write_csv()
    print('---' * 30)
    read_csv()
