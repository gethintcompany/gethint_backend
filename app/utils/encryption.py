from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag
import os
import json
import secrets
from typing import Union


class AESEncryptor:
    def __init__(self, key: Union[bytes, str], salt: bytes = None):
        if isinstance(key, str):
            key = key.encode('utf-8')
        self.key = self._derive_key(key, salt or os.urandom(16))

    def _derive_key(self, password: bytes, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000,
            backend=default_backend()
        )
        return kdf.derive(password)

    def _serialize(self, data) -> bytes:
        if isinstance(data, (dict, list)):
            return json.dumps(data).encode('utf-8')
        if isinstance(data, (int, float)):
            return str(data).encode('utf-8')
        return bytes(data) if isinstance(data, (bytes, bytearray)) else data.encode('utf-8')

    def encrypt(self, data) -> bytes:
        nonce = secrets.token_bytes(16)
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        processed_data = self._serialize(data)
        encrypted = encryptor.update(processed_data) + encryptor.finalize()
        return nonce + encryptor.tag + encrypted

    def decrypt(self, encrypted_data: bytes):
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]

        cipher = Cipher(algorithms.AES(self.key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()

        try:
            decrypted = decryptor.update(ciphertext) + decryptor.finalize()
            try:
                return json.loads(decrypted.decode('utf-8'))
            except json.JSONDecodeError:
                return decrypted.decode('utf-8')
        except InvalidTag:
            raise ValueError("Invalid decryption key or corrupted data")

    @staticmethod
    def generate_key() -> bytes:
        return secrets.token_bytes(32)


#
# Generate random key
key = AESEncryptor.generate_key()

# Initialize with key or password
encryptor = AESEncryptor(key)

# Encrypt any data type
encrypted = encryptor.encrypt({
    "secret": "data",
    "value": 42,
    "array": [1, 2, 3]
})

# Decrypt
try:
    decrypted = encryptor.decrypt(encrypted)
    p1 = encryptor.
    print(encrypted)
    print(decrypted)

except ValueError as e:
    print(f"Decryption failed: {e}")