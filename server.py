# *-* coding: utf-8*-*

import temp
from socket import *


print(temp.byteTemp)

while 1:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 12222))
    s.listen(1)

    print('Connect waiting......')

    conn, addr = s.accept()
    print('Connected by', addr)

    while 1:
        data = conn.recv(1024)
        if not data:
            break

        print('received data :', data)
        conn.send(temp.byteTemp)

conn.close()
s.close()