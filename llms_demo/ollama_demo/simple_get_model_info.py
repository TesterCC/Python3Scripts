from pprint import pprint

import requests
# 2. 获取本地模型列表
response = requests.get("http://localhost:11434/api/tags")
pprint(response.json())