import requests

from pprint import pprint

# get models basic info

response = requests.get("http://localhost:11434/api/tags")
# print(response.json())
# pprint(response.json())   # for pycharm terminal output

basic_data = response.json()

pprint(basic_data)  # for debug

print("=" * 66)

models_info = basic_data.get("models")

for model_info in models_info:

    response_info = dict()

    for k,v in model_info.items():
        # print(f"k: {k}, v: {v}")
        response_info[k] = v

    pprint(response_info)

