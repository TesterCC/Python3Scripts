# coding=utf-8
"""
DATE:   2021/6/8
AUTHOR: Yanxi Li
"""

# 获取指定目录下的所有文件名
import os

FileList = []

file_path = r"E:\11ebook\SecDev\sample_books"
FileNames = os.listdir(file_path)

#print(FileNames)
for i in FileNames:
    # print(i)
    if i.split(".")[0]:
        print(i.split(".")[0])
