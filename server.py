import socket
from _thread import *
import threading
from multiprocessing import Process, Pipe

import temp
import waterlevel
import control_relay_water

print_lock = threading.Lock()


# thread function
def threaded(c):
    # data received from client
    data = c.recv(1024)
    if not data:
        print('Bye')
        # lock released on exit
        print_lock.release()

    decoded_data = data.decode()
    data_list = decoded_data.split(',')
    p_temp.send(data_list[0])
    p_cycle.send(data_list[1])
    t_value = temp.checktemp()   # e.g.) temp\nhumidity\n
    w_value = waterlevel.waterleveling()  # e.g.) temp\nhumidity\n
    print(t_value, w_value)
    data = t_value + w_value    # e.g.) temp\nhumidity\nwaterlevel\n
    msg = bytearray(data, 'utf-8')

    c.send(msg)

    # connection closed
    c.close()


def Main():

    host = ""

    # reverse a port on your computer
    port = 12222
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode 
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit 
    while True:
        # establish connection with client
        client, addr = s.accept()

        # lock acquired by client 
        print_lock.acquire()
        print('Connected to :', addr)

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (client,))
    s.close()


if __name__ == '__main__':
    p_temp, p_cycle = Pipe()
    p_temp.send(0)
    p_cycle.send(1)
    process_temp = Process(target=temp.Main(), args=(p_temp,))
    process_temp.start()
    process_water_relay = Process(target=control_relay_water.Main(), args=(p_cycle,))
    process_water_relay.start()
    Main()
