# coding=utf-8

import os
import socket
import sys
import time
import traceback
import json


# 根据ftp目录文件情况，修改配置文件
def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


def monitor_ftp():
    dir_path = r'/opt/ftp/pub/'

    try:

        main_file = sys.executable if os.name == 'nt' and not sys.executable.endswith('python.exe') else __file__
        config_path = os.path.dirname(main_file) if os.path.sep in main_file else '.'
        config_file = '%s%s%s' % (config_path, os.path.sep, 'log_proxy.json')

        # 读取当前配置文件信息
        with open(config_file) as f:
            config = json.load(f)
        log_file_map = config['log_file']
        # print("1.log_file_map: {}".format(log_file_map))

        config_exist_files = log_file_map.keys()

        # 遍历目录下所有文件，发现新增文件，就修改配置
        for root, dirs, files in os.walk(dir_path):

            cur_files = [dir_path + fi for fi in files if not is_chinese(fi) if fi.split(".")[0]]

            if cur_files:

                for cf in cur_files:
                    # print("cf: {}".format(cf))
                    if cf not in config_exist_files:
                        config['log_file'][cf] = 0

                # print("4.config['log_file']: {}".format(config['log_file']))
                with open(config_file, 'w') as f:
                    json.dump(config, f, indent=4)

                # 重启 rc.local 若命令执行成功，则返回0
                res = os.system("systemctl restart rc-local")
                if res != 0:
                    print("[x] restart log_proxy fail...")

    except:
        traceback.print_exc()
        # sys.exit()
        pass


while True:
    # 考虑到程序稳定性，改为30秒（如有必要，10s一次应该也可以），否则会因为重启间隔太少引发报错，要和log_proxy错开时间，否则两个都不能启动
    time.sleep(30)
    monitor_ftp()
