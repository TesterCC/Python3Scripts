# coding=utf-8

# TCP Client - block

import socket
import traceback

IP = '0.0.0.0'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ret = client.connect((IP, PORT))
    # print(f"conn ret: {ret}")  # none
    client.sendall(b"hello")
    print("[+] send request ...")

    response = client.recv(7)

    if response[:5] == b"world" and response[-2:] == b"\r\n":
        print(f"[-] receive response: {response}")

except ConnectionError:
    traceback.print_exc()

client.close()
