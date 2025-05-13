import requests

def stream_prompt():
    # 5.发送 Prompt（流式输出）

    data = {
        "model": "valorvie/Foundation-Sec-8B-Chinese-Chat:latest",
        "prompt": "详细解释什么是云原生安全？",
        "stream": True,
        # "system": "你是一位经验丰富的安全工程师，回答时请使用简体中文。"  # 这个问题正好是默认用繁体输出，加上system限制后，就是简体输出了。
    }

    with requests.post("http://localhost:11434/api/generate", json=data, stream=True) as response:
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))    # 逐字输出

stream_prompt()