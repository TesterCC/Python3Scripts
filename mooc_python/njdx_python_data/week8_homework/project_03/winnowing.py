#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-06 21:59'

"""
项目3：文档相似性比较

主要步骤：
1. 处理文档
2. 构建分片集合 
3. 构建哈希值集合 
4. 提取特征指纹 
5. 进行比较

"""

import re
import os


# 处理文档
def preprocessing(filename):
    file = open(filename)
    content = file.read()
    word = re.compile(r'[^a-zA-Z]')
    content = word.sub('', content)
    content = content.lower()
    return content


# 生成n-gram模型，构建分片集合
def generate_n_gram(content, n):
    n_gram = []
    for i in range(len(content) - n + 1):
        n_gram.append(content[i:i + n])
    return n_gram


# 构建哈希值集合
def rolling_hashing(n_gram, Base, n):
    hashlist = []
    hash = 0
    initial = n_gram[0]
    # 初始化：Base基数一般设置为素数
    # initial:第一个分片的hash值需要手动计算

    for i in range(n):
        hash += ord(initial[i]) * (Base ** (n - i - 1))
    hashlist.append(hash)

    for i in range(1, len(n_gram)):
        pre = n_gram[i - 1]
        present = n_gram[i]

        hash = (hash - ord(pre[0]) * (Base ** (n - i - 1))) * Base + ord(present[n - 1])
        hashlist.append(hash)

    return hashlist


# 提取特征指纹
def winnowing(hashlist, t, n):
    window = t - n + 1
    minValue = minPos = 0
    fingerprint = {}
    for i in range(len(hashlist) - window + 1):
        temp = hashlist[i:i + window]
        minValue = temp[0]
        minPos = 0
        for j in range(window):
            if temp[j] <= minValue:
                minValue = temp[j]
                minPos = j

        if (i + minPos) not in fingerprint.keys():
            fingerprint[i + minPos] = minValue
    return fingerprint


# 进行比较
def comparison(fingerprint_1, fingerprint_2):
    count = 0
    size = min(len(fingerprint_1), len(fingerprint_2))
    for i in fingerprint_1.values():
        for j in fingerprint_2.values():
            if i == j:
                count += 1
                break
    return count / size


if __name__ == '__main__':
    print('分片大小为5')
    print('检测阈值为9')
    dirpath = os.getcwd()
    path_1 = dirpath + r"/test_1.txt"
    path_2 = dirpath + r"/test_2.txt"
    fingerprint_1 = winnowing(rolling_hashing(generate_n_gram(preprocessing(path_1), 5), 17, 5), 9, 5)
    fingerprint_2 = winnowing(rolling_hashing(generate_n_gram(preprocessing(path_2), 5), 17, 5), 9, 5)
    print("相似度：")
    print(comparison(fingerprint_1, fingerprint_2))  # 0.9277456647398844
