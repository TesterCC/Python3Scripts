# coding=utf-8
"""
DATE:   2021/12/21
AUTHOR: TesterCC
DESC: 13位时间戳转10位时间戳
"""

import time


# # print(var) # 13
# str_time = datetime.datetime.fromtimestamp(var / 1000)
#
# print(str_time)
# # str_time = '2016-03-19 13:27:00'
# t10 = time.mktime(time.strptime(str_time, '%Y-%m-%d %H:%M:%S'))
# t = int(t10)
# print(t)
#
#
# temp = datetime.datetime.fromtimestamp(var / 1000).strftime("%Y-%m-%d %H:%M:%S")
#
# t10b = time.mktime(time.strptime(temp, '%Y-%m-%d %H:%M:%S'))
# print(int(t10b))


def timestamp13to10(timeNum):
    # 13位时间戳转10位时间戳
    # 输入毫秒级的时间(13位时间戳)，转出正常格式的str时间
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(otherStyleTime)

    # 将"2011-09-28 10:00:00"转化为时间戳(10位时间戳)
    return int(time.mktime(time.strptime(otherStyleTime,'%Y-%m-%d %H:%M:%S')))

if __name__ == '__main__':
    var = 1639954854052
    ret = timestamp13to10(var)
    print(var)  # input 13 ts
    print(ret)  # output 10 ts