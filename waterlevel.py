import serial

port = '/dev/ttyACM0'

data = serial.Serial(port, baudrate=9600, timeout = None)

waterlevel = data.readline()



