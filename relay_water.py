import RPi.GPIO as GPIO
import time

pin = 15


def water_relay():
    GPIO.output(pin, GPIO.HIGH)  # on
    time.sleep(5)
    GPIO.output(pin, GPIO.LOW)    # off


def water_relay_first():
    GPIO.output(pin, GPIO.HIGH)  # on
    time.sleep(3)
    GPIO.output(pin, GPIO.LOW)    # off

