import hashlib

from Crypto.Cipher import AES

iv = b'1234567898765432'


class Ofb:
    def __init__(self, key):  # constructor
        self.key = hashlib.sha3_256(key).digest()

    def encrypt(self, plainText):
        if isinstance(plainText, str):
            data_bytes = bytes(plainText, 'utf-8')  # convert it to utf 8 format
        else:
            data_bytes = plainText
        padded_bytes = self.pad(data_bytes)
        AES_object = AES.new(self.key, AES.MODE_OFB, iv)
        cipherText = AES_object.encrypt(padded_bytes)
        return cipherText

    @staticmethod
    def pad(text):
        return text + bytes((16 - len(text) % 16) * chr(16 - len(text) % 16), "utf-8")

    @staticmethod
    def unpad(text):
        return text[:-text[- 1]]

    def decrypt(self, cipherText):
        AES_object = AES.new(self.key, AES.MODE_OFB, iv)
        raw_bytes = AES_object.decrypt(cipherText)
        extracted_bytes = self.unpad(raw_bytes)
        return extracted_bytes
