import socket

from cbc import Cbc
from ofb import Ofb

clientsocket = socket.socket()
k1 = b'1234567812345678'
k2 = b'8765432187654321'
iv = b'1234567898765432'

host = "127.0.0.1"
port = 1234

try:
    clientsocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    response=clientsocket.recv(1028).decode("utf-8")
    print(response)
    clientsocket.send(str.encode("Send key"))
    key= clientsocket.recv(1028)
    key= Cbc(k1).decrypt(key)
    print(key)
    i=input("Name: ")
    if i=="A":
        clientsocket.send(str.encode(i))
        clientsocket.recv(1028).decode("utf-8")
        fisier = open("text.txt", "r").readlines()
        mode= input("Cbc/ Ofb: ")
        clientsocket.send(str.encode(mode))
        for line in fisier:
            if mode == "Cbc":
                clientsocket.send(Cbc(key).encrypt(bytes(line, "utf-8")))
            if mode == "Ofb":
                clientsocket.send(Ofb(key).encrypt(bytes(line, "utf-8")))
            response = clientsocket.recv(2048).decode("utf-8")
        clientsocket.send(str.encode("Done"))
        i=input()
    else:
        clientsocket.send(str.encode(i))
        clientsocket.recv(1028).decode("utf-8")
        clientsocket.send(str.encode("Mode"))
        mode=clientsocket.recv(1028).decode("utf-8")
        print(mode)
        while True:
            message=clientsocket.recv(2048).decode("utf-8")
            if not message:
                break
            if message == "Sending":
                clientsocket.send(str.encode("OK"))
                while True:
                    _message = clientsocket.recv(2048).decode("utf-8")
                    if not _message and (isinstance(_message, str) and str.decode(_message)=="Final"):
                        break
                    if mode == "Cbc":
                        print(Cbc(key).decrypt(_message).decode("utf-8"))
                    if mode == "Ofb":
                        print(Ofb(key).decrypt(_message).decode("utf-8"))
                    clientsocket.send(str.encode("Yems finally"))


        i=input()

clientsocket.close()
