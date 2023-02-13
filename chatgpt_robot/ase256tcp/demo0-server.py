import socket
import os
import hashlib
import sys
from Crypto.Cipher import AES


# # 使用 pycryptodome 这个库来实现 AES-256 的加密

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(plaintext)


def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(ciphertext)


def get_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = ''
    while len(d) < key_length + iv_length:
        d_i = hashlib.sha256(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length + iv_length]


# AES-256 encryption key
password = "secretkey".encode()
salt = os.urandom(8)
key, iv = get_key_and_iv(password, salt, 32, 16)

# create socket for server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen(1)

# accept client connection
client, address = server.accept()

# receive encrypted data from client
ciphertext = client.recv(4096)

# decrypt data
plaintext = decrypt(ciphertext, key, iv)

# print decrypted data
print("Received: ", plaintext.decode())

# close the connection
client.close()
server.close()
