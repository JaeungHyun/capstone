import Adafruit_DHT
import relay
import time


sensor = Adafruit_DHT.DHT22
pin = 7


def checktemp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print("Temp=%0.1f Humidity=%0.1f" % (temperature, humidity))

    stringtemp = str(temperature)+'\n'+str(humidity)+'\n'
    return stringtemp


def Main(p_temp):
    print("temp process is started")
    while True:
        humid, temp = Adafruit_DHT.read_retry(sensor, pin)
        target_temp = p_temp.recv()
        print(temp)
        if target_temp is None:
            continue

        if temp < target_temp:
            relay.relay_on()
        else:
            relay.relay_off()

        print("0.1f" % temp)
        # time.sleep(10)


if __name__ == '__main__':
    Main()
