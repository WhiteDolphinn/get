import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

try:
    #tm = int(input())
    shim = float(input())
    print(shim*3.3, "volts")
    hz = 1000
    
    while True:
        GPIO.output(15, 1)
        time.sleep(shim/hz)
        GPIO.output(15, 0)
        time.sleep((1-shim)/hz)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()