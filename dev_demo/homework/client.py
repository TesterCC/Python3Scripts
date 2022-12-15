# coding=utf-8
"""
DATE:   2021/9/28
AUTHOR: TesterCC
"""

# P10 TCP Client

import socket

# target_host = "www.baidu.com"
# target_port = 80
# target_host = "0.0.0.0"  # cause WinError 10049
target_host = "127.0.0.1"  # can run in windows
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

# client.send(b"GET / HTTP/1.1\n\nHost: baidu.com\r\n\r\n")
# client.send(b"ababaabb \n\nHost: 0.0.0.0\r\n\r\n")
client.send(b"aabbccdd")
print("[+] send 1st data")


# # test 1 ok
# response = client.recv(12)
# response_str = response.decode("utf-8")
# print(f"response_str: {response_str}")  # ABCD11223344
#
# response2_header = response[:3]
# response2_header_str = response2_header.decode("utf-8")
# print(f"response2_header_str: {response2_header_str}")


resp_header = client.recv(4)
resp_header_str = resp_header.decode("utf-8")
print(resp_header_str)

if resp_header_str == "ABCD":
    resp_content = client.recv(8)
    resp_content_str = resp_content.decode("utf-8")
    print(f"resp_content_str: {resp_content_str}")
    client.send(b"RETN"+resp_content)
    print("[+] send 2ed data")


client.close()
