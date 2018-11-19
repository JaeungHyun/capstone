import RPi.GPIO as GPIO

pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)
data = GPIO.input(pin)

# 수위측정


def waterleveling():
    waterleveling = str(data) + '\n'
    print("Status of Water is %s" % waterleveling)
    return waterleveling
