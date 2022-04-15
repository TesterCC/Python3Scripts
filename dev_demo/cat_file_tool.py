# coding=utf-8
"""
DATE:   2021/12/21
AUTHOR: TesterCC
DESC:   将同目录下多个日志文件合并导一个文件中
knowledge maintain tools
python3 cat_file_tool.py -o all.txt
普通运维工具脚本function-based即可
"""

import os
from optparse import OptionParser


def merge_file(dir,output_name):
    # 日志所在目录
    path = dir
    all_file_name = output_name

    # 获取文件夹下所有文件名称
    files = os.listdir(path)
    print(f'[*] total files count: {len(files)}')  # for debug

    # 遍历合并文件写入一个文件中, windows下需要调试路径
    for file in files:
        f = open(path + file).read()  # 将打开的文件内容保存到变量f
        log = open(path + all_file_name, 'a+')  # 以追加模式打开文件
        log.write(f)  # 写入文件
        print(f'[+] finish merge file ：{file}')

    print(f"[*] Finish merge files, save all files content in: {path + all_file_name}")


def run():
    usage = "Usage: \npython3 %prog --dir [dir_path] --output [output_file_name]"
    parse = OptionParser(usage=usage)
    parse.add_option("-d", '--dir', type="string", dest="dir", help="dir path, e.g. /tmp", default="./")
    parse.add_option("-o", '--output', type="string", dest="output", help="output merge file name, e.g. log_all", default="all")

    options, args = parse.parse_args()

    if not options.dir and not options.output:
        raise FileNotFoundError
    else:
        merge_file(options.dir, options.output)

if __name__ == '__main__':
    run()