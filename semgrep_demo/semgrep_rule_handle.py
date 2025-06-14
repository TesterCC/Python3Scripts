# -*- coding:utf-8 -*-

# online install: pip install pyyaml
# offline install: pip install --no-index --find-links=./pip_pyyaml/ pyyaml
import yaml

# todo 需要实现一个类来专门对规则进行修改

def parse_yaml_file(file_path):
    """解析 YAML 文件并返回其内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # 加载 YAML 文件内容
            yaml_content = yaml.safe_load(file)
            return yaml_content
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"YAML 解析错误：{e}")
        return None


def print_yaml_data(data, indent=0):
    """递归打印 YAML 数据"""
    if isinstance(data, dict):
        for key, value in data.items():
            print("  " * indent + f"{key}:")
            print_yaml_data(value, indent + 1)
    elif isinstance(data, list):
        for item in data:
            print("  " * indent + "-")
            print_yaml_data(item, indent + 1)
    else:
        # 基本类型（字符串、数字等）
        print("  " * indent + f"{str(data)}")


def analysis_yaml_dict(yaml_data):
    print(f"[D] parse data type: {type(yaml_data)}")
    print(f"[D] parse data content: \n{yaml_data}")

    rules_data = yaml_data.get("rules")

    for rule_item in rules_data:
        print(f"[D] parse item content: \n{rule_item}")

        for key, value in rule_item.items():
            print(key, " ---> ", value)


def add_custom_metadata(yaml_data, custom_key, custom_value):
    """
    向 YAML 数据中的 metadata 字段添加自定义条目

    参数:
    yaml_data (dict): 解析后的 YAML 数据
    custom_key (str): 要添加的自定义元数据键
    custom_value (str): 要添加的自定义元数据值

    返回:
    dict: 更新后的 YAML 数据
    """
    # 确保 YAML 数据中有 rules 字段且为列表
    if 'rules' not in yaml_data or not isinstance(yaml_data['rules'], list):
        print("错误：YAML 数据中没有找到 'rules' 列表")
        return yaml_data

    # 遍历每个规则
    for rule in yaml_data['rules']:
        # 确保规则中有 metadata 字段
        if 'metadata' not in rule:
            # rule['metadata'] = {}
            pass
        else:
            if 'references' in rule['metadata'].keys():
                print(f"[D] references: {rule['metadata']["references"]}")
                # references: ['https://cwe.mitre.org/data/definitions/14.html', 'https://owasp.org/Top10/A02_2021-Cryptographic_Failures/']
                rule['metadata']["references"].append("https://xxx.example.com")
            # 添加自定义元数据条目
            rule['metadata'][custom_key] = custom_value

    return yaml_data


def save_rules(file_path, rules) -> bool:
    """保存规则到YAML文件"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(rules, file, default_flow_style=False, allow_unicode=True)
        return True
    except Exception as e:
        print(f"保存规则文件出错: {e}")
        return False

if __name__ == "__main__":
    # 指定 YAML 文件路径
    yaml_file_path = 'update/origin/insecure-use-memset.yaml'

    # 解析 YAML 文件
    parsed_data = parse_yaml_file(yaml_file_path)

    analysis_yaml_dict(parsed_data)
    print("==" * 33)

    new_data = add_custom_metadata(parsed_data,"gbt349xx", "1.1.1")
    print("[D] new data: ", new_data)

    save_file_path = "update/new/insecure-use-memset0.yaml"

    save_rules(save_file_path, new_data)

    # if parsed_data:
    #     # 打印解析后的数据
    #     print_yaml_data(parsed_data)
