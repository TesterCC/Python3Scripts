# coding=utf-8
"""
DATE:   2021/2/4
AUTHOR: Yanxi Li
"""

import json
import os

# 读取样本原始日志信息
with open('./poc_v2.json', 'r') as f:
    data = json.load(f)

print("poc_v2.json count: ", len(data))
# print(type(data))
# print(data)

sample_char = "test.ssms.cn:8002/plugins/v3.400.7-win64/TitanAgent_for_All_x86_64.exe"
repeat_files = []      # 记录重复文件名
for item in data:
    if sample_char in item['desc']:
        # print(item['filename'])
        repeat_files.append(item['filename'])

# print(repeat_files)
print(f"[*] Repeat info count: {len(repeat_files)} ")

# # 删除指定目录下的重复样本
#
# poc_file_path = r'/Volumes/MACOSX/aras/sample_analysis/sample_v2/poc_v1.1_session322_log_312/poc_v1/poc_v1'
#
# # 删除目录下删除的session
# def del_repeat_session(poc_file_path):
#     # # windows下的处理，linux下待测试
#     can_not_find_session = []
#     for del_file_name in repeat_files:
#         # print(del_file_name)
#         if os.path.exists(poc_file_path + '/' + del_file_name):
#             os.remove(poc_file_path + '/' + del_file_name)
#         else:
#             print("[DEBUG]", del_file_name)
#             can_not_find_session.append(del_file_name)
#
#
#     print(f"[*] can_not_find_session file: ", can_not_find_session)
#     print(len(can_not_find_session))
#     print(f"[*] Finish del repeat session file ...")
#
#     # 检查指定目录下的样本数量
#     for root, dirs, files in os.walk(poc_file_path):
#         # print(root) #当前目录路径
#         # print(dirs) #当前路径下所有子目录
#         print(files) #当前路径下所有非目录子文件
#         print("[*] Current files count: ", len(files))    # 原始885    处理完322
#
#
# # 根据现存session文件，重新处理原来的poc.json
# files = []
# new_poc_file_path = r'/Volumes/MACOSX/aras/sample_analysis/sample_v2/poc_v1.1_session322_log_312/poc_v1/poc_v1'
# for root, dirs, files in os.walk(poc_file_path):
#     print("current dir files: ", files)  # 当前路径下所有非目录子文件
#     print(type(files))  # list  去重后的session文件名列表
#
# # 读取样本原始日志信息
# with open('./poc_bk.json', 'r') as f:
#     bk_data = json.load(f)
#
# print("need files count: ", len(files))
# print("files: ", files)
# print("[TEST] poc_bk.json count: ", len(bk_data))
#
#
# need_info = []
#
# discard_info = []
#
# for item in bk_data:
#     if item['filename'] in files:
#         need_info.append(item)
#     else:
#         discard_info.append(item)
#
# print("[TEST] need_info count: ", len(need_info))
# print("[-] discard_info count: ", len(discard_info))
#
# with open('poc_v2.json', 'w') as f:
#     f.seek(0)
#     f.truncate()
#     json.dump(need_info, f, indent=4)
#
#
#
# with open('poc_v2.json', 'r') as f:
#     data = json.load(f)
#     print("[TEST] handle data count: ", len(data))
