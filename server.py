# *-* coding: utf-8*-*

import temp
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
print('Connect wating......')

conn, addr = s.accept()
print('Connected by', addr)

while 1:
    data = conn.recv(1024)
    if not data:
        break

    print('received data :', data)
    conn.send(temp.temperature)

conn.close()
s.close()
