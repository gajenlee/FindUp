import os

# ENCRPTION
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class Secure(object):

    # CREATE NEW KEY FOR 1000000 TIMES
    def __init__(self):
        salt = os.urandom(16)
        __password = b'12345_t_200'

        generatorKey = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000000,
            backend=default_backend()
        )
        self.__key = base64.urlsafe_b64encode(generatorKey.derive(__password))

    # ENCRYPT DATA
    def encrypt(self, data):
        data = data.encode('utf-8')
        self.fran = Fernet(self.__key)
        encrypt = self.fran.encrypt(data)
        return encrypt.decode('utf-8'), self.__key.decode('utf-8')

    # DECRYPT DATA
    def decrypt(self, encrypted, key):
        encrypted = encrypted.encode('utf-8')
        __key = key.encode('utf-8')

        self.fran = Fernet(__key)
        decrypted = self.fran.decrypt(encrypted)
        return decrypted.decode('utf-8')
