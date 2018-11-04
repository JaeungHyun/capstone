import serial

port = '/dev/ttyACM0'

data = serial.Serial(port, baudrate=9600, timeout = None)


while 1:
    waterlevel = data.readline()
    print(waterlevel.decode())


