# coding:utf-8

import re
files = ["request_set_parent_xxxxxxxxsda.json", "sub_tree.json", "GeneralNode"]

pattern = r"^request_set_parent(.*).json$"


for file in files:

    match_obj = re.match(pattern, file)
    if match_obj:
        print(f"[D] {match_obj.group(0)}")  # need filename
        print(f"[D] {match_obj.group(1)}")