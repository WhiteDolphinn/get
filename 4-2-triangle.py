import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    tm = int(input())

    for i in range(0, 255):
        time.sleep(tm/512)
        GPIO.output(dac, dec2bin(i))

    for i in range (255, 0, -1):
        time.sleep(tm/512)
        GPIO.output(dac, dec2bin(i))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()