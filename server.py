import socket
from _thread import *
import threading
from multiprocessing import Process, Queue

import RPi.GPIO as GPIO

import temp
import waterlevel
import control_relay_water

print_lock = threading.Lock()


# thread function
def threaded(c):
    # data received from client
    data = c.recv(1024)
    if not data:
        print('Data is not received')

    decoded_data = data.decode()
    print('decoded data is', decoded_data)
    temperature, cycle = decoded_data.split(',')
    p_temp.put(float(temperature))
    p_cycle.put(int(cycle))
    t_value = temp.checktemp()            # e.g.) temp\nhumidity\n
    w_value = waterlevel.waterleveling()  # e.g.) temp\nhumidity\n
    data = t_value + w_value              # e.g.) temp\nhumidity\nwaterlevel\n
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

    while True:
        # establish connection with client
        client, addr = s.accept()

        print('Connected to :', addr)

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (client,))
        try:
            pass
        except KeyboardInterrupt:
            s.close()
            GPIO.cleanup()
            print("Program is exit")


if __name__ == '__main__':
    p_temp = Queue()
    p_cycle = Queue()
    process_temp = Process(target=temp.Main, args=(p_temp,))
    process_temp.start()
    process_water_relay = Process(target=control_relay_water.Main, args=(p_cycle,))
    process_water_relay.start()
    Main()
