import socket
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 20230231 这个应该就可以的
# AES-256加密方法
def encrypt(message, key):
    backend = default_backend()
    message = message.encode('utf-8')
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(message) + encryptor.finalize()
    return base64.b64encode(ct).decode('utf-8')


# AES-256解密方法
def decrypt(encrypted_message, key):
    backend = default_backend()
    encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    message = decryptor.update(encrypted_message) + decryptor.finalize()
    return message.decode('utf-8')


# TCP服务端
def start_server():
    host = '0.0.0.0'
    port = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f'Server started on {host}:{port}')

    client_socket, client_address = server.accept()
    print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

    key = os.urandom(32)
    while True:
        received_data = client_socket.recv(1024).decode('utf-8')
        if received_data:
            decrypted_message = decrypt(received_data, key)
            print(f'Received message: {decrypted_message}')


# TCP客户端
def start_client():
    host = '0.0.0.0'
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print(f'Client connected to {host}:{port}')

    key = os.urandom(32)
    while True:
        message = input('Enter a message: ')
        encrypted_message = encrypt(message, key)
        client.sendall(encrypted_message.encode('utf-8'))


# 判断启动客户端还是服务端
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        start_server()
