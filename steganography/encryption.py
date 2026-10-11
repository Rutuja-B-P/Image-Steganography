# steganography/encryption.py

from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key_from_password(password):
    """
    Derives a 32-byte key from the given password using SHA-256.
    """
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def aes_encrypt(message: str, password: str) -> str:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def aes_decrypt(token: str, password: str) -> str:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()
