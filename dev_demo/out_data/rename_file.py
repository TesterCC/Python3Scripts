import csv
import os

rename_dict = {}

with open('./data/rename.csv', encoding="utf-8") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        name, cve = row

        rename_dict.update({cve: name})

print(len(rename_dict))
print(rename_dict)

# start rename
# 文件夹完整路径
dir_path = r"D:\company\payload_platform\poc_exp"

# 循环遍历文件夹中所有文件，获取文件名及编号
for n, name in enumerate(os.listdir(dir_path)):
    print(f"{n},{name}")

    # 原文件的路径及名称
    src = dir_path + "/" + name
    name_cve = name.split(".")[0]
    new_name = rename_dict[name_cve]
    # 重命名后文件路径及名称
    dst = dir_path + "/" + new_name + ".zip"

    print(f"{src} --> {dst}")

    # 重命名文件
    os.rename(src, dst)
