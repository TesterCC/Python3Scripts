# coding=utf-8
"""
DATE:   2021/6/8
AUTHOR: Yanxi Li
"""

# 简易救济小脚本，获取指定目录下的所有文件名
import os

FileList = []

file_path = r"D:\xx\yyy"   # 指定文件所在目录
FileNames = os.listdir(file_path)

#print(FileNames)
for i in FileNames:
    # print(i)
    print(i.split(".")[0])
