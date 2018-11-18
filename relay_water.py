import RPi.GPIO as GPIO
import time

pin = 15


def water_relay(cycle):
    GPIO.output(pin, GPIO.HIGH)  # on
    time.sleep(5)
    GPIO.output(pin, GPIO.LOW)    # off
    time.sleep(cycle)

