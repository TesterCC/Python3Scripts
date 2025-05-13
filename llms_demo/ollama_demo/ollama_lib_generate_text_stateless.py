"""
3. 生成文本 (Generate Text - Stateless)
这是最基本的文本生成，每次请求都是独立的。
"""

import ollama

model_name = 'valorvie/Foundation-Sec-8B-Chinese-Chat' # 确保这个模型已经通过 ollama pull 下载
prompt_text = "用简体中文解释下什么是CSRF攻击？"

try:
    print(f"正在使用模型 '{model_name}' 生成文本...")
    response = ollama.generate(
        model=model_name,
        prompt=prompt_text
    )
    print("\n模型回复:")
    print(response['response'])

    # 也可以流式接收回复
    print("\n流式回复:")
    stream = ollama.generate(
        model=model_name,
        prompt=prompt_text,
        stream=True
    )
    for chunk in stream:
        if 'response' in chunk:
            print(chunk['response'], end='', flush=True)
    print("\n--- 流式传输结束 ---")

except Exception as e:
    print(f"生成文本时发生错误: {e}")
    print(f"请确保模型 '{model_name}' 已经下载并且 Ollama 服务正在运行。")