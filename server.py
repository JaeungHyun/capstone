import socket
from _thread import *
from ctypes import c_double
from multiprocessing import Process, Queue, Value

import RPi.GPIO as GPIO
import json
from collections import OrderedDict

import temp
import waterlevel
import control_relay_water


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
            s.close()                              # socket closed
            GPIO.cleanup()
            '''
            config = OrderedDict()
            config["target_temp"] = recv_temp.value
            config["target_cycle"] = recv_cycle.value
            
            # Save config value
            with open('config.json', 'w', encoding='utf-8') as make_file:
                json.dump(config, make_file, ensure_ascii=False, indent="\t")
            '''
            print("Release all GPIO resource")
            print("Exit program")


if __name__ == '__main__':
    p_temp = Queue()
    p_cycle = Queue()
    recv_temp = Value(c_double, 0.0, lock=False)
    recv_cycle = Value('i', 0)
    process_temp = Process(target=temp.Main, args=(p_temp, recv_temp, ))
    process_temp.start()
    process_water_relay = Process(target=control_relay_water.Main, args=(p_cycle, recv_cycle, ))
    process_water_relay.start()
    Main()
