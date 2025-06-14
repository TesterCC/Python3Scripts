# -*- coding=utf-8 -*-

import os
import argparse
from pathlib import Path


def count_unique_yaml_files(directory):
    """
    遍历指定目录下所有名称不同的YAML文件并统计数量

    参数:
        directory: 要遍历的目录路径

    返回:
        不同名称的YAML文件数量
    """
    # 用于存储已发现的文件名（不含扩展名）
    unique_files = set()

    # 遍历目录中的所有文件
    for root, _, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否为.yml或.yaml
            if file.lower().endswith(('.yml', '.yaml')):
                # 获取文件名（不含扩展名）
                name_without_ext = os.path.splitext(file)[0]
                # 添加到集合中（自动去重）
                unique_files.add(name_without_ext)
    print(f"all yaml files name: {unique_files}")
    return len(unique_files)


def main():
    # 直接使用固定的目录路径
    directory = './semgrep-rules'  # 当前目录

    # 验证目录是否存在
    if not os.path.isdir(directory):
        print(f"错误: '{directory}' 不是一个有效的目录")
        return

    # 计算并打印结果
    count = count_unique_yaml_files(directory)
    print(f"在目录 '{directory}' 中发现了 {count} 个名称不同的YAML文件")

if __name__ == "__main__":
    main()
