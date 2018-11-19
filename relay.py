import RPi.GPIO as GPIO

pin = 29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def relay_on():
    GPIO.output(pin, GPIO.HIGH)  # on


def relay_off():
    GPIO.output(pin, GPIO.LOW)

