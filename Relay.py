import RPi.GPIO as GPIO

pin = 17

def watering():
    GPIO.setup(pin, GPIO.OUT)  # GPIO Assign mode
    GPIO.output(pin, GPIO.LOW)  # out
    GPIO.output(pin, GPIO.HIGH)  # on