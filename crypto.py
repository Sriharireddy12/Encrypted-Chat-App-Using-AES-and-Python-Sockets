from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b'1234567890abcdef'

def encrypt_message(message):
    iv = get_random_bytes(16)

    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)

    encrypted = cipher.encrypt(message.encode())

    return base64.b64encode(iv + encrypted).decode()

def decrypt_message(data):
    raw = base64.b64decode(data)

    iv = raw[:16]
    encrypted = raw[16:]

    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)

    return cipher.decrypt(encrypted).decode()
    
