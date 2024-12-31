# coding=utf-8
"""
DATE:   2021/3/10
AUTHOR: Yanxi Li

avoid SourceCounter-3.5.33.73  check
三引号 python
"""

# 将 数字 1-10 每行一个插入到 num.txt 文件中
with open('num.txt', 'w') as f:
	for i in range(1,11):
		f.writelines(f"{i}\n")

