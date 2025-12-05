# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2025/12/5

"""
ref:

https://github.com/python-lsp/python-lsp-server

pip install python-lsp-server

python -m pylsp

minimum lsp test client
"""

import json, subprocess

proc = subprocess.Popen(["python", "-m", "pylsp", "-v"],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

msg = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {}
}

content = json.dumps(msg)
proc.stdin.write(f"Content-Length: {len(content)}\r\n\r\n{content}".encode())
proc.stdin.flush()

print(proc.stdout.readline())  # 能收到打印响应即成功