# coding=utf-8
"""
DATE:   2021/12/21
AUTHOR: TesterCC
DESC:   读取ti目录下的所有ti，更具IP去重后要展示IP和最近一次的记录时间。

python3 cat_ti_tool.py -o ti.log
"""
'''
knowledge maintain tools
普通运维工具脚本function-based即可
Linux/MacOS:
cat_ti_tool.py 和 要合并的文件最好在同一级。
'''

import os
from optparse import OptionParser

cur_file = os.path.split(__file__)[-1]


def merge_file(dir, output_name):
    # 日志所在目录
    path = dir
    all_file_name = output_name

    # 获取文件夹下所有文件名称
    files = os.listdir(path)
    files = [i for i in files if i != cur_file]  # 以防直接把程序代码合并了。
    print(f'[*] total files count: {len(files)}')  # for debug

    # 内存分析所有数据遍历合并文件写入一个文件中, windows下需要调试路径
    all_content = []
    for file in files:
        f = open(path + file).readlines()  # 将打开的文件内容保存到变量f, list
        f2 = [i.strip() for i in f]
        all_content += f2
        print(f'[+] finish merge file ：{file}, add {len(all_content)} data.')

    # print(all_content)   # list
    # print("**"*30)
    # print(f"[*] Finish merge files, save all files content in: {path + all_file_name}")
    return all_content

data_dict = dict()
def handle_data(data_set:list, output_name):
    for i in data_set:
        ip,ip_time = i.split(",")
        if data_dict.get(ip):
            if int(data_dict.get(ip)) < int(ip_time):
                data_dict[ip] = ip_time
        else:
            data_dict[ip] = ip_time

    print(f"[+] count: {len(data_dict.keys())}, data_dict data:{data_dict}",)
    with open(output_name, 'a+') as f:
        for k,v in data_dict.items():
            f.write(f"{k},{v}\n")

    print(f'[+] finish handle ti file and save at：{os.getcwd()}/{output_name}')

def run():
    usage = "Usage: \npython3 %prog --dir [dir_path] --output [output_file_name]"
    parse = OptionParser(usage=usage)
    parse.add_option("-d", '--dir', type="string", dest="dir", help="dir path, e.g. /tmp", default="./")
    parse.add_option("-o", '--output', type="string", dest="output", help="output merge file name, e.g. log_all",
                     default="all")

    options, args = parse.parse_args()

    if not options.dir and not options.output:
        raise FileNotFoundError
    else:
        all_content = merge_file(options.dir, options.output)
        handle_data(all_content, options.output)

if __name__ == '__main__':
    run()