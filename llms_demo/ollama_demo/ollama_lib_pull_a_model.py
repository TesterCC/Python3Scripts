# ref: https://github.com/ollama/ollama-python
# Ollama 官方提供了一个 Python 库，可以更方便地与 API 进行交互。
# pip install ollama

import ollama

# 2. 拉取 (下载) 模型 (Pull a Model)
# model_name = 'llama3' # 您想要拉取的模型名称，例如 llama3, mistral, qwen 等
model_name = 'deepseek-r1:1.5b' # 您想要拉取的模型名称，例如 llama3, mistral, qwen 等

try:
    print(f"正在拉取模型: {model_name}...")
    # stream=True  # 会逐步打印下载进度
    for progress in ollama.pull(model_name, stream=True):
        if 'status' in progress:
            print(f"状态: {progress['status']}", end='')
            if 'digest' in progress:
                print(f" (Digest: {progress['digest']})", end='')
            if 'total' in progress and 'completed' in progress and progress['total'] > 0:
                percentage = (progress['completed'] / progress['total']) * 100
                print(f" - {percentage:.2f}% 完成", end='')
            print() # 换行
        elif 'error' in progress:
            print(f"错误: {progress['error']}")
            break
    print(f"模型 {model_name} 拉取完成 (或已存在)。")
except Exception as e:
    print(f"拉取模型时发生错误: {e}")