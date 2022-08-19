# coding:utf-8

# 读取文件内容到内存后删除原文件，达成无文件落地效果（虽然不够优雅）
import os

with open('./test.txt','r+') as f:
    file = f.readlines()

print(file)

print(f"delete test.txt")
os.remove('./test.txt')

file.append("TesterCC")
print(file)