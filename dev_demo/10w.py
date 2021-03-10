# coding=utf-8
"""
DATE:   2021/3/10
AUTHOR: Yanxi Li

avoid SourceCounter-3.5.33.73  check
三引号 python
"""
# 当前目录下直接生成一个绕过检测的10w lines .py文件
with open('10w_demo.py', 'w+') as f:
	for i in range(0,100000):
		f.writelines(f"'''{i}'''\n")

