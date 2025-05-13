import requests

# 6.自定义 System Prompt 或参数（如温度、top_p）
data = {
    "model": "valorvie/Foundation-Sec-8B-Chinese-Chat:latest",
    "prompt": "如何学习网络安全？",
    "stream": False,
    "options": {
        "temperature": 0.7,
        "top_p": 0.9,
        "num_predict": 256
    },
    "system": "你是一位经验丰富的安全工程师，回答时请使用简体中文。"
}

response = requests.post("http://localhost:11434/api/generate", json=data)
print(response.json())   # standard response
print(response.json()["response"])