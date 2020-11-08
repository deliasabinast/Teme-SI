from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plainText= "dsahgdijsadljfn1385sJHDAF315fdf"
key = pad(b"keythatineed", AES.block_size) #converts key
iv = pad(b"initvector",AES.block_size) #init vector

def __init__(self, key): #constructor
    self.key = key

def _encrypt(plainText):
    data_bytes=bytes(plainText, 'utf-8') #convert it to utf 8 format
    padded_bytes=pad(data_bytes, AES.block_size) #padding the data bytes
    AES_object=AES.new(key, AES.MODE_CBC, iv) #we create an AES object
    cipherText = AES_object.encrypt(padded_bytes) #we use the object tp call the encypt function on the added bytes
    return cipherText

cipherText = _encrypt(plainText)
print(cipherText)

def _decrypt(cipherText):
    AES_object = AES.new(key, AES.MODE_CBC, iv) #create the object
    raw_bytes= AES_object.decrypt(cipherText) #we use the object to call the decrypt function
    extracted_bytes=unpad(raw_bytes, AES.block_size) #we use the unpad function on the raw bytes with AES block size
    return extracted_bytes #

plainText=_decrypt(cipherText)
print(plainText)