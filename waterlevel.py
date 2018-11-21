import RPi.GPIO as GPIO

pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

# 수위측정


def waterleveling():
    data = GPIO.input(pin)
    waterleveling = str(data) + '\n'
    print("Status of Water is %s" % waterleveling)
    return waterleveling
