# NOTE: For web interface, use server.py. This file is a standalone CLI tool.

import os
import base64
import qrcode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def generate_aes_key(length=32):
    return os.urandom(length)

def encrypt_data(data, key):
    # Pad data to block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    # Generate random IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ct  # Prepend IV for decryption

def main():
    text = input("Enter the text to encrypt and encode in QR code: ")
    key = generate_aes_key()
    encrypted = encrypt_data(text, key)
    # Encode key and encrypted data in base64 for QR
    b64_key = base64.urlsafe_b64encode(key).decode()
    b64_encrypted = base64.urlsafe_b64encode(encrypted).decode()
    qr_payload = f"key:{b64_key}\ndata:{b64_encrypted}"
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_payload)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("encrypted_qr.png")
    print("QR code with encrypted data and one-time AES key saved as 'encrypted_qr.png'.")

if __name__ == "__main__":
    main()
