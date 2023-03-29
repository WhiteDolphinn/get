import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for value in range(256):
        GPIO.output(dac, dec2bin(value))
        time.sleep(0.0005)
        compvalue = GPIO.input(comp)
        if compvalue == 0:
            print(value)
            print(dec2bin(value))
            print(3.3*value/256 ,"volts")
            return value
        
        

    print(256, "max")
    return 256


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

try:
    while True:
        value = adc()

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
