import RPi.GPIO as GPIO

pin = 17
GPIO.setup(pin, GPIO.IN)

def relay_on():
    GPIO.output(pin, GPIO.HIGH)  # on


def relay_off():
    GPIO.output(pin, GPIO.LOW)

