import Adafruit_DHT
import relay
import time


sensor = Adafruit_DHT.DHT22
pin = 17                  # GPIO number를 사용해야함

# check temperature and humidity for Thread of server.py
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
        target_temp = p_temp.value
        print('target temp(1) is ', target_temp.value)
        print(temp)
        if target_temp is None:
            continue

        print('target temp is(2) ', target_temp.value)

        if temp < target_temp.value:
            relay.relay_on()
        else:
            relay.relay_off()

        print("0.1f" % temp)
        time.sleep(10)


if __name__ == '__main__':
    Main()
