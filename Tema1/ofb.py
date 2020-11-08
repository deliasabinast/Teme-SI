from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plainText= "dsahgdijsadljfn1385sJHDAF315fdf"
key = pad(b"keythatineed", AES.block_size)
iv = pad(b"initvector",AES.block_size)

def __init__(self, key): #constructor
    self.key = key

def _encrypt(plainText):

    padded_bytes=pad(data_bytes, AES.block_size)
    AES_object=AES.new(key, AES.MODE_OFB, iv)
    cipherText = AES_object.encrypt(padded_bytes)
    return cipherText

cipherText = _encrypt(plainText)
print(cipherText)

def _decrypt(cipherText):
    AES_object = AES.new(key, AES.MODE_OFB, iv)
    raw_bytes= AES_object.decrypt(cipherText)
    extracted_bytes=unpad(raw_bytes, AES.block_size)
    return extracted_bytes

plainText=_decrypt(cipherText)
print(plainText)