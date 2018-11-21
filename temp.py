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

    stringtemp = str(temperature)+'\n'+str(humidity)+'\n'  # wrapping to send to client
    return stringtemp


def Main(p_temp, recv_temp):
    print("temp process is started")

    while True:
        humid, temp = Adafruit_DHT.read_retry(sensor, pin)
        global target_temp
        target_temp = p_temp.get()

        if target_temp is None:
            target_temp = 25.0
            print("Initial target temperature is ", target_temp)
            continue

        if temp < target_temp:
            relay.relay_on()
        else:
            relay.relay_off()

        recv_temp.value = target_temp
        time.sleep(10)


if __name__ == '__main__':
    Main()
