import base64
import hashlib

from Crypto.Cipher import AES

iv = b'1234567898765432'


class Cbc:
    def __init__(self, key):  # constructor
        self.key = hashlib.sha3_256(key).digest()

    def encrypt(self, plainText):
        if isinstance(plainText, str):
            data_bytes = bytes(plainText, 'utf-8')  # convert it to utf 8 format
        else:
            data_bytes = plainText
        padded_bytes = self.pad(data_bytes)  # padding the data bytes
        AES_object = AES.new(self.key, AES.MODE_CBC, iv)  # we create an AES object
        cipherText = AES_object.encrypt(
            padded_bytes)  # we use the object tp call the encypt function on the added bytes
        return base64.b64encode(cipherText)

    @staticmethod
    def pad(text):
        return text + bytes((16 - len(text) % 16) * chr(16 - len(text) % 16), "utf-8")

    @staticmethod
    def unpad(text):
        return text[:-text[- 1]]

    def decrypt(self, cipherText):
        cipherText = base64.b64decode(cipherText)
        AES_object = AES.new(self.key, AES.MODE_CBC, iv)  # create the object
        raw_bytes = AES_object.decrypt(cipherText)  # we use the object to call the decrypt function
        extracted_bytes = self.unpad(
            raw_bytes)  # we use the unpad function on the raw bytes with AES block size
        return extracted_bytes
