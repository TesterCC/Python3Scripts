# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2026/2/6


import json
from copy import deepcopy


TARGET_KEY = "semgrep-internal-metavariable-name"

def clean(obj):
    """
    递归删除 TARGET_KEY，
    并自动裁剪空 dict / 空 list
    """
    if isinstance(obj, dict):
        new_dict = {}

        for k, v in obj.items():
            if k == TARGET_KEY:
                continue

            cleaned_v = clean(v)

            # 裁剪空结构
            if cleaned_v in ({}, []):
                continue

            new_dict[k] = cleaned_v

        return new_dict

    elif isinstance(obj, list):
        new_list = []

        for item in obj:
            cleaned_item = clean(item)

            if cleaned_item in ({}, []):
                continue

            new_list.append(cleaned_item)

        return new_list

    else:
        return obj

def remove_target_key(obj):
    """
    递归删除所有 semgrep-internal-metavariable-name 字段
    """
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            if k == TARGET_KEY:
                # 直接跳过该字段
                continue
            new_dict[k] = remove_target_key(v)
        return new_dict

    elif isinstance(obj, list):
        return [remove_target_key(item) for item in obj]

    else:
        return obj


def process_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        if "rule_content" not in item:
            continue

        # rule_content 是 JSON 字符串，需要再 parse 一次
        rule_obj = json.loads(item["rule_content"])

        # 清洗
        # rule_obj_cleaned = remove_target_key(rule_obj)
        rule_obj_cleaned = clean(rule_obj)

        # 再序列化回字符串（保持紧凑或可读都可以）
        item["rule_content"] = json.dumps(
            rule_obj_cleaned,
            ensure_ascii=False
        )

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # # MVP demo
    # process_file(
    #     input_path="data/260206-handle-data-small.json",
    #     output_path="data/260206-handle-data-small-cleaned.json"
    # )

    process_file(
        input_path="data/260206-handle-data.json",
        output_path="data/260206-handle-data-cleaned.json"
    )


