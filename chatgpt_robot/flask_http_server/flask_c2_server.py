from flask import Flask, request
from Cryptodome.Cipher import AES

app = Flask(__name__)

# 用python3 flask实现http c2服务器，且支持AES-256加密通信
def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return (cipher.nonce, tag, ciphertext)


def decrypt(key, nonce, tag, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext


@app.route("/test", methods=["POST"])
def handle_request():
    key = b'This is a key123'   # attention: key的长度不能变
    data = request.data
    nonce, tag, ciphertext = encrypt(key, data)
    plaintext = decrypt(key, nonce, tag, ciphertext)
    print(f"plaintext: {plaintext}")
    return plaintext


if __name__ == "__main__":
    app.run()
