import RPi.GPIO as GPIO
import Adafruit_DHT
import relay
import time
import server

sensor = Adafruit_DHT.DHT22
pin = 4


def checktemp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print("Temp=%0.1f Humidity=%0.1f" % (temperature, humidity))

    stringtemp = str(temperature)+'\n'+str(humidity)+'\n'
    return stringtemp


def main():
    while True:
        humid, temp = Adafruit_DHT.read_retry(sensor, pin)
        target_temp = server.p_temp.recv()

        if target_temp is None:
            continue

        if temp < target_temp:
            relay.relay_on()
        else:
            relay.relay_off()

        print("0.1f" % temp)
        time.sleep(10)


if __name__ == '__main__':
    main()
