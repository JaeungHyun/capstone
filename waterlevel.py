import RPi.GPIO as GPIO

pin = 27
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)
data = GPIO.input(pin)


def waterleveling():
    waterleveling = data.decode() + '\n'
    print("Status of Water is %d" % waterleveling)
    return waterleveling
