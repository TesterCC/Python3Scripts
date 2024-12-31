# coding=utf-8
"""
DATE:   2022/5/24
AUTHOR: TesterCC
"""

"""
5.2 打印输出至文件中

问题：将print()函数的输出重定向到一个文件中去。

解决方案：
在print()函数中指定file关键字参数。
"""
# 文件必须是以文本模式打开，如果是二进制模式，打印就会出错。
with open("print_log.txt", "wt", encoding="utf-8") as f:
    print("测试2022!！",file=f)