# ref: https://github.com/ollama/ollama-python
# Ollama 官方提供了一个 Python 库，可以更方便地与 API 进行交互。
# pip install ollama

from pprint import pprint

import ollama

# 1. 列出本地可用的模型 (List Local Models)

try:
    ret = ollama.list()
    response = ret.get("models")
    print("Local models can use:\n", response)  # debug
    # print(dir(models_info))
    # for model in response:
    #     print(model)
    # print(type(response))   # debug
    # print(dir(response))  # debug

    for model in response:
        print(f"- name: {model['model']}")
        print(f"  size: {model['size'] / (1024**3):.2f} GB") # 将字节转换为GB
        print(f"  modified time: {model['modified_at']}")
        print("-" * 20)
    else:
        print("Didn't find models, please use 'ollama pull <model_name>' to download models。")
except Exception as e:
    print(f"Ollama communication error: {e}")