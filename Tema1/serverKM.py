import os
import socket
from _thread import *
from cbc import Cbc
from ofb import Ofb

serversocket = socket.socket()

messages=[]


host = "127.0.0.1"
port = 1234
ThreadCount = 0
key = os.urandom(16)
k1 = b'1234567812345678'
k2 = b'8765432187654321'
iv = b'1234567898765432'
mode= None
done=False

key=Cbc(k1).encrypt(key)
try:
    serversocket.bind((host, port))
except socket.error as e:
    print(str(e))
print("waiting for connection")
serversocket.listen(5)


def client_thread(connection):
    global mode
    global done
    connection.send(str.encode("The server started working!"))
    while True:
        data = connection.recv(2048)
        if not data:
            break
        connection.send(key)
        if data.decode("utf-8") == "Send key":
            connection.send(key)
        data = connection.recv(2048).decode("utf-8") #bytes to string
        if data=="A":
            connection.send(str.encode("Hello A!"))
            mode= connection.recv(2048).decode("utf-8")
            message="yems"
            while True:
                if message == b"Done":
                    done=True
                    break
                message=connection.recv(2048)
                if not message:
                    break
                if not message== b"Done":
                    messages.append(message)
                    print(messages)
                    connection.send("Say something pls")
        else:
            connection.send(str.encode("Hello B!"))
            while True:
                if mode is not None:
                    break

            connection.recv(2048)
            connection.send(str.encode(mode))
            while True:
                if done:
                    break
            connection.send(str.encode("Sending"))
            connection.recv(2048)
            for message in messages:
                connection.send(message)
                connection.recv(2048)
            connection.send(str.encode("Final"))
    connection.close()


while True:
    client, address = serversocket.accept()
    print("Connected to : " + address[0] + str(address[1]))
    start_new_thread(client_thread, (client,))
    ThreadCount += 1
    print("ThreadNumber " + str(ThreadCount))

serversocket.close()
