from flask import Flask, request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import os

"""
an example of AES-256 encrypted http c2 server in Python3 with Flask framework

In this example, the AES-256 encryption is implemented using the cryptography library. 
The key used for encryption and decryption is b'key_used_for_AES_256'. 
The Flask framework is used to implement the HTTP server and handle the incoming encrypted data at the endpoint /c2. 
The encrypted data is then decrypted using the decrypt function and processed as needed.
"""

app = Flask(__name__)


def encrypt(message, key):
    backend = default_backend()
    iv = os.urandom(16)
    padder = padding.PKCS7(256).padder()
    padded_data = padder.update(message) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ct


def decrypt(ciphertext, key):
    backend = default_backend()
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(256).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data


@app.route("/")
def home():
    return "C2 Server Home"


@app.route("/c2", methods=["POST"])
def c2():
    encrypted_data = request.data
    decrypted_data = decrypt(encrypted_data, b'key_used_for_AES_256')
    # do your processing here
    return "Data received successfully"


if __name__ == "__main__":
    app.run(debug=True)
