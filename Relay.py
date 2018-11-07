import RPi.GPIO as GPIO
from time import sleep

pin = 17

def relaycontrol():
    GPIO.setup(pin, GPIO.OUT)  # GPIO Assign mode
    GPIO.output(pin, GPIO.LOW)  # out
    sleep(10)
    GPIO.output(pin, GPIO.HIGH)  # on