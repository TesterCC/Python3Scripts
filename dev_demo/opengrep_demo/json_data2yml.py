# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/6
import json
import os
import yaml

class SemgrepRuleReader:
    def __init__(self):
        self.config = None

    def yaml_str_presenter(self, dumper, data):
        # 使用 yaml.representer 来强制某些字段使用多行字面量样式
        # 强制使用 block literal style（|）表示多行字符串
        if "\n" in data:  # 检查是否包含换行符
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)


    def generate_task_yaml(self, rules_data:list, yaml_path:str):
        """

        :param rules_data:
        :param yaml_path:
        :return:
        """
        yaml.add_representer(str, self.yaml_str_presenter)
        # 如果你使用的是 SafeDumper
        yaml.SafeDumper.add_representer(str, self.yaml_str_presenter)

        # 组装新规则
        output_yaml_data = {"rules": rules_data}

        # 写入 YAML 文件
        output_dir = os.path.dirname(yaml_path)

        os.makedirs(output_dir, exist_ok=True)
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(output_yaml_data, f, sort_keys=False, allow_unicode=True)



if __name__ == '__main__':

    # json_data_file = "data/260206-handle-data.json"
    # json_data_file = "data/260206-handle-data-small.json"
    # json_data_file = "data/260206-handle-data-small-cleaned.json"
    # json_data_file = "data/260206-handle-data-cleaned.json"   # real need
    json_data_file = "data/260206-handle-data.json"

    with open(json_data_file, "r", encoding="utf-8") as f:
        rule_data_list = json.load(f)


    output_rules_data = []

    for row in rule_data_list:
        rule_content_json = row.get("rule_content")
        rule_data = json.loads(rule_content_json)

        selected_rule = rule_data.get("rules")[0]
        output_rules_data.append(selected_rule)

    srr = SemgrepRuleReader()
    # srr.generate_task_yaml(output_rules_data, yaml_path="task-rule/260206-handle-data-small-cleaned.yaml")
    # srr.generate_task_yaml(output_rules_data, yaml_path="task-rule/260206-handle-data-cleaned.yaml")   # real need
    srr.generate_task_yaml(output_rules_data, yaml_path="task-rule/260206-handle-data.yaml")