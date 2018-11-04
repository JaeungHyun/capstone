# *-* coding: utf-8*-*

import temp
import Relay
import waterlevel
from socket import *
import threading

def handler(clientsock, addr):
    data = threading.local()
    data.x = clientsock.recv(BUFSIZ)

    if not data.x:
        exit()
    
    strresponse = temp.stringTemp + waterlevel.waterleveling
    response = strresponse.encode()
    clientsock.send(response)
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
        print("received data:", clientsock.recv(BUFSIZ).decode())
        t = threading.Thread(handler(clientsock, addr))
        t.start()

