import RPi.GPIO as GPIO
import Adafruit_DHT


sensor = Adafruit_DHT.DHT22
pin = 4

def temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print("Temp=%0.1f Humidity=%0.1f" % (temperature, humidity))

    stringTemp = str(temperature)+'\n'
