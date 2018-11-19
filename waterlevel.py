import RPi.GPIO as GPIO

pin = 27
data = GPIO.input(pin)


def waterleveling():
    waterleveling = data.decode() + '\n'
    print("Status of Water is %d" % waterleveling)
    return waterleveling
