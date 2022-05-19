# coding=utf-8
"""
DATE:   2021/12/21
AUTHOR: TesterCC
DESC:   将同目录下多个日志文件合并到一个文件中
# draft
"""

import os

# 日志所在目录
path = r"/tmp/log_merge/"
# print(os.path.dirname(__file__))
all_log_name = "log_all"

# 获取文件夹下所有文件名称
files = os.listdir(path)
print(files)

# 遍历合并文件写入一个文件中, windows下需要调试路径
for file in files:
    f = open(path + file).read()  # 将打开的文件内容保存到变量f
    log = open(path + all_log_name, 'a+')  # 以追加模式打开文件
    log.write(f)  # 写入文件
    print('已经合并：' + file)

print("[-] Finish cat logs, save all log in: {}".format(path + all_log_name))
