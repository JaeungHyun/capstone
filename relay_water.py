import RPi.GPIO as GPIO
import time

pin = 15                    # pin number를 사용해야함
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


# 솔레노이드 밸브 제어
def water_relay(recv):
    cycle = recv.get()
    print('target_cycle is ', cycle)
    while True:
        GPIO.output(pin, GPIO.HIGH)  # on
        time.sleep(5)
        GPIO.output(pin, GPIO.LOW)    # off
        time.sleep(cycle-5)

