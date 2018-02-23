# -*- coding: utf-8 -*-
"""

http://blog.chinaunix.net/uid-21374062-id-5198995.html
仿Linux命令tree生成树形目录结构，

并汇总当前目录下文件
http://blog.csdn.net/huang_yx005/article/details/52299460

Python显示目录的树形结构
"""
import os


def fileCntIn(currPath):
    """汇总当前目录下文件数"""
    return sum([len(files) for root, dirs, files in os.walk(currPath)])


def dirsTree(startPath):
    """树形打印出目录结构"""
    for root, dirs, files in os.walk(startPath):
        # 获取当前目录下文件数
        fileCount = fileCntIn(root)
        # 获取当前目录相对输入目录的层级关系,整数类型
        level = root.replace(startPath, '').count(os.sep)
        # 树形结构显示关键语句
        # 根据目录的层级关系，重复显示'| '间隔符，
        # 第一层 '| '
        # 第二层 '| | '
        # 第三层 '| | | '
        # 依此类推...
        # 在每一层结束时，合并输出 '|____'
        indent = '| ' * 1 * level + '|____'
        # print '%s%s fileCount:%s' % (indent, os.path.split(root)[1], fileCount)
        print('%s%s' % (indent, os.path.split(root)[1]))


if __name__ == '__main__':
    path = u"/Users/TesterCC/Development/python_workspace/Python_Network"
    dirsTree(path)
