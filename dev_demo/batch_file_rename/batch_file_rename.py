# -*- coding:utf-8 -*-
import os
import traceback

"""
python3实现将当前目录和子目录下所有文件重命名，比如原始名字为a_xxx.py改为a.py
批量重命名给资源名字批量重命名打广告的资源。
"""
import os

clear_keyword = "xxx"


def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # print(f"[D] old name: {file_path}")   # debug
            base_name, ext = os.path.splitext(filename)
            try:
                # custom replace pattern
                if f'_{clear_keyword}' in base_name:
                    new_base_name = base_name.split('_')[0]
                    new_filename = f"{new_base_name}{ext}"
                    new_file_path = os.path.join(root, new_filename)

                    if not os.path.exists(new_file_path):
                        os.rename(file_path, new_file_path)
                        print(f"[D] new name: {new_file_path}")

                elif clear_keyword in base_name:
                    new_base_name = base_name.replace("【 微信号：itcodeba 】(更多IT资源 www.todo1024.cn)", "")
                    new_filename = f"{new_base_name}{ext}"
                    if clear_keyword in ext:
                        new_filename = f"{new_base_name}"
                    new_file_path = os.path.join(root, new_filename)

                    if not os.path.exists(new_file_path):
                        os.rename(file_path, new_file_path)
                        print(f"[D] new name: {new_file_path}")

            except RuntimeError as err:
                traceback.print_exc()


# current_directory = os.getcwd()
current_directory = r"D:\Download\aaa"
rename_files_in_directory(current_directory)

