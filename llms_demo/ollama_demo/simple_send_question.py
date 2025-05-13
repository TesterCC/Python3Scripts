import requests

# 4. 向模型发送 Prompt（非流式）
data = {
    "model": "valorvie/Foundation-Sec-8B-Chinese-Chat:latest",
    "prompt": "如何学习网络安全？",
    "stream": False,
}

response = requests.post("http://localhost:11434/api/generate", json=data)
print(response.json())  # standard response
print("-" * 66)
print(response.json()["response"])
