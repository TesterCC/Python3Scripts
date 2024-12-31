# coding:utf-8
import os
import pandas as pd

# for output apt_parse yara_rules signature
def generate_excel(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.yar')]
    data = []
    for file_name in file_list:
        description = file_name.replace(".yar", "") + "家族检测规则"  # 这里您可以根据实际情况获取或生成描述
        abs_path = f"/opt/tools/apt_parser/core/yara_rules/signature/{file_name}"
        data.append([file_name, description, abs_path])
    df = pd.DataFrame(data, columns=['文件名', '描述', '文件路径'])
    df.to_excel('inner_rule.xlsx', index=False)

folder_path = r'E:\payload_team\ws_code\apt_parser\core\yara_rules\signature'
generate_excel(folder_path)