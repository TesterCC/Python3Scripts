# -*- coding: UTF8 -*-
import os
import time


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def GetFileCreateTime(file_path):
    # '''获取文件的创建时间'''
    t = os.path.getctime(file_path)
    return TimeStampToTime(t)


def GetFileModifyTime(file_path):
    # '''获取文件的修改时间'''
    t = os.path.getmtime(file_path)
    return TimeStampToTime(t)


def GetFileAccessTime(file_path):
    # '''获取文件的访问时间'''
    t = os.path.getatime(file_path)
    return TimeStampToTime(t)


def GetFileSize(file_path):
    # '''获取文件的大小,结果保留两位小数，单位为MB'''

    fsize = os.path.getsize(file_path)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


if __name__ == '__main__':
    path = r"note.txt"
    print(GetFileCreateTime(path))
    print(GetFileModifyTime(path))
    print(GetFileAccessTime(path))
    print(GetFileSize(path))
