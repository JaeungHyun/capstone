# *-* coding: utf-8*-*

import temp
from socket import *
import threading

def handler(clientsock, addr):
    data = clientsock.recv(BUFSIZ)
    if not data:
        exit()
    clientsock.send(temp.byteTemp)

    clientsock.close()


if __name__ == "__main__":
    HOST = ''
    PORT = 12222
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)

    while 1:
        print("Waiting for connection...")
        clientsock, addr = serversock.accept()
        print("connected from", addr)
        t = threading.Thread(handler(clientsock, addr))

