import os

from cbc import Cbc
from ofb import Ofb

key = os.urandom(16)
k1 = b'1234567812345678'
k2 = b'8765432187654321'
cbc = Cbc(k1).encrypt(b'text')

print(cbc)
print(Cbc(k1).decrypt(cbc))

ofb = Ofb(k2).encrypt(b'text')

print(ofb)
print(Ofb(k2).decrypt(ofb))
