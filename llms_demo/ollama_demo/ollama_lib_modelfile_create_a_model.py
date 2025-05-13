"""
5. 创建自定义模型 (Create a Model from Modelfile)
您可以使用 Modelfile 定义自己的模型变体。
"""

import ollama
import os

# modelfile_content = """
# FROM llama3
# SYSTEM "你是一个乐于助人的AI助手，你的名字叫MrRobot，总是用简体中文回答问题。"
# PARAMETER temperature 0.5
# """

model_file_path="ollama_custom_model_file.txt"

custom_model_name = "custom-dpr1"

try:
    # 从文件中读取 Modelfile 的内容
    with open(model_file_path, 'r', encoding='utf-8') as f:
        model_file_content_str = f.read()

    print(f"成功从 '{model_file_path}' 读取 Modelfile 内容。")
    print("--- Modelfile 内容预览 ---")
    print(model_file_content_str[:300] + "..." if len(model_file_content_str) > 300 else model_file_content_str) # if too long, display part of it as preview
    print("--------------------------\n")

    print(f"正在创建自定义模型: {custom_model_name}...")
    # stream=True 会逐步打印创建进度
    for progress in ollama.create(model=custom_model_name, modelfile=model_file_content_str, stream=True):
        if 'status' in progress:
            print(f"状态: {progress['status']}")
        elif 'error' in progress:
            print(f"错误: {progress['error']}")
            break
    print(f"自定义模型 {custom_model_name} 创建完成 (或已存在)。")

    # 测试新创建的模型
    print(f"\n测试自定义模型 '{custom_model_name}':")
    response = ollama.generate(
        model=custom_model_name,
        prompt="你好，你叫什么名字？"
    )
    print("模型回复:", response['response'])

except Exception as e:
    print(f"创建自定义模型时发生错误: {e}")