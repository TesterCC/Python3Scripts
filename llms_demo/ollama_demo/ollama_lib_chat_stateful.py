"""
4. 聊天 (Chat - Stateful)
聊天 API 允许进行多轮对话，模型会记住之前的上下文。
"""

import ollama

model_name = 'valorvie/Foundation-Sec-8B-Chinese-Chat'  # 确保这个模型已经通过 ollama pull 下载
messages_history = []  # record chat history

print(f"开始与模型 '{model_name}' 聊天。输入 '退出' 来结束对话。")

while True:
    print("=" * 77)
    user_input = input("当前使用者: ")
    if user_input.lower() == '退出':
        print("对话结束。")
        break

    messages_history.append({'role': 'user', 'content': user_input})

    try:
        print("模型思考中...")
        # 流式接收回复
        full_response_content = ""
        # 讲聊天历史记录作为上下文信息传入，以便支持后续对话
        stream = ollama.chat(
            model=model_name,
            messages=messages_history,
            stream=True,
        )
        print("模型: ", end="")
        for chunk in stream:
            if 'message' in chunk and 'content' in chunk['message']:
                content_piece = chunk['message']['content']
                print(content_piece, end='', flush=True)
                full_response_content += content_piece
            elif 'error' in chunk:
                print(f"\n错误: {chunk['error']}")
                break
        print()  # 换行

        if full_response_content:
            messages_history.append({'role': 'assistant', 'content': full_response_content})

    except Exception as e:
        print(f"\n与 Ollama API 通信时发生错误: {e}")
        # 发生错误时，可以选择是否从历史记录中移除最后一条用户消息
        if messages_history and messages_history[-1]['role'] == 'user':
            messages_history.pop()
        break
