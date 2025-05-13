import requests

# 3. 拉取模型（例如 llama3）
data = {
    "name": "llama3"
}
response = requests.post("http://localhost:11434/api/pull", json=data)
print(response.json())