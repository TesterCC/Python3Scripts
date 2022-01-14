# coding=utf-8
"""
DATE:   2022/1/14
AUTHOR: TesterCC
DES: python3移动文件

ref: https://www.jianshu.com/p/b96b3c3f05ea

昨天接到一个需求，说是一个服务的一个盘的磁盘空间不够，总是被缓存占满，而且使用的第三方的软件，导致经常磁盘空间不足，所以写一个每天定时移动文件到另外一个磁盘的脚本。
"""

import os
import shutil
import time

# 定是移动文件文件夹到固定目录脚本

old_path = "/Users/Jerry/Desktop/11"
new_path = "/Users/Jerry/Desktop/11_copy"
times_sleep_s = 10   # 60*60*24

def getSubDic(old_p):
    f = os.listdir(old_p)
    for item in f:
        if item[0] == '.':
            continue
        sub_path = '/'+item
        print(sub_path)
        full_sub_path = old_p+sub_path
        # if os.path.exists(full_sub_path):
        if os.path.isdir(full_sub_path):#遍历目录
            print(full_sub_path+' is exit')
            getSubDic(full_sub_path)
        elif os.path.isfile(full_sub_path):#移动文件
            getMoveToPath(full_sub_path)
        else:
            print("error:"+full_sub_path+" not understand")

def getMoveToPath(sub_Path):
    if os.path.exists(new_path):
        if sub_Path:
            # r_index = sub_Path.rfind(old_path,0,len(sub_Path))
            full_new_path = new_path + sub_Path[len(old_path):]
            full_old_path = sub_Path
            new_path_dir = os.path.dirname(full_new_path)
            if os.path.exists(new_path_dir):#目录是否存在
                if os.path.exists(full_new_path):#文件存在
                    if os.path.getsize(full_new_path) != os.path.getsize(full_old_path):
                        print('正在复制文件:' + full_new_path)
                        shutil.move(full_old_path,full_new_path)
                else:
                    print('正在复制文件:' + full_new_path)
                    shutil.move(full_old_path,full_new_path)
            else:
                os.makedirs(new_path_dir)
                getMoveToPath(sub_Path)
    else:
        os.mkdir(new_path)
        getMoveToPath(sub_Path)

if  __name__ == '__main__':
    while True:
        getSubDic(old_path)
        print("循环一次")
        time.sleep(times_sleep_s)