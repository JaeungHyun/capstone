# 온풍기 릴레이 제어
def relay_on():
    GPIO.output(pin, GPIO.HIGH)  # on
    print('Heater On')


def relay_off():
    GPIO.output(pin, GPIO.LOW)    # off
    print('Heater Off')


def main():
    relay_on()
    import time
    time.sleep(3)
    relay_off()
    time.sleep(3)
