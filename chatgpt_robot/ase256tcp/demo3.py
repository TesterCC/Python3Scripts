import socket
import sys
import base64
import hashlib
import os
from Crypto.Cipher import AES

# 使用 pycryptodome 这个库来实现 AES-256 的加密

# # Padding for the input message
# def pad(s):
#     return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


# Encryption using AES-256
def encrypt(message, key, key_size=256):
    # message = pad(message)
    message = message + b"\0" * (AES.block_size - len(message) % AES.block_size)
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(message))


# Decryption using AES-256
def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


# Key for encryption and decryption
key = hashlib.sha256(b"secret_key").digest()


# TCP server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)
    print("[INFO] Server is listening...")
    client_socket, client_address = server_socket.accept()
    print("[INFO] Client connected:", client_address)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        decrypted_data = decrypt(data, key)
        print("[INFO] Received message:", decrypted_data)
        client_socket.send(encrypt(decrypted_data, key))
    client_socket.close()
    server_socket.close()


# TCP client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    message = b"Hello, server!"
    encrypted_message = encrypt(message, key)
    client_socket.send(encrypted_message)
    data = client_socket.recv(1024)
    decrypted_data = decrypt(data, key)
    print("[INFO] Received message:", decrypted_data)
    client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        start_server()
    else:
        start_client()
