import RPi.GPIO as GPIO
import time

pin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


def water_relay(cycle):
    while True:
        GPIO.output(pin, GPIO.HIGH)  # on
        time.sleep(5)
        GPIO.output(pin, GPIO.LOW)    # off
        time.sleep(cycle-5)

