# -*- coding: utf-8 -*-
# 载荷批量转换 test on Windows10
# 7z cmd需要windows安装7zip(并设置环境变量)或Linux安装p7zip
import subprocess
import traceback

import os
import shutil


def list_folders(dir_path):
    contents = os.listdir(dir_path)

    folders = [item for item in contents if os.path.isdir(os.path.join(dir_path, item))]

    return folders


def rename_folder(dir_path, old_name, new_name):
    old_path = os.path.join(dir_path, old_name)
    new_path = os.path.join(dir_path, new_name)

    try:
        os.rename(old_path, new_path)
        print(f"[D] old dir {old_name} had already renamed as {new_name}")
    except OSError as e:
        print(f"[E] Can't rename dir: {old_name} , err： {e}")


def delete_folder(dir_path, folder_name):
    folder_path = os.path.join(dir_path, folder_name)

    try:
        # os.rmdir(folder_path) # just delete empty dir
        shutil.rmtree(folder_path)
        print(f"[D] dir {folder_path} had deleted.")
    except OSError as e:
        print(f"[E] dir {folder_name} can not delete, err: {e}")


def create_7z_archive(dir_path, archive_name):
    cmd = f"7z a -r {archive_name}.7z {dir_path}"
    print(cmd)
    try:
        # subprocess.run(cmd, shell=True, check=True)
        ret_code, output = subprocess.getstatusoutput(cmd)
        print(ret_code, output)
        print(f"[D] directory {dir_path} successfully zip {archive_name}")
    except subprocess.CalledProcessError as e:
        print(f"[E] Error in 7z process...")


if __name__ == '__main__':
    origin_dir = r"E:\ws_py\Python3Scripts\dev_demo\test_rename_payload"

    loop_dirs = list_folders(origin_dir)
    # print(loop_dirs)

    for loop_dir in loop_dirs:
        sub_dirs = list_folders(loop_dir)
        print(f"[I] {loop_dir} sub dirs: {sub_dirs}")
        if "document" in sub_dirs:
            rename_folder(loop_dir, "document", "instruction")
        if "payload" in sub_dirs:
            rename_folder(loop_dir, "payload", "execution")
        if "source" in sub_dirs:
            rename_folder(loop_dir, "source", "source_code")  # real operation：real dir with code
            # delete_folder(loop_dir, "source")  # 正式交付前
        if "video" in sub_dirs:
            delete_folder(loop_dir, "video")

        loop_dir_path = os.path.join(origin_dir, loop_dir)
        # print(">>>>>> ", loop_dir_path)
        # need run in terminal, IDE will report 7z file cannot find
        create_7z_archive(loop_dir_path, loop_dir)
