# middleware.py
from cryptography.fernet import Fernet

# Replace this with a securely generated key
SECRET_KEY = b'HS27hO2EuV2mwmSyQRfc1HeA8QrUmVoeikaxLjIkitI='
cipher = Fernet(SECRET_KEY)

class EncryptionMiddleware:
    @staticmethod
    def encrypt(message: str) -> str:
        return cipher.encrypt(message.encode()).decode()

    @staticmethod
    def decrypt(encrypted_message: str) -> str:
        return cipher.decrypt(encrypted_message.encode()).decode()
